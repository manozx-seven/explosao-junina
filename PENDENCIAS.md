# PENDÊNCIAS — Explosão Junina de Beruri

> Tudo que está em aberto: no sistema, no site do Sócio Torcedor, nos documentos e
> nas decisões da coordenação. O que já foi feito está no `ATUALIZACOES.md`;
> o que o sistema é está no `CONTEXTO.md`.
>
> **Última revisão:** 2026-07-29.
>
> **Decisões de 27/07/2026 são a referência.** Onde um documento anterior conflitar
> com elas, o documento é que muda. Nos dois pontos em que o próprio 27/07 se
> contradiz, valem: temporada do Sócio Torcedor de **10 meses** (fev–nov) e
> **2027 como primeira temporada**.

---

## ▶ Onde parei em 29/07/2026 (fim do dia)

Tudo commitado e no ar (`d2ee6e1` na `main`; o push redeploya o Netlify). Nada
ficou pela metade. **Máquina nova:** `git pull` → `npm install` → `npm test`
(63 asserções). Para mexer nos documentos, `pip install python-docx` e rodar o
gerador dentro de `documentos explosão/_geradores/`.

A última coisa feita no dia foi visual: o **logo oficial da quadrilha** entrou no
favicon, na tela de login e no topo do app, no lugar do ícone de chama. As
imagens estão em `public/img/` e o original em `arte/`.

**O que fazer primeiro, na ordem:**

1. **Conferir a config viva na aba Configurações.** É o único ponto em que o
   banco pode divergir do código: `temporada` ainda estava em **2026** e o
   `tetoBonificacao` (R$ 80) acabou de nascer. Sem isso, a bonificação da
   temporada inteira calcula errado. Ver §1.
2. **Reunião da Diretoria (prevista para agosto/2026).** É o próximo passo real
   do projeto, e não é código. Leva: nomes do organograma (§5), valores e teto
   da bonificação, valores do Sócio Torcedor e a **chave Pix oficial** do
   programa, e a condição das bancas do Arraial.
3. **Ofício de parceria à Prefeitura** para o Arraial da Explosão. O cronograma
   do evento coloca isso em D-90 e é o que define o tamanho do evento — quanto
   antes protocolar, maior a chance de entrar no orçamento do município.
4. **Site do Sócio Torcedor:** faltam ranking da temporada e notificações
   (§2). O resto do M3 está pronto e o site está no ar.

**Não esquecer:** o `_backup/` dos `.docx` é local e gitignored — em outra
máquina ele não existe. Os documentos atuais e os geradores estão todos
versionados, então dá para regerar tudo; só não dá para voltar ao anterior.
No repositório do **Sócio Torcedor** ficou um arquivo não versionado
(`ATUALIZACOES-sessao-2026-07-29.md`) que não viaja no clone.

---

## 1. Sistema de Avaliação (este repositório)

### Configuração da temporada (fazer antes de fevereiro/2027)
- [ ] **Confirmado em 28/07/2026: a config viva ainda está em `temporada=2026`.**
      Ajustar pela aba **Configurações** — `temporada`, `inicioTemporada`,
      `inicioContagem`, `fimContagem`, `fimAdesao`. Os padrões do código já estão em 2027,
      mas o banco manda.
- [ ] Definir a **meta de sócios por brincante** (`metaSociosPorBrincante`, hoje no
      padrão 2) junto com a decisão da coordenação sobre a captação da temporada.
- [ ] Definir e preencher os campos de pagamento da bonificação: `dataPagamentoBonif`
      (após o Festival), `dataPagamentoBonif2` (2ª parcela, opcional) e
      `obsPagamentoBonif`.
- [ ] Manter `escolhaDestinoLiberada` **bloqueada** até a contagem fechar (pós-Festival);
      só então o brincante escolhe resgatar ou doar.
