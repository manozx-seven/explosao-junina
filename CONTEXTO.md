# CONTEXTO — Sistema de Avaliação · Explosão Junina de Beruri

> Documento de contexto do projeto. Descreve **o que é** o sistema, sua
> arquitetura, regras de negócio e infraestrutura. Deve ser lido no início de
> cada sessão de trabalho (ver `CLAUDE.md`). Mudanças de rumo vão aqui;
> o histórico do que foi feito vai em `ATUALIZACOES.md`.

---

## 1. O que é

Sistema web para a **coordenação da Explosão Junina de Beruri (Grupo Recreativo e
Folclórico)** gerenciar a temporada: cadastro de brincantes, registro de ensaios
e apresentações, avaliação de presença e nota por ensaio, ranking de desempenho,
e simulação do **Programa de Bonificação** (pagamento por participação).

Público:
- **Coordenação (admin):** acesso total — cadastra pessoas, cria ensaios, avalia,
  vê dashboard, ranking, bonificação e logs.
- **Brincante:** vê o próprio perfil (presença, notas, bonificação acumulada) e o
  ranking.

## 2. Origem

Nasceu como um app **Google Apps Script** (web app `HtmlService` + dados em
Google Sheets). Foi **migrado** para uma arquitetura moderna hospedada
(GitHub + Netlify + Firebase). O código original está preservado em `legacy/`
apenas para referência.

- Apps Script original (scriptId): `1oqOFytxpuOxNF3LS4YXjUFnXHxhaoXziJ9AvEHY0ZULGqjGFEsyD4Ee2`
  (pertence à conta pessoal `murylo.neves@gmail.com`).
- Planilha de dados legada (Google Sheets): `1tlc6BH5MM-KzwRdoZweWWgxqlfRyNXbCVQMT5eD5d2w`.
- A migração começou **do zero** no Firebase (os dados da planilha não foram importados).

## 3. Arquitetura

```
Navegador (public/index.html)
      │  fetch POST /.netlify/functions/api  { fn, args }
      ▼
Netlify Function (netlify/functions/api.js)   ← dispatcher com whitelist
      │  chama handlers[fn](...args)
      ▼
server/handlers.js  ← lógica de negócio
      │  firebase-admin (transporte REST)
      ▼
Firebase Firestore  ← banco de dados
```

- **Frontend:** SPA em um único arquivo estático `public/index.html`
  (HTML + CSS + JS inline). Fala com o backend **somente** pela função
  `srv(fn, ...args)`, que faz `fetch` para a Netlify Function. (No Apps Script
  original, isso era `google.script.run`.)
- **Backend:** funções serverless Node.js no Netlify. Ponto único de entrada em
  `netlify/functions/api.js`, que recebe `{ fn, args }`, valida contra uma
  whitelist e despacha para `server/handlers.js`.
- **Banco:** Firebase Firestore, acessado via **firebase-admin** com
  `preferRest: true` (transporte REST em vez de gRPC — necessário para rodar
  atrás do proxy TLS corporativo do TJAM e recomendado em serverless).

## 4. Stack e dependências

- Node.js, `firebase-admin` (^12) — banco.
- Netlify (hospedagem estática + functions), `netlify-cli` para deploy/dev.
- `lucide` (CDN) — biblioteca de ícones do frontend.
- Fontes Google: Barlow / Barlow Condensed.
- `dotenv` — carrega `.env` nos scripts locais.

## 5. Modelo de dados (Firestore)

| Coleção      | Doc ID              | Campos |
|--------------|---------------------|--------|
| `config`     | `app`               | mapa de configurações (valores, temporada, datas) |
| `counters`   | `brincantes`        | `{ seq }` — sequência para gerar IDs `EXP2026xx` |
| `brincantes` | o próprio ID (ex. `EXP202601`, `DEV`) | ID, Nome, Apelido, CPF, Fila, Posicao, Tipo, DataAdesao, OptBonificacao, StatusAtivacao, QualificacaoExtra |
| `ensaios`    | ex. `ENS20260210_1234` | ID, Data, Tipo, Descricao, CriadoPor |
| `avaliacoes` | auto                | EnsaioID, BrincanteID, Presente, Nota, Observacao, AvaliadoPor, DataRegistro |
| `logs`       | auto                | DataHora, UsuarioID, UsuarioNome, Acao, Detalhes |

Config padrão (chaves em `config/app`): `valorEnsaio=0.50`, `valorApresentacao=1.00`,
`valorFestival=5.00`, `mesesAtivacao=3`, `frequenciaMinima=75`, `notaMinima=4`,
`percentualNotaMinima=75`, `temporada=2026`, `inicioTemporada=2026-02-01`,
`fimContagem=2026-07-31`, `fimAdesao=2026-04-30`.

