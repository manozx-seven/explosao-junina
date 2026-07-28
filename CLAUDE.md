# CLAUDE.md — Regras fixas deste projeto

> Este arquivo é lido automaticamente pelo Claude Code no início de cada sessão.
> As instruções abaixo são permanentes.

## ⚑ Tarefa fixa (fazer SEMPRE, no começo de toda sessão)

1. **Leia `CONTEXTO.md`** para entender o que é o sistema, a arquitetura e as
   regras de negócio.
2. **Leia `ATUALIZACOES.md`** para saber tudo o que já foi feito, do mais recente
   ao mais antigo.
3. **Leia `PENDENCIAS.md`** para saber o que está em aberto — no sistema, no site
   do Sócio Torcedor, nos documentos e nas decisões da coordenação.

Faça isso **antes** de responder qualquer pedido sobre o projeto, para trabalhar
com o contexto completo.

**Projeto irmão:** o *Site Sócio Torcedor* é um repositório separado
(`manozx-seven/explosao-socio-torcedor`), com a mesma stack. Os **documentos**
dele (Plano de Implementação e material de divulgação) vivem **aqui**, em
`documentos explosão/` — são a especificação de produto daquele site. Mudança de
regra num dos lados quase sempre precisa refletir no outro.

## ⚑ Tarefa fixa (fazer SEMPRE, ao alterar o projeto)

Sempre que fizer **qualquer modificação** neste projeto (código, config, infra,
deploy — qualquer coisa), **registre no `ATUALIZACOES.md`** e, se o item estava
listado em `PENDENCIAS.md`, **risque-o de lá**:
- adicione uma entrada com a **data**, um **título** curto e **o que mudou / por quê**;
- agrupe sob a data corrente (a mais recente fica no topo do arquivo);
- se a mudança alterar a arquitetura ou as regras do sistema, atualize também
  o `CONTEXTO.md`.

**Ao criar um handler novo:** ele precisa entrar em `FUNCOES` no
`netlify/functions/api.js` com **escopo e aridade**. Sem isso ele não responde —
falha fechada, que é o comportamento desejado.

## Resumo rápido (para contexto imediato)

Sistema web de avaliação da **Explosão Junina de Beruri**: cadastro de brincantes,
ensaios, avaliações (presença + nota), ranking e simulação de bonificação.

- **Arquitetura:** frontend estático `public/index.html` → Netlify Function
  `netlify/functions/api.js` → `server/handlers.js` → **Firebase Firestore**
  (via firebase-admin com `preferRest: true`).
- **Deploy:** push na `main` do GitHub (`manozx-seven/explosao-junina`) redeploya
  o Netlify (`explosao` → https://explosao.netlify.app). Firebase project
  `explosao-junina`.
- **Acesso admin de teste:** `DEV` / `123456`.
- **Dev local:** `netlify dev --offline` → http://localhost:8888
  (usa `.env`; rede do TJAM precisa do REST do Firestore).
- **Segredos:** `.env` e `serviceAccountKey.json` são gitignored — nunca commitar.

Detalhes completos em `CONTEXTO.md`.
