// ============================================================
// SISTEMA DE AVALIAÇÃO - EXPLOSÃO JUNINA DE BERURI
// Backend portado do Apps Script (Código.gs) para Firestore.
//
// Modelo de dados no Firestore:
//   config/app              -> documento único com o mapa de configurações
//   counters/brincantes     -> { seq } sequência para gerar IDs EXP2026xx
//   brincantes/{ID}         -> doc id = ID (ex: EXP202601)
//   ensaios/{ID}            -> doc id = ID (ex: ENS20260210_1234)
//   avaliacoes/{autoId}     -> { EnsaioID, BrincanteID, ... }
//   logs/{autoId}           -> { DataHora, UsuarioID, ... }
// ============================================================
const { getDb } = require('./firebase');

const DEFAULT_CONFIG = {
  valorEnsaio: '0.50',
  valorApresentacao: '1.00',
  valorFestival: '5.00',
  mesesAtivacao: '3',
  frequenciaMinima: '75',
  notaMinima: '4',
  percentualNotaMinima: '75',
  temporada: '2026',
  inicioTemporada: '2026-02-01',
  fimContagem: '2026-07-31',
  fimAdesao: '2026-04-30',
};

// ---------- helpers ----------
function today() { return new Date().toISOString().slice(0, 10); }
function nowIso() { return new Date().toISOString(); }
function normalizaCpf(cpf) { return String(cpf || '').replace(/\D/g, '').trim().padStart(11, '0'); }

async function getConfigMap_() {
  const snap = await getDb().collection('config').doc('app').get();
  return { ...DEFAULT_CONFIG, ...(snap.exists ? snap.data() : {}) };
}

async function registrarLog_(usuarioId, usuarioNome, acao, detalhes) {
  try {
    await getDb().collection('logs').add({
      DataHora: nowIso(),
      UsuarioID: usuarioId,
      UsuarioNome: usuarioNome,
      Acao: acao,
      Detalhes: detalhes,
    });
  } catch (e) {
    // Silencia erros de log para não quebrar operações
    console.error('Erro ao registrar log:', e);
  }
}

async function proximoId_() {
  const db = getDb();
  const config = await getConfigMap_();
  const temporada = config.temporada || '2026';
  const counterRef = db.collection('counters').doc('brincantes');
  const seq = await db.runTransaction(async (t) => {
    const doc = await t.get(counterRef);
    const cur = doc.exists ? (doc.data().seq || 0) : 0;
    const next = cur + 1;
    t.set(counterRef, { seq: next }, { merge: true });
    return next;
  });
  return 'EXP' + temporada + String(seq).padStart(2, '0');
}

// ============================================================
// AUTENTICAÇÃO - Login por ID + CPF
// ============================================================
async function login(id, cpf) {
  const cpfLimpo = normalizaCpf(cpf);
  const idLimpo = String(id).trim().toUpperCase();

  const doc = await getDb().collection('brincantes').doc(idLimpo).get();
  if (doc.exists) {
    const b = doc.data();
    if (normalizaCpf(b.CPF) === cpfLimpo) {
      await registrarLog_(idLimpo, b.Nome, 'LOGIN', 'Acesso ao sistema');
      return {
        success: true,
        role: b.Tipo === 'coordenacao' ? 'admin' : 'brincante',
        nome: b.Nome,
        id: b.ID,
        apelido: b.Apelido,
        fila: b.Fila,
        tipo: b.Tipo,
      };
    }
  }
  return { success: false, message: 'ID ou CPF inválido' };
}

// ============================================================
// LOGS
// ============================================================
async function getLogs(limite) {
  let q = getDb().collection('logs').orderBy('DataHora', 'desc');
  if (limite) q = q.limit(Number(limite));
  const snap = await q.get();
  return snap.docs.map((d) => {
    const r = d.data();
    return {
      dataHora: r.DataHora,
      usuarioId: r.UsuarioID,
      usuarioNome: r.UsuarioNome,
      acao: r.Acao,
      detalhes: r.Detalhes,
    };
  });
}

