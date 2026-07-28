# PENDÊNCIAS — Explosão Junina de Beruri

> Tudo que está em aberto: no sistema, no site do Sócio Torcedor, nos documentos e
> nas decisões da coordenação. O que já foi feito está no `ATUALIZACOES.md`;
> o que o sistema é está no `CONTEXTO.md`.
>
> **Última revisão:** 2026-07-27.
>
> **Decisões de 27/07/2026 são a referência.** Onde um documento anterior conflitar
> com elas, o documento é que muda. Nos dois pontos em que o próprio 27/07 se
> contradiz, valem: temporada do Sócio Torcedor de **10 meses** (fev–nov) e
> **2027 como primeira temporada**.

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
- [ ] **Projeto Firebase próprio** (separado de `explosao-junina`) e site próprio no
      Netlify — pendências do dono, listadas no `PROXIMOS-PASSOS.md` de lá.
- [ ] **Resto do M2** (config/geral, campos novos, cálculo de situação, painel do
      sócio, importação CSV, finanças, comprovante no Drive), **M3** (troféus,
      missões, ranking, sorteios) e **M4** (página pública e adesão online).

### Cruzamentos com este sistema (decididos em 27/07/2026)
- [ ] **Módulo de missões neste sistema** para a captação de sócios: o brincante
      declara quem trouxe (**nome e telefone apenas** — nunca CPF ou data de
      nascimento, que são a credencial de login do sócio), fica pendente e o admin
      confirma. Vale **desempenho e troféu, sem bonificação em dinheiro** — não mexe
      no contrato nem na frequência.
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

---

## 4. Documentos (`documentos explosão/`)

Os `.docx` são **gerados por script** em `documentos explosão/_geradores/`
(`kit.py` + um `gen_*.py` por documento). Editar o gerador e rodar de novo —
nunca editar o `.docx` na mão.

> **Para rodar os geradores nesta máquina:** o Python instalado
> (`C:\Users\EJUD\python313`) é a distribuição *embeddable*, **sem pip e sem
> site-packages**, então `pip install python-docx` não funciona. As dependências
> (`python-docx`, `lxml`, `typing_extensions`) foram baixadas do PyPI para uma
> pasta à parte e usadas via `sys.path.insert` — sem alterar a instalação do
> Python. Numa máquina com pip normal, basta `pip install python-docx` e rodar
> `python gen_socio.py`.
>
> Para **ler** os `.docx` dentro do VS Code, está instalada a extensão
> *Office Viewer* (`cweijan.vscode-office`) — visualiza `.docx`, `.xlsx`, `.pdf`
> e `.csv`. É só leitura: alterar continua sendo pelo gerador.

- [ ] **Confirmar o tema anterior.** O plano de reestruturação trata
      *"A Bolha do Amor"* como **tema anterior** (usa a expressão "tema anterior", sem
      citar ano). Se for o tema de 2027, o capítulo de diagnóstico precisa ser reescrito.
- [ ] **Limpar o `Organograma - Explosão Junina.docx`.** O arquivo começa com um
      parágrafo solto de conversa (sobra de copiar/colar de chat) e não segue o padrão
      visual dos outros documentos.
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