- [ ] Revisar os valores por tipo de evento (`valorEnsaio`, `valorApresentacao`,
      `valorFestival`) — com o novo modelo de custeio, a bonificação pode subir.
      **Agora há teto:** `tetoBonificacao` (padrão R$ 80,00, feito em 29/07/2026)
      limita o acumulado por brincante, então mexer nos valores não estoura mais o
      orçamento. Confirmar o teto na reunião da Diretoria junto com os valores.
- [ ] **Conferir se a config viva tem `tetoBonificacao`.** O padrão do código é
      `80.00`, mas o banco manda: se `config/app` já existir sem a chave, o valor
      padrão vale; se alguém salvar a tela de Configurações com o campo vazio, o
      teto é desligado. Checar pela aba Configurações antes da temporada.

### Segurança e acesso
- [x] **Token de sessão no servidor** — feito em 27/07/2026. Coleção `sessoes`,
      escopos por função e o ID do usuário lido da sessão. Detalhes em
      `ATUALIZACOES.md`.
- [ ] **Remover o usuário `DEV`** (senha `123456`, admin total) quando houver um admin
      real cadastrado. **É a porta aberta que sobrou** depois da correção da API.
- [ ] **Rate limit no login.** Não há limite de tentativas: o login é ID + CPF, e numa
      cidade pequena o CPF de alguém não é segredo. Mesma pendência existe no projeto
      irmão — vale resolver com o mesmo desenho (coleção `tentativas_login`).
- [ ] **Revisar escopo ao criar cada handler novo** (`FUNCOES` em
      `netlify/functions/api.js`). Sem entrada lá, a função não responde.

### Funcionalidades adiadas
- [ ] **Programa de Fidelidade** (níveis por temporada, ex.: 0,50 / 0,75 / 1,00) — só
      faz sentido a partir de quem completou uma temporada inteira.
- [ ] **Checklist de resgate da bonificação** (figurino devolvido, permanência até o
      Festival, pendências quitadas) antes de liberar o pagamento.
- [ ] **Compartilhar desempenho** — gerar texto de WhatsApp, PDF ou imagem do perfil do
      brincante. Pedido e adiado.
- [ ] **Valores diferenciados para itens** (marcador, casal de noivos, casal real). Hoje
      só a frequência é diferente (85%).
- [ ] **Repetição na tela de login** (cosmético, 29/07/2026): o logo já traz o nome da
      quadrilha escrito e, logo abaixo, o `<h2>` repete "EXPLOSÃO JUNINA". Dá para
      enxugar o bloco de títulos — não foi feito porque o pedido era só trocar a imagem.

---

## 2. Site do Sócio Torcedor (projeto irmão)

**Projeto separado**, com a mesma stack (front estático + Netlify Functions +
Firebase). Repositório: <https://github.com/manozx-seven/explosao-socio-torcedor>.
O que está em aberto lá é rastreado no `PROXIMOS-PASSOS.md` **daquele repositório** —
aqui fica só o que cruza com este sistema.

Os **documentos** do programa (`Programa Socio Torcedor - Plano de Implementacao.docx`
e o material de divulgação) vivem **neste** repositório, em `documentos explosão/` —
são a especificação de produto daquele site. Mudança de regra num lado precisa
refletir no outro.

- [x] **M1** — login da coordenação, CRUD de sócios (fogueira/bandeirinha/estrela),
      registro e confirmação de pagamentos (Pix/dinheiro) com data e hora **reais**
      separadas da confirmação. Feito, com tema visual de arraial (14/07/2026).
- [x] **Repositório próprio publicado** (27/07/2026).
- [x] **M2 e M3 desenhados** (27/07/2026) — `ARQUITETURA-M2.md` e `ARQUITETURA-M3.md`
      no repositório do Sócio Torcedor.
- [x] **M2 etapa 1** — sessão por token e escopos na API (27/07/2026). Foi de lá que
      veio a correção aplicada neste sistema.
