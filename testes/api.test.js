// ============================================================
// Testes da camada de AUTENTICAÇÃO da API — escopos, anti-forja de sessão e
// as travas que impedem um brincante de acessar o dado de outro.
//
// Não precisa de Firebase nem de `netlify dev`: injeta um Firestore em memória
// no lugar do `server/firebase.js` e chama o handler da Netlify Function
// diretamente, como o Netlify faria.
//
//   node testes/api.test.js        (ou: npm test)
// ============================================================
const path = require('path');

const RAIZ = path.join(__dirname, '..');

// ---------- Firestore falso ----------
const store = {};                       // { colecao: { docId: dados } }
let autoSeq = 0;
const col = (n) => (store[n] = store[n] || {});

function snapDoc(name, id) {
  const d = col(name)[id];
  return { id, exists: d !== undefined, data: () => d };
}
function docRef(name, id) {
  id = String(id);
  return {
    get: async () => snapDoc(name, id),
    set: async (v) => { col(name)[id] = JSON.parse(JSON.stringify(v)); },
    update: async (v) => {
      if (col(name)[id] === undefined) throw new Error('NOT_FOUND ' + name + '/' + id);
      Object.assign(col(name)[id], JSON.parse(JSON.stringify(v)));
    },
    delete: async () => { delete col(name)[id]; },
  };
}
function query(name, ids) {
  const list = () => (ids || Object.keys(col(name))).map((i) => snapDoc(name, i));
  return {
    orderBy: () => query(name, ids),
    limit: (n) => query(name, (ids || Object.keys(col(name))).slice(0, n)),
    get: async () => { const docs = list(); return { docs, forEach: (f) => docs.forEach(f), size: docs.length }; },
  };
}
function collection(name) {
  return Object.assign(query(name), {
    doc: (id) => docRef(name, id),
    add: async (v) => { const id = 'auto' + (++autoSeq); col(name)[id] = JSON.parse(JSON.stringify(v)); return { id }; },
  });
}
const fakeDb = {
  collection,
  runTransaction: async (fn) => fn({
    get: async (ref) => ref.get(),
    set: async (ref, v) => ref.set(v),
  }),
};

// Injeta ANTES de qualquer require dos handlers: eles desestruturam `getDb` na
// carga do módulo, então trocar depois não teria efeito.
const fbPath = require.resolve(path.join(RAIZ, 'server', 'firebase.js'));
require.cache[fbPath] = {
  id: fbPath, filename: fbPath, loaded: true, children: [], paths: [],
  exports: { getDb: () => fakeDb, admin: {} },
};

const api = require(path.join(RAIZ, 'netlify', 'functions', 'api.js'));

// ---------- dados de teste ----------
col('brincantes').DEV = { ID: 'DEV', Nome: 'Coordenação', CPF: '123456', Tipo: 'coordenacao' };
col('brincantes').EXP202701 = { ID: 'EXP202701', Nome: 'Maria', CPF: '11122233344', Tipo: 'brincante', DestinoBonificacao: 'resgatar' };
col('brincantes').EXP202702 = { ID: 'EXP202702', Nome: 'João', CPF: '55566677788', Tipo: 'brincante', DestinoBonificacao: 'resgatar' };
col('config').app = { escolhaDestinoLiberada: 'sim' };

const call = async (fn, args, token) => {
  const r = await api.handler({ httpMethod: 'POST', body: JSON.stringify({ fn, args, token }) });
  return { status: r.statusCode, body: JSON.parse(r.body) };
};

let falhas = 0;
function ok(cond, msg, extra) {
  if (cond) console.log('  ok   ' + msg);
  else { falhas++; console.log('  FALHA ' + msg + (extra !== undefined ? '  -> ' + JSON.stringify(extra) : '')); }
}