// ============================================================
// BRINCANTES - CRUD
// ============================================================
function normalizaBrincante_(b) {
  return {
    ID: b.ID || '',
    Nome: b.Nome || '',
    Apelido: b.Apelido || '',
    CPF: b.CPF || '',
    Fila: b.Fila || '',
    Posicao: b.Posicao || '',
    Tipo: b.Tipo || 'brincante',
    DataAdesao: b.DataAdesao || '',
    OptBonificacao: b.OptBonificacao || 'nao',
    StatusAtivacao: b.StatusAtivacao || 'pendente',
    QualificacaoExtra: b.QualificacaoExtra || '',
  };
}

async function getBrincantes() {
  const snap = await getDb().collection('brincantes').get();
  return snap.docs.map((d) => normalizaBrincante_(d.data()));
}

async function addBrincante(dados, usuario) {
  const config = await getConfigMap_();
  const fimAdesao = config.fimAdesao || '2026-04-30';
  // Bloqueia opt-in bonificação fora do período de adesão
  if (today() > fimAdesao && dados.optBonificacao === 'sim') {
    dados.optBonificacao = 'nao';
  }

  const id = await proximoId_();
  const brincante = {
    ID: id,
    Nome: dados.nome,
    Apelido: dados.apelido || '',
    CPF: normalizaCpf(dados.cpf),
    Fila: dados.fila || '',
    Posicao: dados.posicao || '',
    Tipo: dados.tipo || 'brincante',
    DataAdesao: today(),
    OptBonificacao: dados.optBonificacao || 'nao',
    StatusAtivacao: 'pendente',
    QualificacaoExtra: '',
  };
  await getDb().collection('brincantes').doc(id).set(brincante);

  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'CADASTRO', `Brincante cadastrado: ${dados.nome} (${id})`);
  }
  return { success: true, id, message: `Brincante cadastrado! ID: ${id}` };
}

async function updateBrincante(id, dados, usuario) {
  const ref = getDb().collection('brincantes').doc(String(id).trim());
  const doc = await ref.get();
  if (!doc.exists) return { success: false, message: 'Brincante não encontrado' };

  const campoMap = {
    nome: 'Nome', apelido: 'Apelido', cpf: 'CPF', fila: 'Fila', posicao: 'Posicao',
    tipo: 'Tipo', optBonificacao: 'OptBonificacao', statusAtivacao: 'StatusAtivacao',
    qualificacaoExtra: 'QualificacaoExtra',
  };
  const update = {};
  const changes = [];
  for (const [k, field] of Object.entries(campoMap)) {
    if (dados[k] !== undefined) {
      update[field] = k === 'cpf' ? normalizaCpf(dados[k]) : dados[k];
      changes.push(k);
    }
  }
  if (changes.length) await ref.update(update);

  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'EDIÇÃO', `Brincante ${id} editado. Campos: ${changes.join(', ')}`);
  }
  return { success: true };
}

async function removeBrincante(id, usuario) {
  const ref = getDb().collection('brincantes').doc(String(id).trim());
  const doc = await ref.get();
  if (!doc.exists) return { success: false };
  const nome = doc.data().Nome;
  await ref.delete();
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'EXCLUSÃO', `Brincante removido: ${nome} (${id})`);
  }
  return { success: true };
}

// ============================================================
// ENSAIOS
// ============================================================
async function getEnsaios() {
  const snap = await getDb().collection('ensaios').get();
  return snap.docs.map((d) => {
    const r = d.data();
    return { ID: r.ID, Data: r.Data, Tipo: r.Tipo, Descricao: r.Descricao, CriadoPor: r.CriadoPor };
  });
}

