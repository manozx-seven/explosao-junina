// ============================================================
// SISTEMA DE AVALIAÇÃO - EXPLOSÃO JUNINA DE BERURI
// Code.gs - Backend v2
// ============================================================

const SS_ID = '1tlc6BH5MM-KzwRdoZweWWgxqlfRyNXbCVQMT5eD5d2w';

function getSheet(name) {
  const ss = SS_ID ? SpreadsheetApp.openById(SS_ID) : SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(name);
  if (!sheet) sheet = setupSheet_(ss, name);
  return sheet;
}

// ============================================================
// SETUP - Cria as abas se não existirem
// ============================================================
function setupSheet_(ss, name) {
  const sheet = ss.insertSheet(name);
  const headers = {
    'Brincantes': ['ID','Nome','Apelido','CPF','Fila','Posicao','Tipo','DataAdesao','OptBonificacao','StatusAtivacao'],
    'Ensaios': ['ID','Data','Tipo','Descricao','CriadoPor'],
    'Avaliacoes': ['EnsaioID','BrincanteID','Presente','Nota','Observacao','AvaliadoPor','DataRegistro'],
    'Logs': ['DataHora','UsuarioID','UsuarioNome','Acao','Detalhes'],
    'Config': ['Chave','Valor']
  };
  if (headers[name]) {
    sheet.getRange(1, 1, 1, headers[name].length).setValues([headers[name]]);
    sheet.getRange(1, 1, 1, headers[name].length).setFontWeight('bold');
  }
  if (name === 'Config') {
    const defaults = [
      ['valorEnsaio', '0.50'],
      ['valorApresentacao', '1.00'],
      ['valorFestival', '5.00'],
      ['mesesAtivacao', '3'],
      ['frequenciaMinima', '75'],
      ['notaMinima', '4'],
      ['percentualNotaMinima', '75'],
      ['temporada', '2026'],
      ['inicioTemporada', '2026-02-01'],
      ['fimContagem', '2026-07-31']
    ];
    sheet.getRange(2, 1, defaults.length, 2).setValues(defaults);
  }
  return sheet;
}

function setupAll() {
  ['Brincantes','Ensaios','Avaliacoes','Logs','Config'].forEach(n => getSheet(n));
  return {success: true, message: 'Planilha configurada com sucesso!'};
}

// ============================================================
// GERAR IDs - Para brincantes cadastrados direto na planilha
// Rode esta função pelo editor do Apps Script
// ============================================================
function gerarIDs() {
  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();
  const config = getConfigMap_();
  const temporada = config.temporada || '2026';

  // Encontra o maior número sequencial existente
  let maxSeq = 0;
  for (let i = 1; i < data.length; i++) {
    const id = String(data[i][0]).trim();
    const match = id.match(/^EXP\d{4}(\d+)$/);
    if (match) {
      const seq = parseInt(match[1]);
      if (seq > maxSeq) maxSeq = seq;
    }
  }

  let count = 0;
  for (let i = 1; i < data.length; i++) {
    if (!data[i][0] || String(data[i][0]).trim() === '') {
      maxSeq++;
      const id = 'EXP' + temporada + String(maxSeq).padStart(2, '0');
      sheet.getRange(i + 1, 1).setValue(id);
      count++;
    }
  }
  SpreadsheetApp.getUi().alert(`IDs gerados: ${count} brincante(s).\nPadrão: EXP${temporada}01, EXP${temporada}02...`);
  return { success: true, count };
}

// ============================================================
// CORRIGIR CPFs - Formata como texto com 11 dígitos
// Rode esta função se CPFs foram salvos como número
// ============================================================
function corrigirCPFs() {
  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();
  let count = 0;
  for (let i = 1; i < data.length; i++) {
    const cpfRaw = data[i][3];
    if (cpfRaw !== '' && cpfRaw !== null && cpfRaw !== undefined) {
      const cpfCorrigido = String(cpfRaw).replace(/\D/g, '').padStart(11, '0');
      sheet.getRange(i + 1, 4).setNumberFormat('@').setValue(cpfCorrigido);
      count++;
    }
  }
  SpreadsheetApp.getUi().alert(`CPFs corrigidos: ${count}. Todos formatados como texto com 11 dígitos.`);
  return { success: true, count };
}

// ============================================================
// WEBAPP
// ============================================================
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Explosão Junina - Sistema de Avaliação')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

