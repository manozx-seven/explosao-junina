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
const {
  criarSessao, encerrarSessao, rebaixarParaBrincante, encerrarSessoesDoBrincante,
} = require('./sessoes');

const DEFAULT_CONFIG = {
  valorEnsaio: '0.50',
  valorApresentacao: '1.00',
  valorFestival: '5.00',
  // Teto da bonificação por brincante na temporada (Cláusula Sexta, III, "e").
  // O programa é retorno simbólico: o teto garante que ele nunca estoure o
  // orçamento, por maior que a temporada seja. 0 (ou vazio) = sem teto.
  tetoBonificacao: '80.00',
  mesesAtivacao: '3',
  frequenciaMinima: '75',
  frequenciaItem: '85',
  notaMinima: '4',
  percentualNotaMinima: '75',
  temporada: '2027',
  inicioTemporada: '2027-02-01',
  inicioContagem: '2027-05-01', // piso da contagem (fev–abr = só ativação; começa de fato ao fim da ativação de cada um)
  fimContagem: '2027-07-31',
  fimAdesao: '2027-04-30',
  // Pagamento da bonificação: pelo contrato só é repassada APÓS o Festival.
  // Campos informativos para o brincante saber quando/como vai receber.
  dataPagamentoBonif: '',   // data prevista da 1ª (ou única) entrega
  dataPagamentoBonif2: '',  // 2ª metade/parcela (modelo 13º, opcional)
  obsPagamentoBonif: '',    // texto livre: como será pago (ex.: metade até X, metade até Y)
  // Toggle manual: a coordenação libera quando o valor já está fechado (fim da
  // contagem), permitindo então que o brincante escolha resgatar ou doar.
  escolhaDestinoLiberada: 'nao',
  // Missão de captação: quantos sócios torcedores cada brincante se compromete
  // a trazer na temporada (Plano de Implementação §6 e §15: "2 por brincante").
  metaSociosPorBrincante: '2',
};

// ---------- helpers ----------
function today() { return new Date().toISOString().slice(0, 10); }
function nowIso() { return new Date().toISOString(); }
function normalizaCpf(cpf) { return String(cpf || '').replace(/\D/g, '').trim().padStart(11, '0'); }

// Tipos de brincante (podem acumular coordenação):
//   brincante | item | coordenacao | brincante_coord | item_coord
function ehCoordenacao_(t) { return t === 'coordenacao' || t === 'brincante_coord' || t === 'item_coord'; }
function papelDanca_(t) { return (t === 'item' || t === 'item_coord') ? 'item' : ((t === 'brincante' || t === 'brincante_coord') ? 'brincante' : ''); }
function ehDancarino_(t) { return papelDanca_(t) !== ''; } // participa de métricas/bonificação
function ehItem_(t) { return papelDanca_(t) === 'item'; }

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
//
// O login devolve um TOKEN de sessão. A partir daqui, toda chamada da API
// precisa apresentá-lo, e quem o usuário é passa a vir do servidor — o
// objeto `usuario` não é mais aceito como argumento do navegador.
// ============================================================
async function login(id, cpf) {
  const cpfLimpo = normalizaCpf(cpf);
  const idLimpo = String(id).trim().toUpperCase();

  const doc = await getDb().collection('brincantes').doc(idLimpo).get();
  if (doc.exists) {
    const b = doc.data();
    if (normalizaCpf(b.CPF) === cpfLimpo) {
      // Coordenação entra como admin; quem só dança entra como brincante.
      // Papel duplo nasce admin e pode rebaixar em `entrarComoBrincante`.
      const tipoSessao = ehCoordenacao_(b.Tipo) ? 'admin' : 'brincante';
      const sessao = await criarSessao(tipoSessao, { id: b.ID || idLimpo, nome: b.Nome });
      await registrarLog_(idLimpo, b.Nome, 'LOGIN', 'Acesso ao sistema');
      return {
        success: true,
        token: sessao.token,
        nome: b.Nome,
        id: b.ID,
        apelido: b.Apelido,
        fila: b.Fila,
        tipo: b.Tipo,
        papel: papelDanca_(b.Tipo),        // '' | 'brincante' | 'item'
        podeCoord: ehCoordenacao_(b.Tipo), // pode entrar como coordenação
      };
    }
  }
  return { success: false, message: 'ID ou CPF inválido' };
}

async function logout(sessao) {
  if (sessao && sessao.token) await encerrarSessao(sessao.token);
  return { success: true };
}

/**
 * Quem tem papel duplo escolhe, no login, entrar como coordenação ou como
 * item/brincante. Escolhendo o papel de dança, a sessão é REBAIXADA de fato:
 * o token perde o poder de administrar enquanto durar. Só rebaixa.
 */
async function entrarComoBrincante(sessao) {
  if (!sessao || !sessao.token) return { success: false };
  await rebaixarParaBrincante(sessao.token);
  return { success: true };
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
    DataNascimento: b.DataNascimento || '',
    AnexoI: b.AnexoI || '',   // 'sim' quando o Anexo I (autorização do responsável) foi assinado
    AnexoII: b.AnexoII || '',  // 'sim' quando o Anexo II (autorização de viagem) foi assinado
    DataAdesao: b.DataAdesao || '',
    DataAssinatura: b.DataAssinatura || '',
    OptBonificacao: b.OptBonificacao || 'nao',
    // Destino do valor acumulado no fim da temporada: 'resgatar' (o brincante
    // recebe) ou 'doar' (deixa com a quadrilha). O próprio brincante pode
    // escolher no seu perfil; a coordenação também edita no cadastro.
    DestinoBonificacao: b.DestinoBonificacao || 'resgatar',
    StatusAtivacao: b.StatusAtivacao || 'auto',
    QualificacaoExtra: b.QualificacaoExtra || '',
    StatusMembro: b.StatusMembro || 'ativo',
    MotivoDesligamento: b.MotivoDesligamento || '',
    DataDesligamento: b.DataDesligamento || '',
  };
}

async function getBrincantes() {
  const snap = await getDb().collection('brincantes').get();
  return snap.docs.map((d) => normalizaBrincante_(d.data()));
}

