# Explosão Junina – Sistema de Avaliação

Sistema web de gestão de brincantes, ensaios, avaliações, ranking e bonificação
da Explosão Junina de Beruri.

Originalmente construído em **Google Apps Script + Google Sheets**, foi migrado para:

- **Frontend:** site estático (`public/index.html`) hospedado no **Netlify**
- **Backend:** **Netlify Functions** (serverless, Node.js) em `netlify/functions/api.js`
- **Banco de dados:** **Firebase Firestore**

---

## Arquitetura

```
Navegador (public/index.html)
      │  fetch POST /.netlify/functions/api  { fn, args }
      ▼
Netlify Function (netlify/functions/api.js)   ← dispatcher com whitelist
      │  chama handlers[fn](...args)
      ▼
server/handlers.js  ← lógica de negócio (login, brincantes, ensaios, ...)
      │  firebase-admin
      ▼
Firebase Firestore  ← coleções: brincantes, ensaios, avaliacoes, logs, config
```

O frontend conversa com o backend por **uma única função** `srv(fn, ...args)`,
que substitui o antigo `google.script.run`. Nada mais precisou mudar na interface.

### Coleções no Firestore

| Coleção      | Doc ID              | Campos principais |
|--------------|---------------------|-------------------|
| `config`     | `app`               | mapa de configurações (valores, temporada, datas) |
| `counters`   | `brincantes`        | `{ seq }` — sequência para gerar IDs `EXP2026xx` |
| `brincantes` | `EXP202601`, ...    | ID, Nome, Apelido, CPF, Fila, Posicao, Tipo, DataAdesao, OptBonificacao, StatusAtivacao, QualificacaoExtra |
| `ensaios`    | `ENS20260210_1234`  | ID, Data, Tipo, Descricao, CriadoPor |
| `avaliacoes` | auto                | EnsaioID, BrincanteID, Presente, Nota, Observacao, AvaliadoPor, DataRegistro |
| `logs`       | auto                | DataHora, UsuarioID, UsuarioNome, Acao, Detalhes |

---

## Passo a passo de implantação

### 1. Firebase (banco de dados)

1. Acesse <https://console.firebase.google.com> e crie um projeto (ou use um existente).
2. No menu **Build → Firestore Database → Criar banco de dados**.
   - Escolha o modo **Produção** e uma região (ex: `southamerica-east1`).
   - Como todo acesso é feito pelo backend (Admin SDK), as *Security Rules*
     podem ficar totalmente fechadas — o Admin SDK as ignora. Deixe o padrão de produção.
3. Gere as credenciais de serviço:
   **⚙️ Configurações do projeto → Contas de serviço → Gerar nova chave privada**.
   Um arquivo JSON será baixado. Dele você vai usar 3 valores:
   - `project_id`   → `FIREBASE_PROJECT_ID`
   - `client_email` → `FIREBASE_CLIENT_EMAIL`
   - `private_key`  → `FIREBASE_PRIVATE_KEY`

### 2. Rodar e semear localmente (opcional, mas recomendado)

1. Instale as dependências:
   ```bash
   npm install
   ```
2. Crie o arquivo `.env` a partir do exemplo e preencha com os valores do JSON:
   ```bash
   cp .env.example .env
   ```
   > A `FIREBASE_PRIVATE_KEY` deve ficar **entre aspas**, em uma única linha,
   > com os `\n` literais (exatamente como aparece no JSON).
3. Crie a configuração inicial e o **primeiro usuário de coordenação**:
   ```bash
   npm run seed -- "05165322270" "Coordenação Geral"
   ```
   O comando imprime o **ID de login** gerado (ex: `EXP202601`) e a **senha (CPF)**.
   Guarde esses dados — é com eles que você entra como admin.
4. (Opcional) Rode o site inteiro localmente com o Netlify CLI:
   ```bash
   npm install -g netlify-cli
   netlify dev
   ```
   Abra <http://localhost:8888>.

### 3. GitHub (versionamento)

```bash
git init
git add .
git commit -m "Migração para Netlify + Firebase"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/<seu-repo>.git
git push -u origin main
```

> O `.gitignore` já exclui `node_modules/`, `.env` e a chave de serviço.
> **Nunca** faça commit do `.env` nem do JSON de credenciais.

### 4. Netlify (hospedagem)

1. Acesse <https://app.netlify.com> → **Add new site → Import an existing project**.
2. Conecte a conta do **GitHub** e selecione o repositório.
3. Configurações de build (o `netlify.toml` já define, confirme):
   - **Build command:** *(vazio)*
   - **Publish directory:** `public`
   - **Functions directory:** `netlify/functions`
4. Em **Site settings → Environment variables**, adicione as 3 variáveis:
   - `FIREBASE_PROJECT_ID`
   - `FIREBASE_CLIENT_EMAIL`
   - `FIREBASE_PRIVATE_KEY`  (cole o valor entre aspas, com os `\n`)
5. **Deploy**. Ao terminar, o site fica no ar em `https://<seu-site>.netlify.app`.
6. Se ainda **não** rodou o `seed` localmente, rode agora (com o `.env` preenchido)
   para criar o primeiro admin — o seed grava direto no Firestore, então funciona
   de qualquer máquina.

---

## Login

- **ID** (ex: `EXP202601`) + **CPF** (somente números) funcionam como usuário e senha.
- Usuários com `Tipo = coordenacao` entram como **admin**; os demais como **brincante**.

---

## Estrutura de pastas

```
public/index.html          Frontend (interface completa)
netlify/functions/api.js   Dispatcher da API (Netlify Function)
server/firebase.js         Inicialização do firebase-admin
server/handlers.js         Lógica de negócio (Firestore)
scripts/seed.js            Cria config inicial + primeiro admin
legacy/                    Código.js e Index.html originais (Apps Script)
netlify.toml               Configuração de build do Netlify
.env.example               Modelo das variáveis de ambiente
```

---

## Nota de segurança

O modelo de login (ID + CPF) foi mantido igual ao original para preservar a
experiência dos brincantes. A verificação acontece **no servidor** (Netlify
Function + Admin SDK), então os CPFs **não** ficam expostos ao navegador.

As funções de escrita ainda recebem o objeto `usuario` vindo do cliente (como no
Apps Script original) — isso é suficiente para o uso atual, mas para um controle
de acesso mais forte o próximo passo seria emitir um token de sessão assinado no
`login` e validá-lo no backend. Fica registrado como melhoria futura.