// ============================================================
// AUTENTICAÇÃO - Login por ID + CPF
// ============================================================
function login(id, cpf) {
  const cpfLimpo = String(cpf).replace(/\D/g, '').trim().padStart(11, '0');
  const idLimpo = String(id).trim().toUpperCase();

  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();

  for (let i = 1; i < data.length; i++) {
    const rowId = String(data[i][0]).trim().toUpperCase();
    const rowCpf = String(data[i][3]).replace(/\D/g, '').trim().padStart(11, '0');

    if (rowId === idLimpo && rowCpf === cpfLimpo) {
      const tipo = data[i][6];
      const nome = data[i][1];

      registrarLog_(rowId, nome, 'LOGIN', 'Acesso ao sistema');

      return {
        success: true,
        role: tipo === 'coordenacao' ? 'admin' : 'brincante',
        nome: nome,
        id: data[i][0],
        apelido: data[i][2],
        fila: data[i][4],
        tipo: tipo
      };
    }
  }
  return { success: false, message: 'ID ou CPF inválido' };
}

// ============================================================
// LOGS - Registro de ações
// ============================================================
function registrarLog_(usuarioId, usuarioNome, acao, detalhes) {
  try {
    const sheet = getSheet('Logs');
    sheet.appendRow([
      new Date().toISOString(),
      usuarioId,
      usuarioNome,
      acao,
      detalhes
    ]);
  } catch (e) {
    // Silencia erros de log para não quebrar operações
    console.error('Erro ao registrar log:', e);
  }
}

function getLogs(limite) {
  const sheet = getSheet('Logs');
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];
  const logs = data.slice(1).map(row => ({
    dataHora: row[0],
    usuarioId: row[1],
    usuarioNome: row[2],
    acao: row[3],
    detalhes: row[4]
  }));
  logs.reverse(); // mais recentes primeiro
  return limite ? logs.slice(0, limite) : logs;
}

// ============================================================
// BRINCANTES - CRUD
// ============================================================
function getBrincantes() {
  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];
  const headers = data[0];
  return data.slice(1).map(row => {
    const obj = {};
    headers.forEach((h, i) => {
      const val = row[i];
      obj[h] = val instanceof Date ? val.toISOString().slice(0, 10) : (val !== null && val !== undefined ? val : '');
    });
    return obj;
  });
}

function addBrincante(dados, usuario) {
  const sheet = getSheet('Brincantes');
  const id = proximoId_();

  // Bloqueia opt-in bonificação fora do período de adesão
  const config = getConfigMap_();
  const fimAdesao = config.fimAdesao || '2026-04-30';
  const hoje = new Date().toISOString().slice(0, 10);
  if (hoje > fimAdesao && dados.optBonificacao === 'sim') {
    dados.optBonificacao = 'nao';
  }

  const cpfTexto = String(dados.cpf || '');
  const row = [
    id,
    dados.nome,
    dados.apelido || '',
    cpfTexto,
    dados.fila || '',
    dados.posicao || '',
    dados.tipo || 'brincante',
    new Date().toISOString().slice(0, 10),
    dados.optBonificacao || 'nao',
    'pendente'
  ];
  sheet.appendRow(row);
  // Força CPF como texto para preservar zeros à esquerda
  const lastRow = sheet.getLastRow();
  sheet.getRange(lastRow, 4).setNumberFormat('@').setValue(cpfTexto);

  if (usuario) {
    registrarLog_(usuario.id, usuario.nome, 'CADASTRO', `Brincante cadastrado: ${dados.nome} (${id})`);
  }

  return { success: true, id, message: `Brincante cadastrado! ID: ${id}` };
}

