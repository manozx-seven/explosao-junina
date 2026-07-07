// ============================================================
// Cria (ou atualiza) um usuário DEV de coordenação para acesso
// administrativo, sem precisar cadastrar dados pessoais reais.
//
// Uso:
//   node scripts/seed-dev.js            -> ID=DEV, senha=123456
//   node scripts/seed-dev.js 987654     -> ID=DEV, senha=987654
//
// Login no sistema: ID = DEV, Senha = (o PIN numérico abaixo)
// Depois, pela interface, cadastre as pessoas reais e promova quem
// precisar a "coordenacao". Este usuário DEV pode ser removido no fim.
// ============================================================
require('dotenv').config();
const { getDb } = require('../server/firebase');
const { _DEFAULT_CONFIG } = require('../server/handlers');

function normalizaCpf(cpf) { return String(cpf || '').replace(/\D/g, '').trim().padStart(11, '0'); }

async function main() {
  const pin = process.argv[2] || '123456';
  const senhaArmazenada = normalizaCpf(pin);
  const db = getDb();

  // Garante a configuração padrão (sem sobrescrever, se já existir)
  const configRef = db.collection('config').doc('app');
  const configSnap = await configRef.get();
  if (!configSnap.exists) {
    await configRef.set(_DEFAULT_CONFIG);
    console.log('✔ Configuração padrão criada em config/app');
  } else {
    console.log('• config/app já existe — mantido');
  }

  // Cria/atualiza o usuário DEV (doc id = DEV)
  const dev = {
    ID: 'DEV',
    Nome: 'Desenvolvedor',
    Apelido: 'DEV',
    CPF: senhaArmazenada,
    Fila: '',
    Posicao: '',
    Tipo: 'coordenacao',
    DataAdesao: new Date().toISOString().slice(0, 10),
    OptBonificacao: 'nao',
    StatusAtivacao: 'ativado',
    QualificacaoExtra: '',
  };
  await db.collection('brincantes').doc('DEV').set(dev);

  console.log('\n=================================================');
  console.log('✔ Usuário DEV pronto! Faça login no sistema com:');
  console.log('   ID:    DEV');
  console.log('   Senha: ' + pin + '   (digite exatamente este número)');
  console.log('=================================================\n');
  process.exit(0);
}

main().catch((e) => { console.error('Erro:', e.message); process.exit(1); });