async function addBrincante(dados, usuario) {
  const config = await getConfigMap_();
  const fimAdesao = config.fimAdesao || '2026-04-30';
  // A adesão vale pela DATA de adesão (permite cadastrar em julho quem aderiu
  // em fevereiro). Data de adesão depois do prazo do contrato não vale como opt-in.
  if (dados.optBonificacao === 'sim') {
    const da = dados.dataAdesao || today();
    if (da > fimAdesao) dados.optBonificacao = 'nao';
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
    DataNascimento: dados.dataNascimento || '',
    AnexoI: dados.anexoI ? 'sim' : '',
    AnexoII: dados.anexoII ? 'sim' : '',
    DataAdesao: dados.dataAdesao || today(),
    DataAssinatura: dados.dataAssinatura || today(),
    OptBonificacao: dados.optBonificacao || 'nao',
    DestinoBonificacao: dados.destinoBonificacao === 'doar' ? 'doar' : 'resgatar',
    StatusAtivacao: 'auto',
    QualificacaoExtra: '',
    StatusMembro: 'ativo',
    MotivoDesligamento: '',
    DataDesligamento: '',
  };
  await getDb().collection('brincantes').doc(id).set(brincante);

  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'CADASTRO', `Brincante cadastrado: ${dados.nome} (${id})`);
  }
  return { success: true, id, message: `Brincante cadastrado! ID: ${id}` };
}

// Cadastro em lote: cria vários brincantes de uma vez (import de planilha/CSV).
// Retorna quantos foram criados e a lista de erros por linha.
async function addBrincantesLote(lista, usuario) {
  const criados = [];
  const erros = [];
  for (const dados of (Array.isArray(lista) ? lista : [])) {
    const nome = dados && dados.nome ? String(dados.nome).trim() : '';
    if (!nome) { erros.push({ nome: '(sem nome)', erro: 'Nome vazio' }); continue; }
    try {
      const r = await addBrincante(dados, null); // sem log por linha
      criados.push({ id: r.id, nome });
    } catch (e) {
      erros.push({ nome, erro: e.message || 'Erro' });
    }
  }
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'CADASTRO_LOTE', `Cadastro em lote: ${criados.length} criados, ${erros.length} com erro`);
  }
  return { success: true, criados, erros, total: criados.length };
}

async function updateBrincante(id, dados, usuario) {
  const ref = getDb().collection('brincantes').doc(String(id).trim());
  const doc = await ref.get();
  if (!doc.exists) return { success: false, message: 'Brincante não encontrado' };

  const campoMap = {
    nome: 'Nome', apelido: 'Apelido', cpf: 'CPF', fila: 'Fila', posicao: 'Posicao',
    tipo: 'Tipo', optBonificacao: 'OptBonificacao', destinoBonificacao: 'DestinoBonificacao', statusAtivacao: 'StatusAtivacao',
    qualificacaoExtra: 'QualificacaoExtra',
    dataNascimento: 'DataNascimento', anexoI: 'AnexoI', anexoII: 'AnexoII',
    dataAdesao: 'DataAdesao', dataAssinatura: 'DataAssinatura',
    statusMembro: 'StatusMembro', motivoDesligamento: 'MotivoDesligamento', dataDesligamento: 'DataDesligamento',
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

  // O CPF é a senha: trocá-lo precisa derrubar quem já estava logado com a antiga.
  if (changes.includes('cpf')) await encerrarSessoesDoBrincante(String(id).trim());

  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'EDIÇÃO', `Brincante ${id} editado. Campos: ${changes.join(', ')}`);
  }
  return { success: true };
}

// Auto-serviço: o próprio brincante define, no seu perfil, se ao fim da temporada
// vai RESGATAR o valor acumulado ou DOAR à quadrilha. Só toca esse campo.
//
// Escopo `autenticado`: quem NÃO é admin só altera o próprio destino — o ID vem
// da sessão, não do argumento. Sem isso, o brincante A trocaria a escolha do B
// mudando um parâmetro na requisição.
async function setDestinoBonificacao(id, destino, usuario) {
  const config = await getConfigMap_();
  if (config.escolhaDestinoLiberada !== 'sim') {
    return { success: false, message: 'A escolha ainda não foi liberada pela coordenação.' };
  }
  const dest = destino === 'doar' ? 'doar' : 'resgatar';
  const alvo = (usuario && usuario.tipo !== 'admin') ? usuario.id : id;
  const ref = getDb().collection('brincantes').doc(String(alvo).trim());
  const doc = await ref.get();
  if (!doc.exists) return { success: false, message: 'Brincante não encontrado' };
  await ref.update({ DestinoBonificacao: dest });
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'DESTINO_BONIF', `Brincante ${alvo}: destino da bonificação = ${dest}`);
  }
  return { success: true, destino: dest };
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
    return {
      ID: r.ID, Data: r.Data, Tipo: r.Tipo, Descricao: r.Descricao, CriadoPor: r.CriadoPor,
      // Campos de agenda (eventos antigos não têm; Status ausente = conta normalmente)
      HoraInicio: r.HoraInicio || '', HoraFim: r.HoraFim || '',
      Status: r.Status || 'planejado',
      HoraInicioReal: r.HoraInicioReal || '', HoraFimReal: r.HoraFimReal || '',
      ObsEvento: r.ObsEvento || '',
      // Valor de bonificação específico deste evento (''=usa o padrão do tipo)
      ValorBonificacao: (r.ValorBonificacao === undefined || r.ValorBonificacao === null) ? '' : String(r.ValorBonificacao),
      // Participantes designados (só atividades do compromisso). IDs separados por
      // vírgula; vazio = todos os brincantes (comportamento padrão).
      Participantes: r.Participantes || '',
    };
  });
}

async function addEnsaio(dados, usuario) {
  const dataFormatada = String(dados.data).replace(/-/g, '');
  const id = 'ENS' + dataFormatada + '_' + String(Date.now()).slice(-4);
  const criadoPor = usuario ? `${usuario.nome} (${usuario.id})` : '';
  await getDb().collection('ensaios').doc(id).set({
    ID: id, Data: dados.data, Tipo: dados.tipo, Descricao: dados.descricao || '', CriadoPor: criadoPor,
    HoraInicio: dados.horaInicio || '', HoraFim: dados.horaFim || '',
    Status: 'planejado', HoraInicioReal: '', HoraFimReal: '', ObsEvento: '',
    ValorBonificacao: (dados.valorBonificacao === undefined || dados.valorBonificacao === '') ? '' : String(dados.valorBonificacao),
    Participantes: dados.participantes || '',
  });
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'EVENTO_CRIADO', `Evento ${id}: ${dados.tipo} em ${dados.data}`);
  }
  return { success: true, id };
}