function updateBrincante(id, dados, usuario) {
  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]).trim() === String(id).trim()) {
      const changes = [];
      if (dados.nome !== undefined) { sheet.getRange(i + 1, 2).setValue(dados.nome); changes.push('nome'); }
      if (dados.apelido !== undefined) { sheet.getRange(i + 1, 3).setValue(dados.apelido); changes.push('apelido'); }
      if (dados.cpf !== undefined) { sheet.getRange(i + 1, 4).setNumberFormat('@').setValue(String(dados.cpf)); changes.push('cpf'); }
      if (dados.fila !== undefined) { sheet.getRange(i + 1, 5).setValue(dados.fila); changes.push('fila'); }
      if (dados.posicao !== undefined) { sheet.getRange(i + 1, 6).setValue(dados.posicao); changes.push('posicao'); }
      if (dados.tipo !== undefined) { sheet.getRange(i + 1, 7).setValue(dados.tipo); changes.push('tipo'); }
      if (dados.optBonificacao !== undefined) { sheet.getRange(i + 1, 9).setValue(dados.optBonificacao); changes.push('bonificacao'); }
      if (dados.statusAtivacao !== undefined) { sheet.getRange(i + 1, 10).setValue(dados.statusAtivacao); changes.push('ativacao'); }
      if (dados.qualificacaoExtra !== undefined) { sheet.getRange(i + 1, 11).setValue(dados.qualificacaoExtra); changes.push('qualificacao'); }

      if (usuario) {
        registrarLog_(usuario.id, usuario.nome, 'EDIÇÃO', `Brincante ${id} editado. Campos: ${changes.join(', ')}`);
      }
      return { success: true };
    }
  }
  return { success: false, message: 'Brincante não encontrado' };
}

function removeBrincante(id, usuario) {
  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]).trim() === String(id).trim()) {
      const nome = data[i][1];
      sheet.deleteRow(i + 1);
      if (usuario) {
        registrarLog_(usuario.id, usuario.nome, 'EXCLUSÃO', `Brincante removido: ${nome} (${id})`);
      }
      return { success: true };
    }
  }
  return { success: false };
}

// ============================================================
// ENSAIOS
// ============================================================
function getEnsaios() {
  const sheet = getSheet('Ensaios');
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];
  return data.slice(1).map(row => ({
    ID: row[0],
    Data: row[1] instanceof Date ? row[1].toISOString().slice(0, 10) : row[1],
    Tipo: row[2],
    Descricao: row[3],
    CriadoPor: row[4]
  }));
}

function addEnsaio(dados, usuario) {
  const sheet = getSheet('Ensaios');
  const dataFormatada = String(dados.data).replace(/-/g, '');
  const id = 'ENS' + dataFormatada + '_' + String(Date.now()).slice(-4);
  const criadoPor = usuario ? `${usuario.nome} (${usuario.id})` : '';
  sheet.appendRow([id, dados.data, dados.tipo, dados.descricao || '', criadoPor]);

  if (usuario) {
    registrarLog_(usuario.id, usuario.nome, 'ENSAIO_CRIADO', `Ensaio ${id}: ${dados.tipo} em ${dados.data}`);
  }
  return { success: true, id };
}

function deleteEnsaio(id, usuario) {
  const sheet = getSheet('Ensaios');
  const data = sheet.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (data[i][0] === id) {
      const info = `${data[i][2]} em ${data[i][1]}`;
      sheet.deleteRow(i + 1);
      // Deletar avaliações desse ensaio
      const avSheet = getSheet('Avaliacoes');
      const avData = avSheet.getDataRange().getValues();
      for (let j = avData.length - 1; j >= 1; j--) {
        if (avData[j][0] === id) avSheet.deleteRow(j + 1);
      }
      if (usuario) {
        registrarLog_(usuario.id, usuario.nome, 'ENSAIO_EXCLUIDO', `Ensaio ${id} excluído: ${info}`);
      }
      return { success: true };
    }
  }
  return { success: false };
}

// ============================================================
// AVALIAÇÕES
// ============================================================
function getAvaliacoes(filtro) {
  const sheet = getSheet('Avaliacoes');
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];
  let results = data.slice(1).map(row => ({
    EnsaioID: row[0], BrincanteID: row[1], Presente: row[2],
    Nota: row[3], Observacao: row[4], AvaliadoPor: row[5], DataRegistro: row[6]
  }));
  if (filtro) {
    if (filtro.ensaioId) results = results.filter(r => r.EnsaioID === filtro.ensaioId);
    if (filtro.brincanteId) results = results.filter(r => r.BrincanteID === filtro.brincanteId);
  }
  return results;
}