async function addEnsaio(dados, usuario) {
  const dataFormatada = String(dados.data).replace(/-/g, '');
  const id = 'ENS' + dataFormatada + '_' + String(Date.now()).slice(-4);
  const criadoPor = usuario ? `${usuario.nome} (${usuario.id})` : '';
  await getDb().collection('ensaios').doc(id).set({
    ID: id, Data: dados.data, Tipo: dados.tipo, Descricao: dados.descricao || '', CriadoPor: criadoPor,
  });
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'ENSAIO_CRIADO', `Ensaio ${id}: ${dados.tipo} em ${dados.data}`);
  }
  return { success: true, id };
}

async function deleteEnsaio(id, usuario) {
  const db = getDb();
  const ref = db.collection('ensaios').doc(id);
  const doc = await ref.get();
  if (!doc.exists) return { success: false };
  const info = `${doc.data().Tipo} em ${doc.data().Data}`;
  await ref.delete();
  // Deletar avaliações desse ensaio
  const avSnap = await db.collection('avaliacoes').where('EnsaioID', '==', id).get();
  const batch = db.batch();
  avSnap.docs.forEach((d) => batch.delete(d.ref));
  await batch.commit();
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'ENSAIO_EXCLUIDO', `Ensaio ${id} excluído: ${info}`);
  }
  return { success: true };
}

// ============================================================
// AVALIAÇÕES
// ============================================================
async function getAvaliacoes(filtro) {
  let q = getDb().collection('avaliacoes');
  if (filtro && filtro.ensaioId) q = q.where('EnsaioID', '==', filtro.ensaioId);
  if (filtro && filtro.brincanteId) q = q.where('BrincanteID', '==', filtro.brincanteId);
  const snap = await q.get();
  return snap.docs.map((d) => {
    const r = d.data();
    return {
      EnsaioID: r.EnsaioID, BrincanteID: r.BrincanteID, Presente: r.Presente,
      Nota: r.Nota, Observacao: r.Observacao, AvaliadoPor: r.AvaliadoPor, DataRegistro: r.DataRegistro,
    };
  });
}

async function salvarAvaliacoes(ensaioId, avaliacoes, usuario) {
  const db = getDb();
  // Remove avaliações existentes desse ensaio e insere as novas de forma atômica
  const existing = await db.collection('avaliacoes').where('EnsaioID', '==', ensaioId).get();
  const batch = db.batch();
  existing.docs.forEach((d) => batch.delete(d.ref));

  const now = nowIso();
  const avaliadoPor = usuario ? `${usuario.nome} (${usuario.id})` : 'sistema';
  avaliacoes.forEach((av) => {
    const ref = db.collection('avaliacoes').doc();
    batch.set(ref, {
      EnsaioID: ensaioId,
      BrincanteID: av.brincanteId,
      Presente: av.presente ? 'sim' : 'nao',
      Nota: av.nota || 0,
      Observacao: av.observacao || '',
      AvaliadoPor: avaliadoPor,
      DataRegistro: now,
    });
  });
  await batch.commit();

  if (usuario) {
    const presentes = avaliacoes.filter((a) => a.presente).length;
    await registrarLog_(usuario.id, usuario.nome, 'AVALIAÇÃO', `Ensaio ${ensaioId}: ${avaliacoes.length} brincantes avaliados, ${presentes} presentes`);
  }
  return { success: true, count: avaliacoes.length };
}

// ============================================================
// DASHBOARD / MÉTRICAS
// ============================================================
async function getDashboard() {
  const [brincantes, ensaios, avaliacoes] = await Promise.all([getBrincantes(), getEnsaios(), getAvaliacoes()]);

  const totalBrincantes = brincantes.filter((b) => b.Tipo !== 'coordenacao').length;
  const totalCoord = brincantes.filter((b) => b.Tipo === 'coordenacao').length;
  const totalEnsaios = ensaios.length;
  const optBonificacao = brincantes.filter((b) => b.OptBonificacao === 'sim').length;
  const ativados = brincantes.filter((b) => b.StatusAtivacao === 'ativado').length;

  let totalPresencas = 0, totalRegistros = 0;
  avaliacoes.forEach((a) => { if (a.Presente === 'sim') totalPresencas++; totalRegistros++; });
  const mediaPresenca = totalRegistros > 0 ? Math.round((totalPresencas / totalRegistros) * 100) : 0;

  let somaNotas = 0, contNotas = 0;
  avaliacoes.forEach((a) => {
    if (a.Presente === 'sim' && a.Nota > 0) { somaNotas += Number(a.Nota); contNotas++; }
  });
  const mediaNotas = contNotas > 0 ? (somaNotas / contNotas).toFixed(1) : '0.0';

  return { totalBrincantes, totalCoord, totalEnsaios, optBonificacao, ativados, mediaPresenca, mediaNotas, totalPresencas, totalRegistros };
}