// Edita um evento: data/tipo/descrição/horários planejados, status (cancelar/reativar)
// e horários reais + observação (ajuste após acontecer).
async function updateEvento(id, dados, usuario) {
  const ref = getDb().collection('ensaios').doc(String(id).trim());
  const doc = await ref.get();
  if (!doc.exists) return { success: false };

  const campoMap = {
    data: 'Data', tipo: 'Tipo', descricao: 'Descricao',
    horaInicio: 'HoraInicio', horaFim: 'HoraFim', status: 'Status',
    horaInicioReal: 'HoraInicioReal', horaFimReal: 'HoraFimReal', obsEvento: 'ObsEvento',
    valorBonificacao: 'ValorBonificacao', participantes: 'Participantes',
  };
  const update = {};
  const changes = [];
  for (const [k, field] of Object.entries(campoMap)) {
    if (dados[k] !== undefined) { update[field] = dados[k]; changes.push(k); }
  }
  if (changes.length) await ref.update(update);

  if (usuario) {
    const acao = dados.status === 'cancelado' ? 'EVENTO_CANCELADO' : 'EVENTO_EDITADO';
    await registrarLog_(usuario.id, usuario.nome, acao, `Evento ${id} atualizado. Campos: ${changes.join(', ')}`);
  }
  return { success: true };
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
      Nota: r.Nota, Observacao: r.Observacao, Justificada: r.Justificada === true,
      AvaliadoPor: r.AvaliadoPor, DataRegistro: r.DataRegistro,
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

// Salva/atualiza a avaliação de UM brincante num evento (autosave da chamada).
// patch aceita { presente: 'sim'|'nao'|null, justificativa, justificada, nota, observacao }.
// presente === null remove o registro (volta a "não marcado").
async function upsertAvaliacao(eventoId, brincanteId, patch, usuario) {
  const db = getDb();
  const snap = await db.collection('avaliacoes')
    .where('EnsaioID', '==', eventoId).where('BrincanteID', '==', brincanteId).get();
  const avaliadoPor = usuario ? `${usuario.nome} (${usuario.id})` : 'sistema';

  // "não marcado": apaga eventuais registros existentes desse brincante
  if (patch.presente === null) {
    if (!snap.empty) {
      const batch = db.batch();
      snap.docs.forEach((d) => batch.delete(d.ref));
      await batch.commit();
    }
    return { success: true, marcado: false };
  }

  const ref = snap.empty ? db.collection('avaliacoes').doc() : snap.docs[0].ref;
  const atual = snap.empty ? {} : snap.docs[0].data();
  const presente = patch.presente !== undefined ? patch.presente : (atual.Presente || 'nao');
  const doc = {
    EnsaioID: eventoId,
    BrincanteID: brincanteId,
    Presente: presente,
    Nota: patch.nota !== undefined ? (patch.nota || 0) : (atual.Nota || 0),
    Observacao: patch.observacao !== undefined ? patch.observacao
      : (patch.justificativa !== undefined ? patch.justificativa : (atual.Observacao || '')),
    // Falta justificada (avisou com 24h). Só faz sentido quando é falta.
    Justificada: presente === 'nao'
      ? (patch.justificada !== undefined ? !!patch.justificada : (atual.Justificada === true))
      : false,
    AvaliadoPor: avaliadoPor,
    DataRegistro: nowIso(),
  };
  await ref.set(doc);
  return { success: true, marcado: true };
}

// ============================================================
// DASHBOARD / MÉTRICAS
// ============================================================
// Descarta eventos cancelados e as avaliações ligadas a eles.
// Usado em toda métrica (frequência, ranking, bonificação): evento que
// não aconteceu não conta para nada.
function filtrarCancelados_(ensaios, avaliacoes) {
  const validos = ensaios.filter((e) => e.Status !== 'cancelado');
  const idsValidos = new Set(validos.map((e) => e.ID));
  return {
    ensaios: validos,
    avaliacoes: avaliacoes ? avaliacoes.filter((a) => idsValidos.has(a.EnsaioID)) : avaliacoes,
  };
}

// Atividades do compromisso (Cláusula Segunda, l): não geram bonificação e
// NÃO entram na frequência/nota de ensaios (mas têm presença registrada).
const TIPOS_ATIVIDADE = ['arrecadacao', 'bracal', 'comunitario', 'outra'];
function ehAtividade_(tipo) { return TIPOS_ATIVIDADE.indexOf(tipo) >= 0; }

// Remove cancelados E atividades — usado nas métricas de ensaio (frequência, nota).
function eventosMetrica_(ensaios, avaliacoes) {
  const validos = ensaios.filter((e) => e.Status !== 'cancelado' && !ehAtividade_(e.Tipo));
  const ids = new Set(validos.map((e) => e.ID));
  return {
    ensaios: validos,
    avaliacoes: avaliacoes ? avaliacoes.filter((a) => ids.has(a.EnsaioID)) : avaliacoes,
  };
}

// Valor de bonificação de um evento: usa o override do evento (se preenchido),
// senão o valor padrão do tipo. Igreja e atividades não geram bonificação.
function valorBonifEvento_(ensaio, valorEnsaio, valorApresentacao, valorFestival) {
  const ov = ensaio.ValorBonificacao;
  if (ov !== undefined && ov !== null && String(ov) !== '') {
    const n = parseFloat(ov);
    if (!isNaN(n)) return n;
  }
  if (ensaio.Tipo === 'festival') return valorFestival;
  if (ensaio.Tipo === 'apresentacao') return valorApresentacao;
  if (ensaio.Tipo === 'regular' || ensaio.Tipo === 'ensaiao') return valorEnsaio;
  return 0; // igreja + atividades (arrecadação, braçal, comunitário, outra)
}
// Evento dentro do período de contagem da bonificação (fev–abr = só ativação).
function noPeriodoBonif_(ensaio, inicioContagem, fimContagem) {
  return ensaio.Data >= inicioContagem && ensaio.Data <= fimContagem;
}

// Teto por brincante na temporada (Cláusula Sexta, III, "e"): ao chegar nele, o
// brincante para de acumular e mantém o que já tem. Config `tetoBonificacao`;
// 0, vazio ou lixo = sem teto, porque um erro de digitação na tela de
// configurações não pode zerar a bonificação de todo mundo em silêncio.
function tetoConfig_(config) {
  const n = parseFloat(config && config.tetoBonificacao);
  return (!isNaN(n) && n > 0) ? n : 0;
}
// Aplicado ANTES da sanção: o teto limita o que se acumula; a sanção desconta
// sobre o acumulado (Cláusulas Sétima e Oitava). Inverter a ordem faria a
// advertência formal (−50%) render mais a quem passou do teto do que a quem
// ficou nele.
function aplicarTeto_(valor, teto) {
  return (teto > 0 && valor > teto) ? teto : valor;
}

// ============================================================
// ADVERTÊNCIAS / SANÇÕES (Cláusula Sétima)
// ============================================================
// Penalidade sobre a bonificação por nível: verbal só registra; formal −50%;
// desligamento e gravidade extrema −100%. Vale o pior nível registrado.
const NIVEL_PENALIDADE = { verbal: 0, formal: 50, desligamento: 100, extrema: 100 };
function penalidadeDasAdvs_(advs) {
  let pct = 0;
  (advs || []).forEach((a) => { const p = NIVEL_PENALIDADE[a.Nivel] || 0; if (p > pct) pct = p; });
  return pct;
}
async function getAdvertencias(brincanteId) {
  let q = getDb().collection('advertencias');
  if (brincanteId) q = q.where('BrincanteID', '==', brincanteId);
  const snap = await q.get();
  return snap.docs.map((d) => {
    const r = d.data();
    return { id: d.id, BrincanteID: r.BrincanteID, Nivel: r.Nivel, Motivo: r.Motivo, Data: r.Data, RegistradoPor: r.RegistradoPor, DataRegistro: r.DataRegistro };
  }).sort((a, b) => (b.Data || '').localeCompare(a.Data || ''));
}
async function addAdvertencia(dados, usuario) {
  const doc = {
    BrincanteID: dados.brincanteId,
    Nivel: dados.nivel,
    Motivo: dados.motivo || '',
    Data: dados.data || today(),
    RegistradoPor: usuario ? `${usuario.nome} (${usuario.id})` : 'sistema',
    DataRegistro: nowIso(),
  };
  const ref = await getDb().collection('advertencias').add(doc);
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'ADVERTENCIA', `Advertência ${dados.nivel} para ${dados.brincanteId}: ${dados.motivo || ''}`);
  }
  return { success: true, id: ref.id };
}
async function removeAdvertencia(id, usuario) {
  const ref = getDb().collection('advertencias').doc(id);
  const doc = await ref.get();
  if (!doc.exists) return { success: false };
  await ref.delete();
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'ADVERTENCIA_REMOVIDA', `Advertência ${id} removida`);
  }
  return { success: true };
}

