# PENDÊNCIAS — Explosão Junina de Beruri

> Tudo que está em aberto: no sistema, no site do Sócio Torcedor, nos documentos e
> nas decisões da coordenação. O que já foi feito está no `ATUALIZACOES.md`;
> o que o sistema é está no `CONTEXTO.md`.
>
> **Última revisão:** 2026-07-27.

---

## 1. Sistema de Avaliação (este repositório)

### Configuração da temporada (fazer antes de fevereiro/2027)
- [ ] Conferir a **config viva no Firestore** (`config/app`): se ainda estiver em 2026,
      ajustar pela aba **Configurações** — `temporada`, `inicioTemporada`,
      `inicioContagem`, `fimContagem`, `fimAdesao`. Os padrões do código já estão em 2027,
      mas o banco manda.
- [ ] Definir e preencher os campos de pagamento da bonificação: `dataPagamentoBonif`
      (após o Festival), `dataPagamentoBonif2` (2ª parcela, opcional) e
      `obsPagamentoBonif`.
- [ ] Manter `escolhaDestinoLiberada` **bloqueada** até a contagem fechar (pós-Festival);
      só então o brincante escolhe resgatar ou doar.
- [ ] Revisar os valores por tipo de evento (`valorEnsaio`, `valorApresentacao`,
      `valorFestival`) — com o novo modelo de custeio, a bonificação pode subir.

### Segurança e acesso
- [ ] **Token de sessão assinado no servidor.** Hoje as funções de escrita recebem o
      objeto `usuario` vindo do cliente (herança do Apps Script). A verificação de login
      é no servidor, mas a evolução natural é emitir token no login.
- [ ] **Remover o usuário `DEV`** quando houver um admin real cadastrado.
- [ ] Sessão ainda é só do lado do cliente (localStorage, expira em 1h sem atividade).

### Funcionalidades adiadas
- [ ] **Programa de Fidelidade** (níveis por temporada, ex.: 0,50 / 0,75 / 1,00) — só
      faz sentido a partir de quem completou uma temporada inteira.
- [ ] **Checklist de resgate da bonificação** (figurino devolvido, permanência até o
      Festival, pendências quitadas) antes de liberar o pagamento.
- [ ] **Compartilhar desempenho** — gerar texto de WhatsApp, PDF ou imagem do perfil do
      brincante. Pedido e adiado.
- [ ] **Valores diferenciados para itens** (marcador, casal de noivos, casal real). Hoje
      só a frequência é diferente (85%).

---

## 2. Site do Sócio Torcedor (projeto irmão)

Pasta: `C:\Users\murylo.neves\Desktop\Explosão - Site Sócio Torcedor` — **projeto
separado**, com a mesma stack (front estático + Netlify Functions + Firebase).

- [ ] **Não está no Git.** Criar repositório próprio (não misturar com este).
- [ ] **Não está publicado.** Criar site próprio no Netlify.
- [ ] **Projeto Firebase próprio** (separado de `explosao-junina`) e variáveis de
      ambiente no painel.
- [x] **M1** — login da coordenação, CRUD de sócios (fogueira/bandeirinha/estrela),
      registro e confirmação de pagamentos (Pix/dinheiro) com data e hora **reais**
      separadas da confirmação. Feito, e com o tema visual de arraial (14/07/2026).
- [ ] **M2** — painel do sócio (login próprio): minhas contribuições + finanças da
      quadrilha.
- [ ] **M3** — troféus e conquistas (em dia até o dia 5, sequência, temporada completa,
      padrinho, veterano).
- [ ] **M4** — página pública, adesão online e carteirinha digital.
- [ ] **Futuro** — pagamento automático (cobrança recorrente / confirmação de Pix).

---

## 3. Implementações previstas nos documentos de 2027

Foram descritas nos planos de evento e ainda **não existem**:

- [ ] **Votação popular em tempo real do Arraial da Explosão** — cadastro dos grupos e
      da ordem de apresentação, votação por QR code (sem app), janela de votação por
      grupo/categoria, um voto por dispositivo, painel ao vivo para projetar no telão,
      resultado imediato e relatório final. **Precisa de plano B offline** (rede local
      ou cédula impressa).
- [ ] **Certificados de participação** gerados automaticamente para as danças convidadas.
- [ ] **Registro de venda de camisa e produtos** — pedidos, tamanho, forma de pagamento,
      controle de estoque (usado no Arraial de Lançamento e o ano todo).
- [ ] **Painel público de transparência** — página aberta com o balanço da temporada,
      alimentada pelos registros financeiros (dois níveis: recurso público detalhado,
      arrecadação própria só o total).
- [ ] **Sorteio digital** — entre o público presente e entre os sócios em dia, com
      registro do resultado.

---

## 4. Documentos (`documentos explosão/`)

Os `.docx` são **gerados por script** em `documentos explosão/_geradores/`
(`kit.py` + um `gen_*.py` por documento). Editar o gerador e rodar de novo —
nunca editar o `.docx` na mão.

- [ ] **Confirmar o tema anterior.** O plano de reestruturação trata
      *"A Bolha do Amor"* como **tema anterior** (usa a expressão "tema anterior", sem
      citar ano). Se for o tema de 2027, o capítulo de diagnóstico precisa ser reescrito.
- [ ] **Limpar o `Organograma - Explosão Junina.docx`.** O arquivo começa com um
      parágrafo solto de conversa (sobra de copiar/colar de chat) e não segue o padrão
      visual dos outros documentos.
- [ ] **Kit Parceiro** — atualizar para o novo papel das parcerias: sustentar o Programa
      Sócio Torcedor (descontos, prêmios de sorteio, brindes) e gerar ações para o
      público geral.
- [ ] **Programa Sócio Torcedor (divulgação)** — alinhar valores e benefícios ao plano de
      implementação depois que a Diretoria bater o martelo.
- [ ] **Contrato do brincante** — revisar antes da assinatura prevista para fevereiro de
      2027 (datas da temporada, prazos de adesão e ativação).
- [ ] Documentos sem gerador (editados à mão, via `python-docx` avulso): Contratos,
      Kit Parceiro, Programa Sócio Torcedor (divulgação) e Organograma. Migrar para o
      kit quando forem revisados.

---

## 5. Decisões da coordenação (não dependem de código)

- [ ] **Nomear as pessoas** de cada cargo da Diretoria e cada Grupo de Produção do
      organograma (reunião prevista para agosto de 2026).
- [ ] **Escolher o tema de 2027** (previsão: outubro de 2026) e fechar o *documento do
      tema* — sinopse, atos, paleta, referências, o que é surpresa.
- [ ] **Definir a data do Arraial de Lançamento** (previsão: março de 2027).
- [ ] **Definir a data do Arraial da Explosão** (agosto de 2027 ou mais para o fim do ano).
- [ ] **Fechar valores e benefícios do Sócio Torcedor** e definir o **Pix oficial** do
      programa.
- [ ] **Definir no Arraial da Explosão** se as danças de fora competem, competem em
      categoria própria ou participam fora de competição.
- [ ] **Definir a condição das bancas** do Arraial (gratuito, taxa simbólica ou
      contrapartida).
- [ ] **Meta de sócios por brincante** para a captação da temporada.
