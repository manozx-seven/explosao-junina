// ============================================================
// Netlify Function - ponto único de entrada da API.
// Recebe { fn, args } e despacha para o handler correspondente.
// Substitui o google.script.run do Apps Script.
// ============================================================
const handlers = require('../../server/handlers');

// Apenas funções nesta lista podem ser chamadas pelo cliente.
const PUBLICAS = new Set([
  'login',
  'getLogs',
  'getBrincantes', 'addBrincante', 'addBrincantesLote', 'updateBrincante', 'removeBrincante',
  'getEnsaios', 'addEnsaio', 'updateEvento', 'deleteEnsaio',
  'getAvaliacoes', 'salvarAvaliacoes', 'upsertAvaliacao',
  'getAdvertencias', 'addAdvertencia', 'removeAdvertencia',
  'getDashboard', 'getPerfilBrincante', 'getRanking', 'getSimulacaoBonificacao',
  'getConfig', 'getStatusAdesao', 'updateConfig', 'updateConfigMap',
]);

const json = (statusCode, body) => ({
  statusCode,
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify(body),
});

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

  const { fn, args } = payload;
  if (!fn || !PUBLICAS.has(fn) || typeof handlers[fn] !== 'function') {
    return json(400, { __error: `Função não permitida: ${fn}` });
  }

  try {
    const result = await handlers[fn](...(Array.isArray(args) ? args : []));
    // null é resposta válida (ex: getPerfilBrincante) -> retorna body "null"
    return json(200, result === undefined ? null : result);
  } catch (err) {
    console.error(`Erro em ${fn}:`, err);
    return json(500, { __error: err.message || 'Erro interno' });
  }
};