// Desligamento com perda integral (Cláusula Oitava): transferência p/ concorrente,
// desligamento nos 15 dias pré-Festival, ou desligamento por sanção da quadrilha.
const MOTIVOS_PERDA_INTEGRAL = ['concorrente', 'pre_festival', 'quadrilha'];
function penalidadeDesligamento_(brincante) {
  if (brincante.StatusMembro === 'desligado' && MOTIVOS_PERDA_INTEGRAL.indexOf(brincante.MotivoDesligamento) >= 0) return 100;
  return 0;
}
// Penalidade efetiva = pior entre advertências e desligamento.
function penalidadeTotal_(brincante, advs) {
  return Math.max(penalidadeDasAdvs_(advs), penalidadeDesligamento_(brincante));
}

// ============================================================
// ATIVAÇÃO (Cláusula Sexta, II — proporcional à data de adesão)
// ============================================================
function addMeses_(dateStr, n) {
  if (!dateStr) return '';
  const d = new Date(dateStr + 'T00:00:00');
  d.setMonth(d.getMonth() + n);
  return d.toISOString().slice(0, 10);
}
function addDias_(dateStr, n) {
  if (!dateStr) return '';
  const d = new Date(dateStr + 'T00:00:00');
  d.setDate(d.getDate() + n);
  return d.toISOString().slice(0, 10);
}
// Data em que o brincante COMEÇA a acumular bonificação: o maior entre o piso da
// contagem (inicioContagem) e o dia seguinte ao fim da ativação individual.
function inicioBonif_(ativacaoFim, inicioContagem) {
  const aposAtiv = ativacaoFim ? addDias_(ativacaoFim, 1) : '';
  if (!aposAtiv) return inicioContagem;
  return aposAtiv > inicioContagem ? aposAtiv : inicioContagem;
}
// Calcula o status de ativação de um brincante. StatusAtivacao manual
// ('ativado'/'nao_elegivel') sobrepõe o cálculo; 'auto' (ou vazio/legado) calcula.
function avaliarAtivacao(brincante, ensaiosMetric, avsBrincante, config) {
  const meses = parseInt(config.mesesAtivacao || 3, 10);
  const freqMin = ehItem_(brincante.Tipo)
    ? parseInt(config.frequenciaItem || 85, 10)
    : parseInt(config.frequenciaMinima || 75, 10);
  const notaMin = parseFloat(config.notaMinima || 4);
  const percNota = parseInt(config.percentualNotaMinima || 75, 10);
  const fimContagem = config.fimContagem || '2027-07-31';
  const inicioContagem = config.inicioContagem || '2027-05-01';
  const hoje = today();
  const adesao = brincante.DataAdesao || '';

  const manual = brincante.StatusAtivacao;
  if (manual === 'ativado') {
    const af = addMeses_(adesao, meses);
    return { status: 'ativado', ativado: true, override: true, adesao, ativacaoFim: af, bonificacaoInicio: inicioBonif_(af, inicioContagem), fimContagem };
  }
  if (manual === 'nao_elegivel') return { status: 'nao_elegivel', ativado: false, override: true, adesao, ativacaoFim: '', bonificacaoInicio: '', fimContagem };

  if (brincante.OptBonificacao !== 'sim') return { status: 'sem_bonificacao', ativado: false, adesao, ativacaoFim: '', bonificacaoInicio: '', fimContagem };
  if (!adesao) return { status: 'sem_adesao', ativado: false, adesao: '', ativacaoFim: '', bonificacaoInicio: '', fimContagem };

  const ativacaoFim = addMeses_(adesao, meses);
  const bonificacaoInicio = inicioBonif_(ativacaoFim, inicioContagem);
  if (ativacaoFim >= fimContagem) return { status: 'nao_elegivel', ativado: false, adesao, ativacaoFim, bonificacaoInicio: '', fimContagem };

  const janela = ensaiosMetric.filter((e) => e.Data >= adesao && e.Data <= ativacaoFim);
  const ids = new Set(janela.map((e) => e.ID));
  const avs = avsBrincante.filter((a) => ids.has(a.EnsaioID));
  const totalJanela = janela.length;
  const presencas = avs.filter((a) => a.Presente === 'sim').length;
  const freq = totalJanela > 0 ? Math.round((presencas / totalJanela) * 100) : 0;
  const notas = avs.filter((a) => a.Presente === 'sim' && a.Nota > 0).map((a) => Number(a.Nota));
  const notasBoas = notas.filter((n) => n >= notaMin).length;
  const notaPct = notas.length > 0 ? Math.round((notasBoas / notas.length) * 100) : 0;
  const freqOk = freq >= freqMin;
  const notaOk = notaPct >= percNota;

  if (hoje <= ativacaoFim) {
    return { status: 'em_ativacao', ativado: false, adesao, ativacaoFim, bonificacaoInicio, fimContagem, freq, freqOk, notaPct, notaOk, totalJanela };
  }
  const ativado = freqOk && notaOk;
  return { status: ativado ? 'ativado' : 'nao_ativado', ativado, adesao, ativacaoFim, bonificacaoInicio, fimContagem, freq, freqOk, notaPct, notaOk, totalJanela };
}