- [x] **M2 — painel do sócio** (28/07/2026): login do sócio, carteirinha digital,
      situação do mês, progresso, histórico, troca de nível, mural, finanças e, do
      lado da coordenação, regras, fila de confirmação, lembretes e importação por
      planilha.
- [x] **Site no ar com o banco de verdade** (29/07/2026) — projeto Firebase próprio e
      site no Netlify: <https://explosao-socio-torcedor.netlify.app>.
- [ ] **Comprovante de pagamento por imagem** (resto do M2) — depende de conta e
      credenciais externas ainda não provisionadas. Hoje o sócio descreve o
      pagamento por texto e a coordenação confirma.
- [ ] **M3 em andamento**: troféus (todas as dez conquistas), **sorteios** e o
      **módulo de missões** (pontos retidos, validação em lote, prova por link ou
      texto) já estão prontos. Faltam **ranking da temporada no mural** e as
      **notificações** (a mensagem pronta para WhatsApp é a de melhor retorno).
- [ ] **M4** — página pública e adesão online.

### Cruzamentos com este sistema (decididos em 27/07/2026)
- [x] **Módulo de missões neste sistema** para a captação de sócios — feito em
      28/07/2026. Coleção `indicacoes`, aba **Sócios** para a coordenação, card
      "Missão: traga a torcida" no perfil do brincante, troféu Padrinho e a config
      `metaSociosPorBrincante`. Guarda **nome e telefone apenas**; vale desempenho
      e troféu, sem dinheiro. Detalhes em `ATUALIZACOES.md`.
- [ ] **Confirmação automática da indicação**: a base é a confirmação manual do admin;
      por cima dela, o cruzamento automático quando o cadastro do sócio aparecer com
      nome e telefone batendo. Exige integração entre dois projetos hoje independentes
      — desenhar antes de construir.

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
- [ ] **Cadastro das bancas do Arraial** — formulário de inscrição do edital da feira
      (o que vende, tamanho da banca, se traz estrutura, se precisa de energia),
      seleção pela coordenação, confirmação da vaga, mapa dos espaços demarcados e
      registro do acerto (taxa de 5% a 10% ou valor fixo) para o balanço do evento.

---

## 4. Documentos (`documentos explosão/`)

Os `.docx` são **gerados por script** em `documentos explosão/_geradores/`
(`kit.py` + um `gen_*.py` por documento). Editar o gerador e rodar de novo —
nunca editar o `.docx` na mão.

> **Para rodar os geradores nesta máquina:** o `python-docx` está disponível no
> Python do Laragon (`C:\laragon\bin\python\python-3.13`), então basta
> `python gen_socio.py` dentro de `_geradores/`. (A observação anterior, sobre um
> Python *embeddable* sem pip, não vale mais.)
>
> Para **ler** os `.docx` dentro do VS Code, está instalada a extensão
> *Office Viewer* (`cweijan.vscode-office`) — visualiza `.docx`, `.xlsx`, `.pdf`
> e `.csv`. É só leitura: alterar continua sendo pelo gerador.

- [ ] **Confirmar o tema anterior.** O plano de reestruturação trata
      *"A Bolha do Amor"* como **tema anterior** (usa a expressão "tema anterior", sem
      citar ano). Se for o tema de 2027, o capítulo de diagnóstico precisa ser reescrito.
- [x] **Organograma limpo e com gerador** (29/07/2026). Saiu o parágrafo solto de
      chat, entrou o padrão visual do kit, o capítulo de objetivo, o quadro de
      alçadas e o quadro de nomeação. A imagem do organograma vive agora em
      `_geradores/_ativos/organograma.png`.
- [ ] **Kit Parceiro** — atualizar para o novo papel das parcerias: sustentar o Programa
      Sócio Torcedor (descontos, prêmios de sorteio, brindes) e gerar ações para o
      público geral.
- [x] **Plano de Implementação do Sócio Torcedor** (`gen_socio.py`) — corrigido e
      regerado em 27–28/07/2026: temporada de 10 meses, calendário de implantação
      refeito (campanha no fim de 2026, captação em janeiro/2027, início em
      fevereiro/2027), sorteio condicionado a estar em dia, transparência por
      temporada, carteirinha exclusiva e os **novos valores dos níveis**.