function salvarAvaliacoes(ensaioId, avaliacoes, usuario) {
  const sheet = getSheet('Avaliacoes');
  // Remove avaliações existentes desse ensaio
  const data = sheet.getDataRange().getValues();
  for (let i = data.length - 1; i >= 1; i--) {
    if (data[i][0] === ensaioId) sheet.deleteRow(i + 1);
  }
  // Insere novas
  const now = new Date().toISOString();
  const avaliadoPor = usuario ? `${usuario.nome} (${usuario.id})` : 'sistema';
  avaliacoes.forEach(av => {
    sheet.appendRow([
      ensaioId,
      av.brincanteId,
      av.presente ? 'sim' : 'nao',
      av.nota || 0,
      av.observacao || '',
      avaliadoPor,
      now
    ]);
  });

  if (usuario) {
    const presentes = avaliacoes.filter(a => a.presente).length;
    registrarLog_(usuario.id, usuario.nome, 'AVALIAÇÃO', `Ensaio ${ensaioId}: ${avaliacoes.length} brincantes avaliados, ${presentes} presentes`);
  }

  return { success: true, count: avaliacoes.length };
}

// ============================================================
// DASHBOARD / MÉTRICAS
// ============================================================
function getDashboard() {
  const brincantes = getBrincantes();
  const ensaios = getEnsaios();
  const avaliacoes = getAvaliacoes();

  const totalBrincantes = brincantes.filter(b => b.Tipo !== 'coordenacao').length;
  const totalCoord = brincantes.filter(b => b.Tipo === 'coordenacao').length;
  const totalEnsaios = ensaios.length;
  const optBonificacao = brincantes.filter(b => b.OptBonificacao === 'sim').length;
  const ativados = brincantes.filter(b => b.StatusAtivacao === 'ativado').length;

  let totalPresencas = 0, totalRegistros = 0;
  avaliacoes.forEach(a => {
    if (a.Presente === 'sim') totalPresencas++;
    totalRegistros++;
  });
  const mediaPresenca = totalRegistros > 0 ? Math.round((totalPresencas / totalRegistros) * 100) : 0;

  let somaNotas = 0, contNotas = 0;
  avaliacoes.forEach(a => {
    if (a.Presente === 'sim' && a.Nota > 0) {
      somaNotas += Number(a.Nota);
      contNotas++;
    }
  });
  const mediaNotas = contNotas > 0 ? (somaNotas / contNotas).toFixed(1) : '0.0';

  return {
    totalBrincantes, totalCoord, totalEnsaios, optBonificacao, ativados,
    mediaPresenca, mediaNotas, totalPresencas, totalRegistros
  };
}