async function getDashboard() {
  const [brincantesRaw, ensaiosRaw, avaliacoesRaw] = await Promise.all([getBrincantes(), getEnsaios(), getAvaliacoes()]);
  const brincantes = brincantesRaw;
  const { ensaios } = filtrarCancelados_(ensaiosRaw, avaliacoesRaw); // contagem de eventos (inclui atividades)
  const { avaliacoes } = eventosMetrica_(ensaiosRaw, avaliacoesRaw); // presença/nota só de ensaios

  const totalBrincantes = brincantes.filter((b) => ehDancarino_(b.Tipo)).length;
  const totalCoord = brincantes.filter((b) => ehCoordenacao_(b.Tipo)).length;
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
//
// Escopo `autenticado`: a coordenação vê o perfil de qualquer um; quem NÃO é
// admin vê apenas o próprio, e o ID vem DA SESSÃO. Sem essa trava, bastaria
// trocar o parâmetro para ler o desempenho, a bonificação e as advertências
// de outra pessoa.
// ============================================================
async function getPerfilBrincante(brincanteId, usuario) {
  const alvo = (usuario && usuario.tipo !== 'admin') ? usuario.id : brincanteId;
  const [brincantes, ensaiosRaw, config] = await Promise.all([getBrincantes(), getEnsaios(), getConfigMap_()]);
  const brincante = brincantes.find((b) => b.ID === alvo);
  if (!brincante) return null;
  brincanteId = alvo;

  const avaliacoesRaw = await getAvaliacoes({ brincanteId });
  const advs = await getAdvertencias(brincanteId);
  // Missão de captação: fica no perfil junto do resto, mas NÃO entra em
  // nenhuma conta de frequência, nota ou bonificação daqui para baixo.
  const minhasIndicacoes = await getIndicacoes({ brincanteId });
  // Não cancelados (inclui atividades) -> histórico e bonificação.
  const { ensaios: ensaiosNC, avaliacoes: avaliacoesNC } = filtrarCancelados_(ensaiosRaw, avaliacoesRaw);
  // Só ensaios/apresentações -> frequência e nota.
  const metric = eventosMetrica_(ensaiosRaw, avaliacoesRaw);

  const totalEnsaios = metric.ensaios.length;
  const presencas = metric.avaliacoes.filter((a) => a.Presente === 'sim').length;
  const percPresenca = totalEnsaios > 0 ? Math.round((presencas / totalEnsaios) * 100) : 0;

  const notas = metric.avaliacoes.filter((a) => a.Presente === 'sim' && a.Nota > 0).map((a) => Number(a.Nota));
  const mediaNotas = notas.length > 0 ? (notas.reduce((a, b) => a + b, 0) / notas.length).toFixed(1) : '0.0';
  const notasAcimaDe4 = notas.filter((n) => n >= 4).length;
  const percNotasBoas = notas.length > 0 ? Math.round((notasAcimaDe4 / notas.length) * 100) : 0;

  const valorEnsaio = parseFloat(config.valorEnsaio || 0.5);
  const valorApresentacao = parseFloat(config.valorApresentacao || 1.0);
  const valorFestival = parseFloat(config.valorFestival || 5.0);
  const inicioContagem = config.inicioContagem || '2026-05-01';
  const fimContagem = config.fimContagem || '2026-07-31';

  // Ativação (proporcional/automática) usa as métricas de ensaio.
  const ativacao = avaliarAtivacao(brincante, metric.ensaios, metric.avaliacoes, config);
  // Contagem começa ao fim da ativação individual (proporcional à adesão), respeitando o piso.
  const inicioBonifInd = ativacao.bonificacaoInicio || inicioContagem;
  let bonificacao = 0;
  if (brincante.OptBonificacao === 'sim' && ativacao.ativado) {
    avaliacoesNC.forEach((av) => {
      if (av.Presente === 'sim') {
        const ensaio = ensaiosNC.find((e) => e.ID === av.EnsaioID);
        // Só conta a partir do início individual da bonificação, até o fim da contagem.
        if (ensaio && noPeriodoBonif_(ensaio, inicioBonifInd, fimContagem)) {
          bonificacao += valorBonifEvento_(ensaio, valorEnsaio, valorApresentacao, valorFestival);
        }
      }
    });
  }
  // Teto da temporada (Cláusula Sexta, III, "e") antes da sanção.
  const teto = tetoConfig_(config);
  const bonificacaoSemTeto = bonificacao;
  bonificacao = aplicarTeto_(bonificacao, teto);
  const tetoAtingido = teto > 0 && bonificacaoSemTeto >= teto;
  // Sanção (Cláusulas Sétima e Oitava): desconto sobre o total acumulado.
  const sancaoPct = penalidadeTotal_(brincante, advs);
  const bonificacaoBruta = bonificacao;
  bonificacao = bonificacao * (1 - sancaoPct / 100);

  const historico = avaliacoesNC.map((av) => {
    const ensaio = ensaiosNC.find((e) => e.ID === av.EnsaioID);
    return {
      data: ensaio ? ensaio.Data : '',
      tipo: ensaio ? ensaio.Tipo : '',
      presente: av.Presente === 'sim',
      justificada: av.Justificada === true,
      nota: Number(av.Nota),
      observacao: av.Observacao,
      avaliadoPor: av.AvaliadoPor,
    };
  }).sort((a, b) => new Date(b.data) - new Date(a.data));

  const freqMinima = ehItem_(brincante.Tipo) ? parseInt(config.frequenciaItem || 85, 10) : parseInt(config.frequenciaMinima || 75, 10);
  const dicas = montarDicas_(percPresenca, parseFloat(mediaNotas), percNotasBoas, freqMinima, parseInt(config.percentualNotaMinima || 75, 10));
  return {
    ...brincante,
    totalEnsaios, presencas, percPresenca,
    mediaNotas, percNotasBoas, notas,
    bonificacao: bonificacao.toFixed(2),
    bonificacaoBruta: bonificacaoBruta.toFixed(2),
    bonificacaoSemTeto: bonificacaoSemTeto.toFixed(2),
    teto: teto ? teto.toFixed(2) : '',
    tetoAtingido,
    sancaoPct,
    advertencias: advs,
    ativacao,
    menorDeIdade: ehMenor_(brincante.DataNascimento),
    idade: idadeAnos_(brincante.DataNascimento),
    papel: papelDanca_(brincante.Tipo),
    freqMinima,
    escolhaDestinoLiberada: config.escolhaDestinoLiberada === 'sim',
    captacao: {
      ...resumoCaptacao_(minhasIndicacoes, parseInt(config.metaSociosPorBrincante || 2, 10) || 0),
      indicacoes: minhasIndicacoes,
    },
    pagamento: {
      data1: config.dataPagamentoBonif || '',
      data2: config.dataPagamentoBonif2 || '',
      obs: config.obsPagamentoBonif || '',
    },
    dicas,
    historico,
  };
}

// idade em anos a partir da data de nascimento (YYYY-MM-DD); null se vazia.
function idadeAnos_(nasc) {
  if (!nasc) return null;
  const d = new Date(nasc + 'T00:00:00');
  if (isNaN(d)) return null;
  const h = new Date();
  let a = h.getFullYear() - d.getFullYear();
  const m = h.getMonth() - d.getMonth();
  if (m < 0 || (m === 0 && h.getDate() < d.getDate())) a--;
  return a;
}
function ehMenor_(nasc) { const a = idadeAnos_(nasc); return a !== null && a < 18; }

// Dicas por nível de desempenho (mostradas ao brincante no perfil).
function montarDicas_(freq, media, notaPct, freqMin, notaPctMin) {
  const dicas = [];
  if (freq < freqMin) {
    dicas.push({ nivel: 'alerta', texto: 'Sua presença está abaixo do mínimo (' + freqMin + '%). Avise faltas com 24h de antecedência e compareça mais — fale com o líder da sua fila.' });
  }
  if (media > 0 && media < 3) {
    dicas.push({ nivel: 'alerta', texto: 'Seu desempenho está abaixo do esperado. Procure a coordenação e os coreógrafos para reforço nos passos — a quadrilha está 100% à disposição para te ajudar, sem constrangimento.' });
  } else if (media >= 3 && media < 4) {
    dicas.push({ nivel: 'melhorar', texto: 'Você está quase na meta. Foque em sincronia e expressão e peça dicas aos líderes de fila e coreógrafos nos ensaios.' });
  } else if (media >= 4 && notaPct < notaPctMin) {
    dicas.push({ nivel: 'melhorar', texto: 'Boas notas, mas ainda falta constância: mantenha nota ≥ 4 em mais ensaios. Continue firme!' });
  } else if (media >= 4 && freq >= freqMin) {
    dicas.push({ nivel: 'bom', texto: 'Ótimo desempenho! Você está dentro das metas. Continue assim e ajude os colegas com mais dificuldade.' });
  }
  return dicas;
}

// ============================================================
// RANKING
// ============================================================
async function getRanking() {
  const [brincantesAll, avaliacoesRaw, ensaiosRaw] = await Promise.all([getBrincantes(), getAvaliacoes(), getEnsaios()]);
  const { ensaios, avaliacoes } = eventosMetrica_(ensaiosRaw, avaliacoesRaw);
  const brincantes = brincantesAll.filter((b) => ehDancarino_(b.Tipo));
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
      tipo: papelDanca_(b.Tipo),
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
  const [brincantesAll, ensaiosRaw, avaliacoesRaw, config, advsAll] = await Promise.all([
    getBrincantes(), getEnsaios(), getAvaliacoes(), getConfigMap_(), getAdvertencias(),
  ]);
  const { ensaios, avaliacoes } = filtrarCancelados_(ensaiosRaw, avaliacoesRaw);
  const metric = eventosMetrica_(ensaiosRaw, avaliacoesRaw); // p/ ativação (só ensaios)
  const brincantes = brincantesAll.filter((b) => ehDancarino_(b.Tipo) && b.OptBonificacao === 'sim');

  const valorEnsaio = parseFloat(config.valorEnsaio || 0.5);
  const valorApresentacao = parseFloat(config.valorApresentacao || 1.0);
  const valorFestival = parseFloat(config.valorFestival || 5.0);
  const teto = tetoConfig_(config);
  const inicioContagem = config.inicioContagem || '2026-05-01';
  const fimContagem = config.fimContagem || '2026-07-31';

  // Agrupa advertências por brincante para aplicar a sanção.
  const advsPor = {};
  advsAll.forEach((a) => { (advsPor[a.BrincanteID] = advsPor[a.BrincanteID] || []).push(a); });

  let totalGeral = 0, totalResgate = 0, totalDoacao = 0, noTeto = 0;
  const lista = brincantes.map((b) => {
    const avs = avaliacoes.filter((a) => a.BrincanteID === b.ID);
    const avsMetric = metric.avaliacoes.filter((a) => a.BrincanteID === b.ID);
    const ativacao = avaliarAtivacao(b, metric.ensaios, avsMetric, config);
    // Contagem a partir do início individual (fim da ativação), respeitando o piso.
    const inicioBonifInd = ativacao.bonificacaoInicio || inicioContagem;
    let valor = 0, ensaiosPresente = 0, apresentacoesPresente = 0, festivalPresente = false;
    avs.forEach((av) => {
      if (av.Presente === 'sim') {
        const ensaio = ensaios.find((e) => e.ID === av.EnsaioID);
        if (ensaio && noPeriodoBonif_(ensaio, inicioBonifInd, fimContagem)) {
          valor += valorBonifEvento_(ensaio, valorEnsaio, valorApresentacao, valorFestival);
          if (ensaio.Tipo === 'festival') festivalPresente = true;
          else if (ensaio.Tipo === 'apresentacao') apresentacoesPresente++;
          else if (ensaio.Tipo === 'regular' || ensaio.Tipo === 'ensaiao') ensaiosPresente++;
        }
      }
    });
    // Teto da temporada antes da sanção (mesma ordem do perfil).
    const valorSemTeto = valor;
    valor = aplicarTeto_(valor, teto);
    const atingiuTeto = teto > 0 && valorSemTeto >= teto;
    const sancaoPct = penalidadeTotal_(b, advsPor[b.ID]);
    const valorComSancao = valor * (1 - sancaoPct / 100);
    const elegivel = ativacao.ativado;
    const destino = b.DestinoBonificacao === 'doar' ? 'doar' : 'resgatar';
    if (elegivel) {
      totalGeral += valorComSancao;
      if (atingiuTeto) noTeto++;
      if (destino === 'doar') totalDoacao += valorComSancao;
      else totalResgate += valorComSancao;
    }
    return {
      nome: b.Apelido || b.Nome,
      fila: b.Fila,
      statusAtivacao: ativacao.status,
      elegivel,
      destino,
      ensaiosPresente,
      apresentacoesPresente,
      festivalPresente,
      valorBruto: valor.toFixed(2),
      valorSemTeto: valorSemTeto.toFixed(2),
      atingiuTeto,
      sancaoPct,
      valorAcumulado: valorComSancao.toFixed(2),
    };
  });

  return {
    lista,
    totalGeral: totalGeral.toFixed(2),
    totalResgate: totalResgate.toFixed(2),
    totalDoacao: totalDoacao.toFixed(2),
    teto: teto ? teto.toFixed(2) : '',
    noTeto,
    // Quanto a quadrilha pagaria, no pior caso, se todos os elegíveis chegassem
    // ao teto — o número que o Financeiro precisa para reservar o orçamento.
    tetoTotal: teto ? (teto * lista.filter((l) => l.elegivel).length).toFixed(2) : '',
    escolhaDestinoLiberada: config.escolhaDestinoLiberada === 'sim',
    pagamento: {
      data1: config.dataPagamentoBonif || '',
      data2: config.dataPagamentoBonif2 || '',
      obs: config.obsPagamentoBonif || '',
    },
    config: { valorEnsaio, valorApresentacao, valorFestival, teto },
  };
}

// ============================================================
// MISSÕES — CAPTAÇÃO DE SÓCIOS TORCEDORES
//
// Decisão de 27/07/2026, escrita no "Programa Socio Torcedor - Plano de
// Implementacao.docx" §6: trazer sócios é uma MISSÃO do brincante e vale
// **desempenho e troféu — reconhecimento, não dinheiro**. Por isso nada aqui
// entra na frequência, no ranking de desempenho nem na bonificação: a missão
// não toca o contrato. O brincante declara quem trouxe; a coordenação confirma.
//
// ⚠️ PRIVACIDADE — regra do documento, não preferência de implementação:
// a indicação guarda APENAS **nome e telefone**. CPF e data de nascimento
// juntos são a credencial de login do sócio no outro sistema (Site Sócio
// Torcedor); guardá-los aqui espalharia a senha de terceiros por um sistema
// que não precisa dela. O documento gravado é montado campo a campo — o que o
// cliente mandar além disso não entra, nem por engano nem de propósito.
//
// Coleção `indicacoes/{autoId}`:
//   BrincanteID, Nome, Telefone, Status (pendente|confirmada|recusada),
//   DataDeclaracao, DeclaradaPor, DecididaPor, DataDecisao, MotivoRecusa
// ============================================================
const STATUS_INDICACAO = ['pendente', 'confirmada', 'recusada'];

// Nome do troféu conforme o Plano §9 ("Chamador de Gente — indicar alguém que
// virou sócio de verdade"). Fica em constante de propósito: o nome já mudou uma
// vez (era "Padrinho") e a tela lê daqui, para não haver duas verdades.
const TROFEU_CAPTACAO = 'Chamador de Gente';

function normalizaTelefone_(t) { return String(t || '').replace(/\D/g, '').slice(0, 11); }

function normalizaIndicacao_(id, r) {
  return {
    id,
    BrincanteID: r.BrincanteID || '',
    Nome: r.Nome || '',
    Telefone: r.Telefone || '',
    Status: STATUS_INDICACAO.indexOf(r.Status) >= 0 ? r.Status : 'pendente',
    DataDeclaracao: r.DataDeclaracao || '',
    DeclaradaPor: r.DeclaradaPor || '',
    DecididaPor: r.DecididaPor || '',
    DataDecisao: r.DataDecisao || '',
    MotivoRecusa: r.MotivoRecusa || '',
  };
}

async function getIndicacoes(filtro) {
  filtro = filtro || {};
  const snap = await getDb().collection('indicacoes').get();
  let lista = snap.docs.map((d) => normalizaIndicacao_(d.id, d.data()));
  if (filtro.brincanteId) lista = lista.filter((i) => i.BrincanteID === filtro.brincanteId);
  if (filtro.status) lista = lista.filter((i) => i.Status === filtro.status);
  return lista.sort((a, b) => (b.DataDeclaracao || '').localeCompare(a.DataDeclaracao || ''));
}

/**
 * Declara um sócio trazido. Escopo `autenticado`: o brincante declara por si e
 * o ID vem DA SESSÃO — mesma trava de getPerfilBrincante, senão bastaria
 * trocar o parâmetro para creditar a missão de outra pessoa. Admin pode
 * declarar em nome de alguém (quem chegou pela coordenação, no papel).
 */
async function addIndicacao(dados, usuario) {
  dados = dados || {};
  const ehAdmin = !!usuario && usuario.tipo === 'admin';
  const brincanteId = ehAdmin
    ? String(dados.brincanteId || '').trim().toUpperCase()
    : (usuario ? usuario.id : '');
  if (!brincanteId) return { success: false, message: 'Escolha qual brincante trouxe o sócio.' };

  const nome = String(dados.nome || '').trim().replace(/\s+/g, ' ');
  const telefone = normalizaTelefone_(dados.telefone);
  if (nome.length < 3) return { success: false, message: 'Informe o nome de quem você trouxe.' };
  if (telefone.length < 10) return { success: false, message: 'Informe o telefone com DDD (10 ou 11 dígitos).' };

  const brincante = (await getBrincantes()).find((b) => b.ID === brincanteId);
  if (!brincante) return { success: false, message: 'Brincante não encontrado.' };

  // O mesmo contato declarado por dois brincantes vira briga na hora do troféu.
  // Recusada não bloqueia: se a coordenação recusou, o contato volta a valer.
  const jaTem = (await getIndicacoes({})).find((i) => i.Telefone === telefone && i.Status !== 'recusada');
  if (jaTem) {
    return {
      success: false,
      message: jaTem.BrincanteID === brincanteId
        ? 'Você já declarou esse contato.'
        : 'Esse contato já foi declarado por outro brincante.',
    };
  }

  // Montado campo a campo de propósito — ver o aviso de privacidade acima.
  const doc = {
    BrincanteID: brincanteId,
    Nome: nome,
    Telefone: telefone,
    Status: 'pendente',
    DataDeclaracao: nowIso(),
    DeclaradaPor: usuario ? `${usuario.nome} (${usuario.id})` : 'sistema',
    DecididaPor: '',
    DataDecisao: '',
    MotivoRecusa: '',
  };
  const ref = await getDb().collection('indicacoes').add(doc);
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'INDICACAO_SOCIO', `Indicação de "${nome}" creditada a ${brincanteId}`);
  }
  return { success: true, id: ref.id, indicacao: normalizaIndicacao_(ref.id, doc) };
}