## 6. Regras de negócio

- **Login:** ID + CPF conferidos no servidor contra a coleção `brincantes`
  (o CPF é normalizado para 11 dígitos dos dois lados). `Tipo = coordenacao`
  entra como **admin**; os demais como **brincante**.
- **IDs de brincante:** `EXP` + temporada + sequência (contador transacional em
  `counters/brincantes`). Ex.: `EXP202601`.
- **Tipos de ensaio:** `regular`, `ensaiao`, `apresentacao`, `festival`, `igreja`.
- **Bonificação** (só conta se `OptBonificacao = sim` **e** `StatusAtivacao = ativado`):
  - festival → `valorFestival` (5,00)
  - apresentacao → `valorApresentacao` (1,00)
  - demais ensaios → `valorEnsaio` (0,50)
  - **igreja → não gera bonificação**
- **Ativação** (metas para o brincante ativar a bonificação): presença ≥ 75% e
  nota ≥ 4 em pelo menos 75% dos ensaios, dentro do período de ativação
  (`mesesAtivacao` = 3). Há também uma **Qualificação Extra** manual
  (aprovado/reprovado) avaliada pela coordenação.
- **Adesão à bonificação:** só permitida até `fimAdesao`.

## 7. Autenticação e usuário DEV

- Não há tela de "trocar senha": a senha de cada pessoa **é o CPF**; muda-se
  editando o campo `CPF` do brincante.
- **Usuário DEV** (acesso admin sem dados pessoais reais): `ID = DEV`,
  senha = `123456`. Criado por `scripts/seed-dev.js`. Serve para administrar e
  cadastrar as pessoas reais; pode ser removido quando houver um admin real.
- Observação de segurança: as funções de escrita ainda recebem o objeto `usuario`
  vindo do cliente (herdado do Apps Script). A verificação de login é no servidor,
  então CPFs não vazam ao navegador. Evolução futura: emitir token de sessão
  assinado no login.

## 8. Estrutura de pastas

```
public/index.html          Frontend completo (UI + lógica de tela)
netlify/functions/api.js   Dispatcher da API (Netlify Function)
server/firebase.js         Init do firebase-admin (REST) via variáveis de ambiente
server/handlers.js         Lógica de negócio (Firestore) — ~18 funções
scripts/seed.js            Cria config inicial + coordenação real (por CPF)
scripts/seed-dev.js        Cria/atualiza o usuário DEV (admin)
scripts/gen-env.js         Gera .env a partir do serviceAccountKey.json
legacy/                    Código.js e Index.html originais (Apps Script)
CONTEXTO.md                Este arquivo
ATUALIZACOES.md            Histórico de mudanças
CLAUDE.md                  Regras fixas da sessão (lidas automaticamente)
netlify.toml               Build do Netlify (publish=public, functions dir, preferRest)
.env / .env.example        Credenciais do Firebase (o .env real é gitignored)
```

## 9. Infraestrutura / contas

- **GitHub:** https://github.com/manozx-seven/explosao-junina (branch `main`).
  Auth via conta `manozx-seven` (o commit fica como `manozx-seven`).
- **Netlify:** projeto `explosao` — https://explosao.netlify.app
  (site id `b347dc17-5886-4c66-a51e-3e74c9bb4e38`, conta "Seven Solution").
  Deploy automático a cada push na `main`. Variáveis de ambiente configuradas
  no painel: `FIREBASE_PROJECT_ID`, `FIREBASE_CLIENT_EMAIL`, `FIREBASE_PRIVATE_KEY`.
- **Firebase:** projeto `explosao-junina`, Firestore região `southamerica-east1`.
  Conta de serviço: `firebase-adminsdk-fbsvc@explosao-junina.iam.gserviceaccount.com`.

## 10. Desenvolvimento local

```bash
npm install                      # dependências
node scripts/gen-env.js          # gera .env a partir do serviceAccountKey.json
node scripts/seed-dev.js         # cria config + usuário DEV (123456)
netlify dev --offline            # sobe site + função + .env em http://localhost:8888
```

Notas:
- Rede corporativa do TJAM intercepta TLS → o `preferRest` do Firestore contorna
  isso. Na nuvem (Netlify) não há esse proxy.
- `netlify dev` sem `--offline` exige login do Netlify na sessão; use `--offline`
  para testar sem autenticar.
- **Segredos nunca vão pro Git:** `.env` e `serviceAccountKey.json` estão no
  `.gitignore`.
