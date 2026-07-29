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
  const base = () => ids || Object.keys(col(name));
  const list = () => base().map((i) => snapDoc(name, i));
  return {
    // Só '==' — é o único operador que os handlers usam.
    where: (campo, op, valor) => query(name, base().filter((i) => {
      const d = col(name)[i];
      return d !== undefined && (op === '==' ? d[campo] === valor : true);
    })),
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

  console.log('\n== missão de captação: escopos e trava de dono ==');
  ok((await call('getCaptacao', [], tokenMaria)).status === 403, 'brincante no painel de captação -> 403');
  ok((await call('getIndicacoes', [{}], tokenMaria)).status === 403, 'brincante lendo todas as indicações -> 403');
  ok((await call('decidirIndicacao', ['x', 'confirmada', ''], tokenMaria)).status === 403, 'brincante confirmando indicação -> 403');

  // O ID do argumento é ignorado: a missão é creditada a quem está na sessão.
  r = await call('addIndicacao', [{ brincanteId: 'EXP202702', nome: 'Tia Zuleide', telefone: '(92) 99888-7766' }], tokenMaria);
  ok(r.body.success === true, 'brincante declara indicação', r.body);
  const idIndMaria = r.body.id;
  let ind = col('indicacoes')[idIndMaria];
  ok(ind.BrincanteID === 'EXP202701', 'creditada à Maria (ID veio da sessão, não do argumento)', ind.BrincanteID);
  ok(ind.Status === 'pendente', 'nasce pendente — quem confirma é a coordenação', ind.Status);
  ok(ind.Telefone === '92998887766', 'telefone normalizado para dígitos', ind.Telefone);

  console.log('\n== privacidade: CPF e nascimento nunca são gravados ==');
  r = await call('addIndicacao', [{
    nome: 'Seu Raimundo', telefone: '92991112233',
    cpf: '12345678901', CPF: '12345678901', dataNascimento: '1970-05-02', DataNascimento: '1970-05-02',
    observacao: 'CPF 123.456.789-01',
  }], tokenMaria);
  ok(r.body.success === true, 'declaração aceita', r.body);
  const gravado = col('indicacoes')[r.body.id];
  const campos = Object.keys(gravado).sort().join(',');
  ok(campos === 'BrincanteID,DataDecisao,DataDeclaracao,DecididaPor,DeclaradaPor,MotivoRecusa,Nome,Status,Telefone',
     'documento tem só os campos previstos', campos);
  ok(!/12345678901|1970-05-02/.test(JSON.stringify(gravado)),
     'CPF e data de nascimento NÃO entraram no banco', gravado);

  console.log('\n== indicação duplicada ==');
  r = await call('addIndicacao', [{ nome: 'Zuleide de novo', telefone: '92 99888 7766' }], tokenMaria);
  ok(r.body.success === false, 'mesmo telefone é recusado', r.body);
  r = await call('addIndicacao', [{ brincanteId: 'EXP202702', nome: 'Zuleide', telefone: '92998887766' }], tokenAdmin);
  ok(r.body.success === false && /outro brincante/.test(r.body.message || ''),
     'outro brincante não rouba o contato já declarado', r.body);

  console.log('\n== o brincante só apaga a própria indicação ==');
  r = await call('addIndicacao', [{ brincanteId: 'EXP202702', nome: 'Compadre do João', telefone: '92993334455' }], tokenAdmin);
  const idIndJoao = r.body.id;
  ok(col('indicacoes')[idIndJoao].BrincanteID === 'EXP202702', 'admin declara em nome de outro');
  r = await call('removeIndicacao', [idIndJoao], tokenMaria);
  ok(r.body.success === false && col('indicacoes')[idIndJoao] !== undefined,
     'Maria não apaga a indicação do João', r.body);

  console.log('\n== decisão da coordenação ==');
  r = await call('decidirIndicacao', [idIndMaria, 'confirmada', ''], tokenAdmin);
  ok(r.body.success === true && col('indicacoes')[idIndMaria].Status === 'confirmada', 'admin confirma', r.body);
  ok(/Coordenação/.test(col('indicacoes')[idIndMaria].DecididaPor), 'registra quem confirmou', col('indicacoes')[idIndMaria].DecididaPor);
  r = await call('removeIndicacao', [idIndMaria], tokenMaria);
  ok(r.body.success === false && col('indicacoes')[idIndMaria] !== undefined,
     'brincante não apaga o que já foi decidido', r.body);
  ok((await call('decidirIndicacao', [idIndMaria, 'invalido', ''], tokenAdmin)).body.success === false,
     'decisão fora da lista é recusada');

  console.log('\n== troféu e painel de captação ==');
  col('config').app.metaSociosPorBrincante = '2';
  await call('addIndicacao', [{ nome: 'Vizinha Rosa', telefone: '92994445566' }], tokenMaria);
  const idRosa = Object.keys(col('indicacoes')).find((k) => col('indicacoes')[k].Nome === 'Vizinha Rosa');
  await call('decidirIndicacao', [idRosa, 'confirmada', ''], tokenAdmin);
  r = await call('getCaptacao', [], tokenAdmin);
  const maria = r.body.ranking.find((x) => x.id === 'EXP202701');
  ok(maria.confirmadas === 2 && maria.trofeu === true, 'Maria bateu a meta e ganhou o troféu', maria);
  ok(r.body.trofeuNome === 'Chamador de Gente', 'nome do troféu vem do servidor (Plano §9)', r.body.trofeuNome);
  const joao = r.body.ranking.find((x) => x.id === 'EXP202702');
  ok(joao.confirmadas === 0 && joao.pendentes === 1 && joao.trofeu === false, 'João segue sem troféu', joao);
  ok(r.body.ranking[0].id === 'EXP202701', 'ranking ordenado por confirmadas');

  console.log('\n== a missão não contamina desempenho nem bonificação ==');
  r = await call('getPerfilBrincante', ['EXP202701'], tokenMaria);
  ok(r.status === 200 && r.body.captacao.confirmadas === 2, 'perfil traz a captação da própria pessoa', r.body.captacao);
  ok(r.body.totalEnsaios === 0 && r.body.presencas === 0 && r.body.percPresenca === 0,
     'frequência intacta (indicação não é presença)', { t: r.body.totalEnsaios, p: r.body.percPresenca });
  ok(r.body.bonificacao === '0.00', 'bonificação intacta (missão não vira dinheiro)', r.body.bonificacao);
  const rank = (await call('getRanking', [], tokenAdmin)).body;
  ok(rank.every((x) => x.presencas === 0 && x.percPresenca === 0 && x.totalAvaliacoes === 0),
     'ranking de desempenho segue zerado — indicação não é presença nem nota', rank);
  const sim = (await call('getSimulacaoBonificacao', [], tokenAdmin)).body;
  ok(sim.totalGeral === '0.00', 'simulação de bonificação não virou dinheiro', sim.totalGeral);

  console.log('\n== teto da bonificação (Cláusula Sexta, III, "e") ==');
  // 12 ensaios a R$ 10 = R$ 120 acumulados, contra um teto de R$ 80.
  Object.assign(col('config').app, {
    valorEnsaio: '10.00', tetoBonificacao: '80.00',
    inicioContagem: '2027-05-01', fimContagem: '2027-07-31',
  });
  Object.assign(col('brincantes').EXP202702, { OptBonificacao: 'sim', StatusAtivacao: 'ativado' });
  for (let i = 1; i <= 12; i++) {
    const id = 'ENS2027050' + i;
    col('ensaios')[id] = { ID: id, Data: '2027-05-' + String(i).padStart(2, '0'), Tipo: 'regular', Status: 'realizado' };
    col('avaliacoes')['AV' + id] = { EnsaioID: id, BrincanteID: 'EXP202702', Presente: 'sim', Nota: 5 };
  }
  r = await call('getPerfilBrincante', ['EXP202702'], tokenAdmin);
  ok(r.body.bonificacaoSemTeto === '120.00', 'acumulou R$ 120 antes do teto', r.body.bonificacaoSemTeto);
  ok(r.body.bonificacao === '80.00', 'perfil trava a bonificação no teto', r.body.bonificacao);
  ok(r.body.teto === '80.00' && r.body.tetoAtingido === true, 'perfil avisa que o teto foi atingido', { t: r.body.teto, a: r.body.tetoAtingido });

  let simT = (await call('getSimulacaoBonificacao', [], tokenAdmin)).body;
  let joaoT = simT.lista.find((x) => x.nome === 'João');
  ok(joaoT.valorAcumulado === '80.00' && joaoT.valorSemTeto === '120.00' && joaoT.atingiuTeto === true,
     'simulação aplica o mesmo teto do perfil', joaoT);
  ok(simT.totalGeral === '80.00' && simT.noTeto === 1, 'total da coordenação respeita o teto', { t: simT.totalGeral, n: simT.noTeto });
  ok(simT.teto === '80.00' && simT.tetoTotal === '80.00', 'compromisso máximo = teto × elegíveis', { t: simT.teto, tt: simT.tetoTotal });

  // A ordem importa: teto primeiro, sanção depois. Se fosse ao contrário,
  // 120 × 50% = 60 daria MAIS a quem passou do teto do que os 40 corretos.
  await call('addAdvertencia', [{ brincanteId: 'EXP202702', nivel: 'formal', motivo: 'teste' }], tokenAdmin);
  r = await call('getPerfilBrincante', ['EXP202702'], tokenAdmin);
  ok(r.body.bonificacao === '40.00', 'sanção de −50% incide sobre o teto, não sobre o acumulado', r.body.bonificacao);

  // Teto zerado = sem teto (proteção contra apagar o campo na tela de config).
  col('config').app.tetoBonificacao = '0';
  simT = (await call('getSimulacaoBonificacao', [], tokenAdmin)).body;
  joaoT = simT.lista.find((x) => x.nome === 'João');
  ok(joaoT.valorSemTeto === '120.00' && joaoT.atingiuTeto === false && joaoT.valorAcumulado === '60.00',
     'teto 0 desliga o limite (e a sanção volta a valer sobre os R$ 120)', joaoT);
  col('config').app.tetoBonificacao = '80.00';

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