/**
 * Confirmação manual da coordenação — a base do desenho. O cruzamento
 * automático com o cadastro do outro sistema entra por cima disto depois
 * (PENDENCIAS.md §2), nunca no lugar.
 */
async function decidirIndicacao(id, decisao, motivo, usuario) {
  if (STATUS_INDICACAO.indexOf(decisao) < 0) return { success: false, message: 'Decisão inválida.' };
  const ref = getDb().collection('indicacoes').doc(String(id));
  const doc = await ref.get();
  if (!doc.exists) return { success: false, message: 'Indicação não encontrada.' };

  const pendente = decisao === 'pendente';
  await ref.update({
    Status: decisao,
    DecididaPor: pendente ? '' : (usuario ? `${usuario.nome} (${usuario.id})` : 'sistema'),
    DataDecisao: pendente ? '' : nowIso(),
    MotivoRecusa: decisao === 'recusada' ? String(motivo || '').trim().slice(0, 200) : '',
  });
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'INDICACAO_DECIDIDA', `Indicação ${id} (${doc.data().Nome || ''}) marcada como ${decisao}`);
  }
  return { success: true };
}

/**
 * Escopo `autenticado`: a coordenação apaga qualquer uma; o brincante só apaga
 * a PRÓPRIA e só enquanto pendente — depois de decidida, quem desfaz é a
 * coordenação. O dono é lido do documento, nunca do cliente.
 */