// ============================================================
// PERFIL DO BRINCANTE
// ============================================================
async function getPerfilBrincante(brincanteId) {
  const [brincantes, ensaios, config] = await Promise.all([getBrincantes(), getEnsaios(), getConfigMap_()]);
  const brincante = brincantes.find((b) => b.ID === brincanteId);
  if (!brincante) return null;

  const avaliacoes = await getAvaliacoes({ brincanteId });

  const totalEnsaios = ensaios.length;
  const presencas = avaliacoes.filter((a) => a.Presente === 'sim').length;
  const percPresenca = totalEnsaios > 0 ? Math.round((presencas / totalEnsaios) * 100) : 0;

  const notas = avaliacoes.filter((a) => a.Presente === 'sim' && a.Nota > 0).map((a) => Number(a.Nota));
  const mediaNotas = notas.length > 0 ? (notas.reduce((a, b) => a + b, 0) / notas.length).toFixed(1) : '0.0';
  const notasAcimaDe4 = notas.filter((n) => n >= 4).length;
  const percNotasBoas = notas.length > 0 ? Math.round((notasAcimaDe4 / notas.length) * 100) : 0;

  const valorEnsaio = parseFloat(config.valorEnsaio || 0.5);
  const valorApresentacao = parseFloat(config.valorApresentacao || 1.0);
  const valorFestival = parseFloat(config.valorFestival || 5.0);

  let bonificacao = 0;
  if (brincante.OptBonificacao === 'sim' && brincante.StatusAtivacao === 'ativado') {
    avaliacoes.forEach((av) => {
      if (av.Presente === 'sim') {
        const ensaio = ensaios.find((e) => e.ID === av.EnsaioID);
        if (ensaio) {
          const tipo = ensaio.Tipo;
          if (tipo === 'festival') bonificacao += valorFestival;
          else if (tipo === 'apresentacao') bonificacao += valorApresentacao;
          else if (tipo !== 'igreja') bonificacao += valorEnsaio;
          // 'igreja' não gera bonificação
        }
      }
    });
  }

  const historico = avaliacoes.map((av) => {
    const ensaio = ensaios.find((e) => e.ID === av.EnsaioID);
    return {
      data: ensaio ? ensaio.Data : '',
      tipo: ensaio ? ensaio.Tipo : '',
      presente: av.Presente === 'sim',
      nota: Number(av.Nota),
      observacao: av.Observacao,
      avaliadoPor: av.AvaliadoPor,
    };
  }).sort((a, b) => new Date(b.data) - new Date(a.data));

  return {
    ...brincante,
    totalEnsaios, presencas, percPresenca,
    mediaNotas, percNotasBoas, notas,
    bonificacao: bonificacao.toFixed(2),
    historico,
  };
}