(async () => {
  console.log('\n== API sem token ==');
  let r = await call('getBrincantes', []);
  ok(r.status === 401, 'getBrincantes sem token -> 401', r);
  ok(r.body.__auth === true, 'resposta marca __auth para o front derrubar a sessão', r.body);
  r = await call('removeBrincante', ['EXP202701']);
  ok(r.status === 401, 'removeBrincante sem token -> 401', r);
  ok(col('brincantes').EXP202701 !== undefined, 'brincante NÃO foi removido');
  r = await call('updateConfigMap', [{ valorEnsaio: '99' }]);
  ok(r.status === 401 && col('config').app.valorEnsaio === undefined, 'config NÃO foi alterada sem token');

  console.log('\n== tokens inválidos ==');
  ok((await call('getBrincantes', [], 'a'.repeat(64))).status === 401, 'token forjado -> 401');
  ok((await call('getBrincantes', [], '../brincantes/DEV')).status === 401, 'path injection -> 401');
  ok((await call('getBrincantes', [], 'abc')).status === 401, 'token curto -> 401');
  ok((await call('getBrincantes', [], { fake: true })).status === 401, 'token não-string -> 401');

  console.log('\n== função fora do mapa ==');
  r = await call('getConfigMap_', []);
  ok(r.status === 400, 'helper interno não é chamável', r);

  console.log('\n== login ==');
  r = await call('login', ['DEV', '999999']);
  ok(r.body.success === false && !r.body.token, 'senha errada não devolve token', r.body);
  r = await call('login', ['DEV', '123456']);
  const tokenAdmin = r.body.token;
  ok(/^[a-f0-9]{64}$/.test(tokenAdmin || ''), 'login admin devolve token de 64 chars', r.body);
  r = await call('login', ['EXP202701', '11122233344']);
  const tokenMaria = r.body.token;
  ok(/^[a-f0-9]{64}$/.test(tokenMaria || ''), 'login brincante devolve token');

  console.log('\n== escopos ==');
  r = await call('getBrincantes', [], tokenAdmin);
  ok(r.status === 200 && Array.isArray(r.body), 'admin lê getBrincantes', r);
  ok((await call('getBrincantes', [], tokenMaria)).status === 403, 'brincante em getBrincantes -> 403');
  ok((await call('updateConfigMap', [{ valorEnsaio: '99' }], tokenMaria)).status === 403, 'brincante em updateConfigMap -> 403');
  ok(col('config').app.valorEnsaio === undefined, 'config continua intacta');
  ok((await call('getLogs', [5], tokenMaria)).status === 403, 'brincante em getLogs -> 403');
  ok((await call('getSimulacaoBonificacao', [], tokenMaria)).status === 403, 'brincante na bonificação geral -> 403');

  console.log('\n== o brincante só acessa o próprio dado ==');
  r = await call('setDestinoBonificacao', ['EXP202702', 'doar'], tokenMaria);
  ok(r.status === 200, 'chamada aceita');
  ok(col('brincantes').EXP202702.DestinoBonificacao === 'resgatar',
     'destino do João intacto (ID do argumento ignorado)', col('brincantes').EXP202702.DestinoBonificacao);
  ok(col('brincantes').EXP202701.DestinoBonificacao === 'doar', 'mudou o da Maria — o ID veio da sessão');
  await call('setDestinoBonificacao', ['EXP202702', 'doar'], tokenAdmin);
  ok(col('brincantes').EXP202702.DestinoBonificacao === 'doar', 'admin pode alterar o de outro');

  console.log('\n== anti-forja de sessão ==');
  await call('addBrincante', [{ nome: 'Fulano' }, { id: 'HACKER', nome: 'HACKER' }], tokenAdmin);
  const logs = Object.values(col('logs'));
  ok(!logs.some((l) => l.UsuarioNome === 'HACKER' || l.UsuarioID === 'HACKER'),
     'argumento extra NÃO vira sessão', logs.filter((l) => /HACKER/.test(JSON.stringify(l))));
  const ultimo = logs[logs.length - 1];
  ok(ultimo && ultimo.UsuarioNome === 'Coordenação', 'log gravou o usuário da sessão', ultimo);

  console.log('\n== papel duplo: rebaixar a sessão ==');
  col('brincantes').EXP202703 = { ID: 'EXP202703', Nome: 'Ana', CPF: '99988877766', Tipo: 'item_coord' };
  r = await call('login', ['EXP202703', '99988877766']);
  const tokenAna = r.body.token;
  ok((await call('getBrincantes', [], tokenAna)).status === 200, 'coordenação dupla nasce admin');
  await call('entrarComoBrincante', [], tokenAna);
  ok((await call('getBrincantes', [], tokenAna)).status === 403, 'depois de rebaixar, perde o acesso admin');

  console.log('\n== troca de CPF derruba a sessão ==');
  await call('updateBrincante', ['EXP202701', { cpf: '00011122233' }], tokenAdmin);
  ok((await call('getPerfilBrincante', ['EXP202701'], tokenMaria)).status === 401,
     'token antigo da Maria foi invalidado (o CPF é a senha)');

  console.log('\n== logout ==');
  await call('logout', [], tokenAdmin);
  ok((await call('getBrincantes', [], tokenAdmin)).status === 401, 'token não vale mais depois do logout');

  console.log('\n== resultado ==');
  if (falhas) { console.log('  ' + falhas + ' FALHA(S)'); process.exit(1); }
  console.log('  TODOS OS TESTES PASSARAM');
})().catch((e) => { console.error('ERRO:', e); process.exit(2); });
