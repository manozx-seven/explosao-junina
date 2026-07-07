// ============================================================
// Seed inicial do Firestore.
//   - grava a configuração padrão em config/app
//   - cria o primeiro usuário de coordenação (admin) já ATIVADO
//
// Uso:
//   node scripts/seed.js "<CPF>" "<Nome completo>"
// Exemplo:
//   node scripts/seed.js 05165322270 "Coordenação Geral"
//
// O ID de login é gerado automaticamente (ex: EXP202601) e mostrado no final.
// ============================================================
require('dotenv').config();
const { getDb } = require('../server/firebase');
const { _DEFAULT_CONFIG } = require('../server/handlers');

function normalizaCpf(cpf) { return String(cpf || '').replace(/\D/g, '').trim().padStart(11, '0'); }

async function main() {
  const cpf = process.argv[2];
  const nome = process.argv[3];

  if (!cpf || !nome) {
    console.error('Uso: node scripts/seed.js "<CPF>" "<Nome completo>"');
    process.exit(1);
  }

  const db = getDb();

  // 1) Configuração padrão (não sobrescreve chaves já existentes)
  const configRef = db.collection('config').doc('app');
  const configSnap = await configRef.get();
  if (!configSnap.exists) {
    await configRef.set(_DEFAULT_CONFIG);
    console.log('✔ Configuração padrão criada em config/app');
  } else {
    console.log('• config/app já existe — mantido como está');
  }
  const config = { ..._DEFAULT_CONFIG, ...(configSnap.exists ? configSnap.data() : {}) };
  const temporada = config.temporada || '2026';

  // 2) Gera o próximo ID via contador (mesma lógica do backend)
  const counterRef = db.collection('counters').doc('brincantes');
  const seq = await db.runTransaction(async (t) => {
    const doc = await t.get(counterRef);
    const cur = doc.exists ? (doc.data().seq || 0) : 0;
    const next = cur + 1;
    t.set(counterRef, { seq: next }, { merge: true });
    return next;
  });
  const id = 'EXP' + temporada + String(seq).padStart(2, '0');

  // 3) Cria o admin (coordenação), já ativado
  const admin = {
    ID: id,
    Nome: nome,
    Apelido: 'Coordenação',
    CPF: normalizaCpf(cpf),
    Fila: '',
    Posicao: '',
    Tipo: 'coordenacao',
    DataAdesao: new Date().toISOString().slice(0, 10),
    OptBonificacao: 'nao',
    StatusAtivacao: 'ativado',
    QualificacaoExtra: '',
  };
  await db.collection('brincantes').doc(id).set(admin);

  console.log('\n==========================================');
  console.log('✔ Usuário de coordenação criado com sucesso!');
  console.log('   Login (ID):  ' + id);
  console.log('   Senha (CPF): ' + normalizaCpf(cpf));
  console.log('==========================================\n');
  process.exit(0);
}

main().catch((e) => {
  console.error('Erro no seed:', e);
  process.exit(1);
});
