# ATUALIZAÇÕES — Sistema de Avaliação · Explosão Junina

> Histórico de tudo que foi feito no projeto, do mais recente para o mais antigo.
> **Regra fixa:** toda modificação no projeto deve ser registrada aqui (ver `CLAUDE.md`).
> Formato de cada entrada: data, título e o que mudou / por quê.

---

## 2026-07-07 — Migração completa + redesign

Toda a fundação do projeto foi construída neste dia. Em ordem cronológica:

### Migração de arquitetura (Apps Script → Netlify + Firebase)
- Clonado o projeto Apps Script original com `clasp` (arquivos em `legacy/`).
- Backend portado de Google Sheets para **Firebase Firestore**:
  `server/handlers.js` (~18 funções: login, brincantes, ensaios, avaliações,
  ranking, bonificação, logs, config) e `server/firebase.js` (init do
  firebase-admin).
- Criado o dispatcher serverless `netlify/functions/api.js` (recebe `{fn,args}`,
  valida contra whitelist, chama o handler).
- Frontend `public/index.html`: a função `srv()` deixou de usar
  `google.script.run` e passou a fazer `fetch` para a Netlify Function.
  Restante da UI preservado.
- Adicionados `netlify.toml`, `package.json`, `.gitignore`, `.env.example`, `README.md`.
- Originais preservados em `legacy/` (Código.js, Index.html, appsscript.json).

### Firestore via REST (preferRest)
- `server/firebase.js` passou a usar `db.settings({ preferRest: true })`.
  Motivo: o gRPC falhava com `SELF_SIGNED_CERT_IN_CHAIN` na rede corporativa do
  TJAM (proxy que intercepta TLS). REST contorna isso e é recomendado em serverless.
- Criado `scripts/gen-env.js` (gera `.env` a partir do `serviceAccountKey.json`).

### Banco e primeiro acesso
- Firebase project `explosao-junina` + Firestore (`southamerica-east1`).
- `scripts/seed.js` (config inicial + coordenação por CPF) e
  `scripts/seed-dev.js` (usuário **DEV / 123456**, admin sem dados reais).
- Config padrão gravada em `config/app`; usuário DEV criado e login validado.

### GitHub e Netlify
- Repositório https://github.com/manozx-seven/explosao-junina (branch `main`).
- Site Netlify `explosao` (https://explosao.netlify.app) ligado ao repo, com
  deploy automático a cada push.
- Variáveis `FIREBASE_PROJECT_ID`, `FIREBASE_CLIENT_EMAIL`, `FIREBASE_PRIVATE_KEY`
  importadas via `netlify env:import .env` e deploy de produção realizado.

### Correções de login
- A tela exigia CPF com **exatamente 11 dígitos**, o que impedia o login DEV
  (6 dígitos). Passou a aceitar senha com **mínimo de 4 dígitos**.
- A mensagem genérica "Erro ao conectar" foi trocada pelo **erro real do servidor**.
- Adicionado favicon SVG (chama), removendo o 404 de `/favicon.ico`.

### Redesign visual (identidade Explosão Junina + ícones profissionais)
- **Removidos todos os emojis** (👁 🔒 ✓ ✗ × ⏳ 🎆).
- Adotada a biblioteca de ícones **Lucide** (via CDN) em menus, botões, presença,
  perfil, toasts e favicon.
- Identidade junina: **bandeirinhas (bunting SVG)** no login e na topbar, brasão
  com ícone de chama, tipografia de cartaz (Barlow Condensed), paleta de arraiá
  noturno refinada, cards/badges/nav repaginados.

### Performance de navegação (sistema ágil)
- **Cache em memória por tela** (`_cache`): ao voltar a uma aba já visitada, ela
  renderiza instantaneamente; os dados são revalidados em segundo plano.
- Removido o **overlay bloqueante** da navegação; primeira carga usa **skeletons**.
- Exclusões (brincante/ensaio) atualizam a lista na hora (otimista).
- Funções de render separadas das de load para permitir render a partir do cache.