async function removeIndicacao(id, usuario) {
  const ref = getDb().collection('indicacoes').doc(String(id));
  const doc = await ref.get();
  if (!doc.exists) return { success: false, message: 'Indicação não encontrada.' };
  const r = normalizaIndicacao_(doc.id, doc.data());

  if (!usuario || usuario.tipo !== 'admin') {
    if (!usuario || r.BrincanteID !== usuario.id) return { success: false, message: 'Esta indicação não é sua.' };
    if (r.Status !== 'pendente') return { success: false, message: 'Já foi avaliada pela coordenação — fale com ela para desfazer.' };
  }
  await ref.delete();
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'INDICACAO_REMOVIDA', `Indicação ${id} (${r.Nome}) removida`);
  }
  return { success: true };
}

// Resumo da missão de um brincante. Usado no perfil dele e no painel da
// coordenação — um cálculo só, para os dois lados nunca divergirem.
function resumoCaptacao_(indicacoes, meta) {
  const confirmadas = indicacoes.filter((i) => i.Status === 'confirmada').length;
  const pendentes = indicacoes.filter((i) => i.Status === 'pendente').length;
  const recusadas = indicacoes.filter((i) => i.Status === 'recusada').length;
  return {
    meta,
    confirmadas,
    pendentes,
    recusadas,
    // Troféu de captação (Plano §9): reconhecimento, sem valor em dinheiro.
    trofeu: meta > 0 && confirmadas >= meta,
    trofeuNome: TROFEU_CAPTACAO,
    progresso: meta > 0 ? Math.min(100, Math.round((confirmadas / meta) * 100)) : 0,
  };
}

