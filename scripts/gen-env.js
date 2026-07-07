// Gera o arquivo .env a partir do serviceAccountKey.json do Firebase.
// Uso: node scripts/gen-env.js
const fs = require('fs');
const path = require('path');

const keyPath = path.join(__dirname, '..', 'serviceAccountKey.json');
if (!fs.existsSync(keyPath)) {
  console.error('serviceAccountKey.json não encontrado na raiz do projeto.');
  process.exit(1);
}

const k = JSON.parse(fs.readFileSync(keyPath, 'utf8'));
if (!k.project_id || !k.client_email || !k.private_key) {
  console.error('JSON inválido: faltam project_id / client_email / private_key.');
  process.exit(1);
}

const env = [
  `FIREBASE_PROJECT_ID=${k.project_id}`,
  `FIREBASE_CLIENT_EMAIL=${k.client_email}`,
  `FIREBASE_PRIVATE_KEY="${k.private_key.replace(/\n/g, '\\n')}"`,
  '',
].join('\n');

fs.writeFileSync(path.join(__dirname, '..', '.env'), env);
console.log('✔ .env gerado com sucesso');
console.log('  FIREBASE_PROJECT_ID   =', k.project_id);
console.log('  FIREBASE_CLIENT_EMAIL =', k.client_email);
console.log('  FIREBASE_PRIVATE_KEY  = (ok, ' + k.private_key.length + ' chars, oculta)');
