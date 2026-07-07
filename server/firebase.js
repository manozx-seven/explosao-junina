// ============================================================
// Firebase Admin - inicialização a partir de variáveis de ambiente
// ============================================================
const admin = require('firebase-admin');

let initialized = false;

function initApp() {
  if (initialized) return;

  const projectId = process.env.FIREBASE_PROJECT_ID;
  const clientEmail = process.env.FIREBASE_CLIENT_EMAIL;
  // A chave privada vem com "\n" literais nas variáveis de ambiente;
  // aqui convertemos de volta para quebras de linha reais.
  const privateKey = (process.env.FIREBASE_PRIVATE_KEY || '').replace(/\\n/g, '\n');

  if (!projectId || !clientEmail || !privateKey) {
    throw new Error(
      'Credenciais do Firebase ausentes. Defina FIREBASE_PROJECT_ID, ' +
      'FIREBASE_CLIENT_EMAIL e FIREBASE_PRIVATE_KEY.'
    );
  }

  admin.initializeApp({
    credential: admin.credential.cert({ projectId, clientEmail, privateKey }),
  });
  initialized = true;
}

function getDb() {
  initApp();
  return admin.firestore();
}

module.exports = { getDb, admin };
