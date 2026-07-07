# CLAUDE.md — Regras fixas deste projeto

> Este arquivo é lido automaticamente pelo Claude Code no início de cada sessão.
> As instruções abaixo são permanentes.

## ⚑ Tarefa fixa (fazer SEMPRE, no começo de toda sessão)

1. **Leia `CONTEXTO.md`** para entender o que é o sistema, a arquitetura e as
   regras de negócio.
2. **Leia `ATUALIZACOES.md`** para saber tudo o que já foi feito, do mais recente
   ao mais antigo.

Faça isso **antes** de responder qualquer pedido sobre o projeto, para trabalhar
com o contexto completo.

## ⚑ Tarefa fixa (fazer SEMPRE, ao alterar o projeto)

Sempre que fizer **qualquer modificação** neste projeto (código, config, infra,
deploy — qualquer coisa), **registre no `ATUALIZACOES.md`**:
- adicione uma entrada com a **data**, um **título** curto e **o que mudou / por quê**;
- agrupe sob a data corrente (a mais recente fica no topo do arquivo);
- se a mudança alterar a arquitetura ou as regras do sistema, atualize também
  o `CONTEXTO.md`.

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
