// ============================================================
// Sessões — autenticação por token para a API do Sistema de Avaliação.
//
// Coleção `sessoes/{token}`:
//   Token, Tipo ('admin'|'brincante'), BrincanteID, Nome, CriadoEm, ExpiraEm
//
// Regra central: quem o usuário É vem SEMPRE daqui, nunca de um argumento
// enviado pelo navegador. Antes disso, o cliente mandava o objeto `usuario`
// junto da requisição — qualquer um podia se declarar "Coordenação".
//
// Mesmo desenho já em produção no projeto irmão (Site Sócio Torcedor).
// ============================================================
const crypto = require('crypto');
const { getDb } = require('./firebase');

// Duração da sessão por tipo de usuário.
const DURACAO_MS = {
  admin: 12 * 60 * 60 * 1000,          // 12 horas — a coordenação mexe em dados de todos
  brincante: 30 * 24 * 60 * 60 * 1000, // 30 dias — o brincante só consulta o próprio perfil
};

// 64 caracteres hex. O formato é validado antes de virar caminho no banco:
// sem isso, um token com '/' alcançaria outro documento.
const FORMATO_TOKEN = /^[a-f0-9]{64}$/;

function novoToken() {
  return crypto.randomBytes(32).toString('hex');
}

function tokenValido_(token) {
  return typeof token === 'string' && FORMATO_TOKEN.test(token);
}

/**
 * Cria uma sessão e devolve o objeto no formato que os handlers já esperam
 * (`usuario.id` / `usuario.nome`), agora vindo do servidor.
 * @param {'admin'|'brincante'} tipo
 * @param {{id?:string, nome?:string}} dados
 */
async function criarSessao(tipo, dados) {
  const agora = Date.now();
  const token = novoToken();
  const id = (dados && dados.id) || '';
  const nome = (dados && dados.nome) || '';
  await getDb().collection('sessoes').doc(token).set({
    Token: token,
    Tipo: tipo,
    BrincanteID: id,
    Nome: nome,
    CriadoEm: new Date(agora).toISOString(),
    ExpiraEm: new Date(agora + (DURACAO_MS[tipo] || DURACAO_MS.brincante)).toISOString(),
  });
  limparExpiradas_();  // oportunista, não bloqueia
  return { token, tipo, id, nome };
}

/**
 * Valida o token recebido do cliente.
 * @returns {Promise<{token,tipo,id,nome}|null>} null se ausente, inválido ou expirado.
 */
async function validarSessao(token) {
  if (!tokenValido_(token)) return null;
  const ref = getDb().collection('sessoes').doc(token);
  const doc = await ref.get();
  if (!doc.exists) return null;

  const s = doc.data();
  if (new Date(s.ExpiraEm).getTime() < Date.now()) {
    try { await ref.delete(); } catch (e) { /* expirada é o que importa */ }
    return null;
  }
  return { token, tipo: s.Tipo, id: s.BrincanteID || '', nome: s.Nome || '' };
}

/**
 * Rebaixa uma sessão de admin para brincante.
 * Usado quando quem tem papel duplo (coordenação + item/brincante) escolhe
 * entrar como brincante: a escolha deixa de ser só visual e o token perde o
 * poder de administrar. Só rebaixa — nunca promove.
 */
async function rebaixarParaBrincante(token) {
  if (!tokenValido_(token)) return false;
  const ref = getDb().collection('sessoes').doc(token);
  const doc = await ref.get();
  if (!doc.exists) return false;
  await ref.update({
    Tipo: 'brincante',
    // a sessão de brincante dura mais, mas manter o prazo curto do admin é
    // o lado seguro: rebaixar não pode esticar a validade do token.
  });
  return true;
}

async function encerrarSessao(token) {
  if (!tokenValido_(token)) return;
  try { await getDb().collection('sessoes').doc(token).delete(); } catch (e) { /* idempotente */ }
}

/**
 * Remove todas as sessões de um brincante.
 * Chamado quando o CPF muda — como o CPF é a senha, trocar a credencial
 * precisa derrubar quem já estava logado com a antiga.
 */
async function encerrarSessoesDoBrincante(brincanteId) {
  if (!brincanteId) return;
  try {
    const snap = await getDb().collection('sessoes').get();
    const mortas = snap.docs.filter((d) => d.data().BrincanteID === brincanteId);
    await Promise.all(mortas.map((d) => getDb().collection('sessoes').doc(d.id).delete()));
  } catch (e) { /* não pode derrubar a edição do brincante */ }
}

// Netlify Functions não têm cron: a faxina acontece de carona no login,
// em 1 de cada 10 vezes, para não pagar a varredura em toda entrada.
function limparExpiradas_() {
  if (Math.random() > 0.1) return;
  (async () => {
    try {
      const agora = Date.now();
      const snap = await getDb().collection('sessoes').get();
      const vencidas = snap.docs.filter((d) => {
        const e = d.data().ExpiraEm;
        return !e || new Date(e).getTime() < agora;
      });
      await Promise.all(vencidas.map((d) => getDb().collection('sessoes').doc(d.id).delete()));
    } catch (e) { /* faxina nunca derruba a operação */ }
  })();
}

module.exports = {
  criarSessao, validarSessao, rebaixarParaBrincante,
  encerrarSessao, encerrarSessoesDoBrincante,
};