- [x] **Programa Sócio Torcedor (divulgação)** — corrigido em 27–28/07/2026: sorteio
      com a condição de estar em dia, transparência liberada temporada por temporada,
      carteirinha exclusiva de quem aderir até fevereiro/2027 e os novos valores.
      Continua **sem gerador** (editado via `python-docx` avulso) — migrar para o kit
      segue pendente abaixo.

> **Valores dos níveis (28/07/2026):** Fogueira **R$ 10** · Bandeirinha **R$ 20** ·
> Estrela do Arraial **R$ 30** — antes 5/10/20. Na temporada de 10 meses: R$ 100 /
> R$ 200 / R$ 300 por sócio, e a meta de 100 sócios passa de R$ 8.000 para
> **R$ 15.000**. Já refletido nos dois `.docx` e no `server/niveis.js` do projeto
> irmão. Segue como **proposta até a Diretoria bater o martelo**.
- [x] **Sócio Torcedor: os dois documentos detalhados contra o site** (29/07/2026) —
      régua do atraso, entressafra, corte do dia 20, valor derivado do nível, login
      do sócio, missões, travas do sorteio, painéis e status real dos marcos. O
      material de divulgação ganhou gerador (`gen_socio_divulgacao.py`) e seções
      novas (painel, troféus, missões, atraso e FAQ).
- [x] **Guia do contrato e da bonificação** (29/07/2026) — documento novo
      (`gen_contrato_guia.py`) explicando por que o contrato existe, o valor
      jurídico dele, o programa com o teto e a interação com o sistema.
- [x] **Arraial da Explosão reenquadrado como projeto** (29/07/2026) — o "por que
      fazer", a parceria com a Prefeitura e a feira com edital, taxa e banner.
- [ ] **Contrato do brincante** — revisar antes da assinatura prevista para fevereiro de
      2027 (datas da temporada, prazos de adesão e ativação). O teto de R$ 80 já entrou
      (29/07/2026, via `patch_contrato_teto.py`).
- [ ] **Preencher os campos em branco antes de imprimir/divulgar:** os cinco
      contatos oficiais da coordenação no contrato (primeira página dos dois termos)
      e o bloco "FALE CONOSCO" do material de divulgação do Sócio Torcedor, que ainda
      está com `[Nome do responsável]` e `[Telefone/WhatsApp]`.
- [ ] **Leitura jurídica do contrato** antes da assinatura de fevereiro/2027 —
      sobretudo imagem, anexos de menor de idade e a natureza não empregatícia da
      bonificação. O guia registra que o texto foi escrito pela própria coordenação.
- [ ] Documentos sem gerador (editados à mão ou por script pontual): **Contratos**
      (alterado por `patch_contrato_teto.py`) e **Kit Parceiro**. Migrar para o kit
      quando forem revisados — o resto da pasta já é gerado.

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
- [ ] **Fechar a condição das bancas** do Arraial. A proposta do dono (29/07/2026) é
      **taxa de 5% a 10% sobre a venda ou valor fixo pelo espaço**, valendo também
      para quem ocupa lugar na tenda; falta a Diretoria escolher o modelo e o número.
      Danças convidadas seguem sem pagar.
- [ ] **Protocolar o ofício de parceria com a Prefeitura** para o Arraial da Explosão,
      pedindo recursos, limpeza, segurança, organização do espaço, estrutura e
      transporte/hospedagem das danças convidadas. O cronograma do evento coloca isso
      em D-90 — é o item que decide o tamanho do evento.
- [ ] **Publicar o edital da feira** com o formulário de cadastro das bancas, para
      montar o mapa dos espaços e o banner de divulgação com o nome de cada uma.
- [ ] **Meta de sócios por brincante** para a captação da temporada.