/**
 * Painel da coordenação: quem trouxe quanto. É um ranking de RECONHECIMENTO —
 * não se mistura com o ranking de desempenho (getRanking), que continua sendo
 * só presença e nota.
 */
async function getCaptacao() {
  const [brincantes, indicacoes, config] = await Promise.all([getBrincantes(), getIndicacoes({}), getConfigMap_()]);
  const meta = parseInt(config.metaSociosPorBrincante || 2, 10) || 0;

  const porBrincante = {};
  indicacoes.forEach((i) => {
    (porBrincante[i.BrincanteID] = porBrincante[i.BrincanteID] || []).push(i);
  });

  // A missão é dos brincantes (Plano §6, "Brincantes (embaixadores)"), mas quem
  // já tem indicação entra de qualquer jeito — mudar o tipo de alguém não pode
  // sumir com o que a pessoa já trouxe.
  const ranking = brincantes
    .filter((b) => ehDancarino_(b.Tipo) || porBrincante[b.ID])
    .map((b) => ({
      id: b.ID,
      nome: b.Nome,
      apelido: b.Apelido || '',
      tipo: b.Tipo,
      ...resumoCaptacao_(porBrincante[b.ID] || [], meta),
    }))
    .sort((a, b) => (b.confirmadas - a.confirmadas) || (b.pendentes - a.pendentes) || a.nome.localeCompare(b.nome));

  return {
    meta,
    metaTotal: meta * ranking.length,
    trofeuNome: TROFEU_CAPTACAO,
    confirmadas: indicacoes.filter((i) => i.Status === 'confirmada').length,
    pendentes: indicacoes.filter((i) => i.Status === 'pendente').length,
    trofeus: ranking.filter((r) => r.trofeu).length,
    ranking,
    indicacoes,
  };
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

// Salva várias chaves de config de uma vez (usado pela aba Configurações).
async function updateConfigMap(mapa, usuario) {
  if (!mapa || typeof mapa !== 'object') return { success: false };
  const limpo = {};
  Object.keys(mapa).forEach((k) => { limpo[k] = String(mapa[k]); });
  await getDb().collection('config').doc('app').set(limpo, { merge: true });
  if (usuario) {
    await registrarLog_(usuario.id, usuario.nome, 'CONFIG_ALTERADA', `Configurações atualizadas: ${Object.keys(limpo).join(', ')}`);
  }
  return { success: true };
}

// ============================================================
// EXPORT - funções disponíveis para a API.
// Quem pode chamar cada uma é declarado em netlify/functions/api.js
// (escopo + aridade). Estar aqui não basta para ser chamável.
// ============================================================
module.exports = {
  login, logout, entrarComoBrincante,
  getLogs,
  getBrincantes, addBrincante, addBrincantesLote, updateBrincante, setDestinoBonificacao, removeBrincante,
  getEnsaios, addEnsaio, updateEvento, deleteEnsaio,
  getAvaliacoes, salvarAvaliacoes, upsertAvaliacao,
  getAdvertencias, addAdvertencia, removeAdvertencia,
  getIndicacoes, addIndicacao, decidirIndicacao, removeIndicacao, getCaptacao,
  getDashboard, getPerfilBrincante, getRanking, getSimulacaoBonificacao,
  getConfig, getStatusAdesao, updateConfig, updateConfigMap,
  // helpers exportados para o seed
  _getConfigMap: getConfigMap_,
  _DEFAULT_CONFIG: DEFAULT_CONFIG,
};