// ============================================================
// PERFIL DO BRINCANTE
// ============================================================
function getPerfilBrincante(brincanteId) {
  const brincantes = getBrincantes();
  const brincante = brincantes.find(b => b.ID === brincanteId);
  if (!brincante) return null;

  const avaliacoes = getAvaliacoes({ brincanteId });
  const ensaios = getEnsaios();
  const config = getConfigMap_();

  const totalEnsaios = ensaios.length;
  const presencas = avaliacoes.filter(a => a.Presente === 'sim').length;
  const percPresenca = totalEnsaios > 0 ? Math.round((presencas / totalEnsaios) * 100) : 0;

  const notas = avaliacoes.filter(a => a.Presente === 'sim' && a.Nota > 0).map(a => Number(a.Nota));
  const mediaNotas = notas.length > 0 ? (notas.reduce((a, b) => a + b, 0) / notas.length).toFixed(1) : '0.0';
  const notasAcimaDe4 = notas.filter(n => n >= 4).length;
  const percNotasBoas = notas.length > 0 ? Math.round((notasAcimaDe4 / notas.length) * 100) : 0;

  const valorEnsaio = parseFloat(config.valorEnsaio || 0.5);
  const valorApresentacao = parseFloat(config.valorApresentacao || 1.0);
  const valorFestival = parseFloat(config.valorFestival || 5.0);

  let bonificacao = 0;
  if (brincante.OptBonificacao === 'sim' && brincante.StatusAtivacao === 'ativado') {
    avaliacoes.forEach(av => {
      if (av.Presente === 'sim') {
        const ensaio = ensaios.find(e => e.ID === av.EnsaioID);
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

  const historico = avaliacoes.map(av => {
    const ensaio = ensaios.find(e => e.ID === av.EnsaioID);
    return {
      data: ensaio ? ensaio.Data : '',
      tipo: ensaio ? ensaio.Tipo : '',
      presente: av.Presente === 'sim',
      nota: Number(av.Nota),
      observacao: av.Observacao,
      avaliadoPor: av.AvaliadoPor
    };
  }).sort((a, b) => new Date(b.data) - new Date(a.data));

  return {
    ...brincante,
    totalEnsaios, presencas, percPresenca,
    mediaNotas, percNotasBoas, notas,
    bonificacao: bonificacao.toFixed(2),
    historico
  };
}

// ============================================================
// RANKING
// ============================================================
function getRanking() {
  const brincantes = getBrincantes().filter(b => b.Tipo !== 'coordenacao');
  const avaliacoes = getAvaliacoes();
  const ensaios = getEnsaios();
  const totalEnsaios = ensaios.length;

  return brincantes.map(b => {
    const avs = avaliacoes.filter(a => a.BrincanteID === b.ID);
    const presencas = avs.filter(a => a.Presente === 'sim').length;
    const notas = avs.filter(a => a.Presente === 'sim' && a.Nota > 0).map(a => Number(a.Nota));
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
      totalAvaliacoes: notas.length
    };
  }).sort((a, b) => parseFloat(b.mediaNotas) - parseFloat(a.mediaNotas) || b.percPresenca - a.percPresenca);
}

// ============================================================
// BONIFICAÇÃO - SIMULAÇÃO
// ============================================================
function getSimulacaoBonificacao() {
  const brincantes = getBrincantes().filter(b => b.Tipo !== 'coordenacao' && b.OptBonificacao === 'sim');
  const ensaios = getEnsaios();
  const avaliacoes = getAvaliacoes();
  const config = getConfigMap_();

  const valorEnsaio = parseFloat(config.valorEnsaio || 0.5);
  const valorApresentacao = parseFloat(config.valorApresentacao || 1.0);
  const valorFestival = parseFloat(config.valorFestival || 5.0);

  let totalGeral = 0;

  const lista = brincantes.map(b => {
    const avs = avaliacoes.filter(a => a.BrincanteID === b.ID);
    let valor = 0;
    let ensaiosPresente = 0;
    let apresentacoesPresente = 0;
    let festivalPresente = false;

    avs.forEach(av => {
      if (av.Presente === 'sim') {
        const ensaio = ensaios.find(e => e.ID === av.EnsaioID);
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
      valorAcumulado: valor.toFixed(2)
    };
  });

  return { lista, totalGeral: totalGeral.toFixed(2), config: { valorEnsaio, valorApresentacao, valorFestival } };
}

// ============================================================
// CONFIG
// ============================================================
function getConfig() {
  return getConfigMap_();
}

function getStatusAdesao() {
  const config = getConfigMap_();
  const fimAdesao = config.fimAdesao || '2026-04-30';
  const hoje = new Date().toISOString().slice(0, 10);
  return {
    dentroDoPeríodo: hoje <= fimAdesao,
    fimAdesao: fimAdesao
  };
}

function updateConfig(chave, valor) {
  const sheet = getSheet('Config');
  const data = sheet.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (data[i][0] === chave) {
      sheet.getRange(i + 1, 2).setValue(valor);
      return { success: true };
    }
  }
  sheet.appendRow([chave, valor]);
  return { success: true };
}

// ============================================================
// HELPERS
// ============================================================
function getConfigMap_() {
  const sheet = getSheet('Config');
  const data = sheet.getDataRange().getValues();
  const map = {};
  for (let i = 1; i < data.length; i++) {
    map[data[i][0]] = data[i][1];
  }
  return map;
}

function proximoId_() {
  const sheet = getSheet('Brincantes');
  const data = sheet.getDataRange().getValues();
  const config = getConfigMap_();
  const temporada = config.temporada || '2026';
  let maxSeq = 0;
  for (let i = 1; i < data.length; i++) {
    const id = String(data[i][0]).trim();
    const match = id.match(/^EXP\d{4}(\d+)$/);
    if (match) {
      const seq = parseInt(match[1]);
      if (seq > maxSeq) maxSeq = seq;
    }
  }
  return 'EXP' + temporada + String(maxSeq + 1).padStart(2, '0');
}

function testarLogin() {
  const resultado = login('EXP202601', '05165322270');
  Logger.log(JSON.stringify(resultado));
}

function testarBrincantes() {
  const resultado = getBrincantes();
  Logger.log('Total: ' + resultado.length);
  Logger.log(JSON.stringify(resultado));
}