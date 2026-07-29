// ============================================================
// Netlify Function - ponto único de entrada da API.
// Recebe { fn, args, token } e despacha para o handler correspondente.
// Substitui o google.script.run do Apps Script.
//
// Toda função declara ESCOPO e ARIDADE:
//   escopo -> quem pode chamar (publico | autenticado | brincante | admin)
//   args   -> quantos argumentos vêm do cliente
//
// A sessão é resolvida no servidor e entra SEMPRE como último argumento do
// handler. O cliente não consegue forjar quem é: mesmo que envie argumentos
// a mais, a lista é normalizada para exatamente `args` posições antes de a
// sessão ser anexada.
//
// `autenticado` = qualquer sessão válida (admin ou brincante). As funções
// desse escopo leem o ID do usuário DA SESSÃO quando quem chama não é admin
// — ver getPerfilBrincante e setDestinoBonificacao em server/handlers.js.
// ============================================================
const handlers = require('../../server/handlers');
const { validarSessao } = require('../../server/sessoes');

const FUNCOES = {
  // --- público (sem token) ---
  login:                   { escopo: 'publico',     args: 2 },

  // --- qualquer sessão válida ---
  logout:                  { escopo: 'autenticado', args: 0 },
  entrarComoBrincante:     { escopo: 'autenticado', args: 0 },
  getPerfilBrincante:      { escopo: 'autenticado', args: 1 },
  setDestinoBonificacao:   { escopo: 'autenticado', args: 2 },
  // Missão de captação de sócios: o brincante declara por si (o ID vem da
  // sessão) e apaga só a própria enquanto pendente — travas em handlers.js.
  addIndicacao:            { escopo: 'autenticado', args: 1 },
  removeIndicacao:         { escopo: 'autenticado', args: 1 },

  // --- coordenação ---
  getLogs:                 { escopo: 'admin', args: 1 },

  getBrincantes:           { escopo: 'admin', args: 0 },
  addBrincante:            { escopo: 'admin', args: 1 },
  addBrincantesLote:       { escopo: 'admin', args: 1 },
  updateBrincante:         { escopo: 'admin', args: 2 },
  removeBrincante:         { escopo: 'admin', args: 1 },

  getEnsaios:              { escopo: 'admin', args: 0 },
  addEnsaio:               { escopo: 'admin', args: 1 },
  updateEvento:            { escopo: 'admin', args: 2 },
  deleteEnsaio:            { escopo: 'admin', args: 1 },

  getAvaliacoes:           { escopo: 'admin', args: 1 },
  salvarAvaliacoes:        { escopo: 'admin', args: 2 },
  upsertAvaliacao:         { escopo: 'admin', args: 3 },

  getAdvertencias:         { escopo: 'admin', args: 1 },
  addAdvertencia:          { escopo: 'admin', args: 1 },
  removeAdvertencia:       { escopo: 'admin', args: 1 },

  getIndicacoes:           { escopo: 'admin', args: 1 },
  decidirIndicacao:        { escopo: 'admin', args: 3 },
  getCaptacao:             { escopo: 'admin', args: 0 },

  getDashboard:            { escopo: 'admin', args: 0 },
  getRanking:              { escopo: 'admin', args: 0 },
  getSimulacaoBonificacao: { escopo: 'admin', args: 0 },

  getConfig:               { escopo: 'admin', args: 0 },
  getStatusAdesao:         { escopo: 'admin', args: 0 },
  updateConfig:            { escopo: 'admin', args: 2 },
  updateConfigMap:         { escopo: 'admin', args: 1 },
};

const json = (statusCode, body) => ({
  statusCode,
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify(body),
});

// `__auth: true` avisa o front para descartar a sessão e voltar ao login.
const semAuth = (msg) => json(401, { __error: msg, __auth: true });

exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return json(405, { __error: 'Método não permitido' });
  }

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch (e) {
    return json(400, { __error: 'JSON inválido' });
  }

  const { fn, args, token } = payload;
  const def = Object.prototype.hasOwnProperty.call(FUNCOES, fn) ? FUNCOES[fn] : null;
  if (!def || typeof handlers[fn] !== 'function') {
    return json(400, { __error: `Função não permitida: ${fn}` });
  }

  // ---- autenticação e autorização ----
  let sessao = null;
  if (def.escopo !== 'publico') {
    sessao = await validarSessao(token);
    if (!sessao) return semAuth('Sessão expirada. Entre novamente.');
    if (def.escopo !== 'autenticado' && sessao.tipo !== def.escopo) {
      return json(403, { __error: 'Sem permissão para esta operação' });
    }
  }

  // Normaliza para exatamente `def.args` posições: argumentos a mais são
  // descartados (senão o cliente empurraria um objeto para o lugar da
  // sessão) e a menos viram undefined (para a sessão não escorregar).
  const recebidos = Array.isArray(args) ? args : [];
  const argsCliente = Array.from({ length: def.args }, (_, i) => recebidos[i]);

  try {
    const result = await handlers[fn](...argsCliente, sessao);
    // null é resposta válida (ex: getPerfilBrincante) -> retorna body "null"
    return json(200, result === undefined ? null : result);
  } catch (err) {
    console.error(`Erro em ${fn}:`, err);
    return json(500, { __error: err.message || 'Erro interno' });
  }
};