// ============================================================
// RANKING
// ============================================================
async function getRanking() {
  const [brincantesAll, avaliacoes, ensaios] = await Promise.all([getBrincantes(), getAvaliacoes(), getEnsaios()]);
  const brincantes = brincantesAll.filter((b) => b.Tipo !== 'coordenacao');
  const totalEnsaios = ensaios.length;

  return brincantes.map((b) => {
    const avs = avaliacoes.filter((a) => a.BrincanteID === b.ID);
    const presencas = avs.filter((a) => a.Presente === 'sim').length;
    const notas = avs.filter((a) => a.Presente === 'sim' && a.Nota > 0).map((a) => Number(a.Nota));
    const media = notas.length > 0 ? (notas.reduce((a, c) => a + c, 0) / notas.length) : 0;
    const perc = totalEnsaios > 0 ? Math.round((presencas / totalEnsaios) * 100) : 0;
    return {
      id: b.ID,
      nome: b.Apelido || b.Nome,
      fila: b.Fila,
      tipo: b.Tipo,
      presencas,
      percPresenca: perc,
      mediaNotas: media.toFixed(1),
      totalAvaliacoes: notas.length,
    };
  }).sort((a, b) => parseFloat(b.mediaNotas) - parseFloat(a.mediaNotas) || b.percPresenca - a.percPresenca);
}

// ============================================================
// BONIFICAÇÃO - SIMULAÇÃO
// ============================================================
async function getSimulacaoBonificacao() {
  const [brincantesAll, ensaios, avaliacoes, config] = await Promise.all([
    getBrincantes(), getEnsaios(), getAvaliacoes(), getConfigMap_(),
  ]);
  const brincantes = brincantesAll.filter((b) => b.Tipo !== 'coordenacao' && b.OptBonificacao === 'sim');

  const valorEnsaio = parseFloat(config.valorEnsaio || 0.5);
  const valorApresentacao = parseFloat(config.valorApresentacao || 1.0);
  const valorFestival = parseFloat(config.valorFestival || 5.0);

  let totalGeral = 0;
  const lista = brincantes.map((b) => {
    const avs = avaliacoes.filter((a) => a.BrincanteID === b.ID);
    let valor = 0, ensaiosPresente = 0, apresentacoesPresente = 0, festivalPresente = false;
    avs.forEach((av) => {
      if (av.Presente === 'sim') {
        const ensaio = ensaios.find((e) => e.ID === av.EnsaioID);
        if (ensaio) {
          if (ensaio.Tipo === 'festival') { valor += valorFestival; festivalPresente = true; }
          else if (ensaio.Tipo === 'apresentacao') { valor += valorApresentacao; apresentacoesPresente++; }
          else if (ensaio.Tipo !== 'igreja') { valor += valorEnsaio; ensaiosPresente++; }
        }
      }
    });
    const elegivel = b.StatusAtivacao === 'ativado';
    if (elegivel) totalGeral += valor;
    return {
      nome: b.Apelido || b.Nome,
      fila: b.Fila,
      statusAtivacao: b.StatusAtivacao,
      elegivel,
      ensaiosPresente,
      apresentacoesPresente,
      festivalPresente,
      valorAcumulado: valor.toFixed(2),
    };
  });

  return { lista, totalGeral: totalGeral.toFixed(2), config: { valorEnsaio, valorApresentacao, valorFestival } };
}

// ============================================================
// CONFIG
// ============================================================
async function getConfig() {
  return getConfigMap_();
}

async function getStatusAdesao() {
  const config = await getConfigMap_();
  const fimAdesao = config.fimAdesao || '2026-04-30';
  const hoje = today();
  return { dentroDoPeríodo: hoje <= fimAdesao, fimAdesao };
}

async function updateConfig(chave, valor) {
  await getDb().collection('config').doc('app').set({ [chave]: valor }, { merge: true });
  return { success: true };
}

// ============================================================
// EXPORT - mapa de funções expostas à API (whitelist)
// ============================================================
module.exports = {
  login,
  getLogs,
  getBrincantes, addBrincante, updateBrincante, removeBrincante,
  getEnsaios, addEnsaio, deleteEnsaio,
  getAvaliacoes, salvarAvaliacoes,
  getDashboard, getPerfilBrincante, getRanking, getSimulacaoBonificacao,
  getConfig, getStatusAdesao, updateConfig,
  // helpers exportados para o seed
  _getConfigMap: getConfigMap_,
  _DEFAULT_CONFIG: DEFAULT_CONFIG,
};
