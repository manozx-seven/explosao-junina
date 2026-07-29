# ATUALIZAÇÕES — Sistema de Avaliação · Explosão Junina

> Histórico de tudo que foi feito no projeto, do mais recente para o mais antigo.
> **Regra fixa:** toda modificação no projeto deve ser registrada aqui (ver `CLAUDE.md`).
> Formato de cada entrada: data, título e o que mudou / por quê.

---

## 2026-07-29 — Teto de R$ 80 na bonificação (contrato e sistema)

Decisão do dono: o Programa de Bonificação passa a ter **teto de R$ 80,00 por
brincante na temporada**. Ele existe para o programa dar retorno simbólico sem
estourar o orçamento — sem teto, o custo depende de quantos convites de
apresentação aparecerem, e isso ninguém controla.

- **Contrato** (`documentos explosão/Contratos Explosao Junina Final.docx`):
  novo script `_geradores/patch_contrato_teto.py`, idempotente, alterando os
  **dois termos** (Brincante e Item Destaque): alíneas "e" e "f" na Cláusula
  Sexta, III; alínea nova na seção X amarrando o Programa de Fidelidade ao mesmo
  teto (o Nível 3 dobra o valor por ensaio — sem essa linha, os dois pontos do
  documento se contradiriam); linha do teto na tabela de projeção; observação
  explicando que o máximo atual (R$ 44,00) ainda fica abaixo dele; e o teto no
  quadro de adesão da primeira página, onde o brincante assina.
  O contrato segue sem gerador completo: reescrevê-lo do zero arriscaria perder
  formatação jurídica (campos de assinatura, caixas de opção, anexos). O patch é
  script versionado — continua valendo que nenhum `.docx` é editado à mão.
- **Sistema:** config nova `tetoBonificacao` (padrão `80.00`), `tetoConfig_()` e
  `aplicarTeto_()` em `server/handlers.js`. **O teto entra antes da sanção**: ele
  limita o que se acumula, e a sanção desconta sobre o acumulado. Invertido, a
  advertência formal (−50%) renderia mais a quem passou do teto do que a quem
  ficou nele. `0`, vazio ou lixo = sem teto — erro de digitação na tela de
  configurações não pode zerar a bonificação de todo mundo em silêncio.
- **`getPerfilBrincante`** devolve `bonificacaoSemTeto`, `teto` e `tetoAtingido`;
  **`getSimulacaoBonificacao`** devolve `valorSemTeto`/`atingiuTeto` por
  brincante, mais `teto`, `noTeto` e `tetoTotal` — o compromisso máximo com os
  elegíveis de hoje, que é o número de que o Financeiro precisa para reservar
  orçamento.
- **Frontend:** campo do teto na aba Configurações; faixa na aba Bonificação com
  teto, compromisso máximo e quantos já chegaram nele; marca "no teto" na linha
  de quem atingiu; e, no perfil do brincante, aviso com quanto falta para
  alcançá-lo (ou de que chegou, deixando claro que presença e nota continuam
  sendo requisitos para receber).
- **Testes: 63 asserções, todas passando** (eram 55). Oito novas cobrem o teto no
  perfil e na simulação, a **ordem teto → sanção** (R$ 120 com −50% vira R$ 40, e
  não R$ 60) e o desligamento do teto com `0`.
- `CONTEXTO.md` §5 e §6 atualizados.

## 2026-07-29 — Documentos: Arraial, Organograma, contrato explicado e Sócio Torcedor

Rodada de documentos pedida pelo dono. Três geradores novos, dois reescritos e
um `.docx` corrigido por script.

- **Arraial da Explosão** (`gen_arraial_explosao.py`): reenquadrado como
  **projeto**, não como plano de um evento que já existe — capítulo 1 novo ("Por
  que vamos fazer"), com o problema (a temporada junina morre cedo em Beruri), a
  ideia que costura a reestruturação (**estar sempre ativo, sempre inovando,
  sempre movimentando o cenário da quadrilha na cidade**), o que cada frente da
  quadrilha ganha com o evento e o que precisa ser decidido para ele sair do
  papel. A **§4 Feira e Comércio Local** foi refeita: parceria com a Prefeitura
  (limpeza, segurança, espaço, estrutura, transporte e hospedagem das danças
  convidadas), **taxa de 5% a 10% sobre a venda ou valor fixo pelo espaço**,
  edital com formulário de cadastro das bancas, seleção, mapa e demarcação dos
  espaços, e **banner de divulgação com o nome de cada banca** — que é o que
  transforma a taxa em investimento para o comerciante. Cronograma, checklist,
  riscos, equipes e a lista do que o sistema vai fazer acompanharam a mudança.
- **Guia do contrato** (`gen_contrato_guia.py`, documento **novo**): "Contrato e
  Bonificacao - Guia Explicativo.docx". Explica por que existe contrato numa
  quadrilha, o que ele protege dos dois lados, a importância jurídica (afastar
  vínculo empregatício, cessão de imagem, anexos de menor de idade, direito de
  defesa, formalidades), o Programa de Bonificação inteiro **com o teto** e um
  capítulo mapeando **cláusula por cláusula onde ela vive dentro do Sistema de
  Avaliação**. Fecha com FAQ do brincante e checklist da reunião de assinatura.
- **Organograma** (`gen_organograma.py`, gerador **novo**): o arquivo era o único
  editado direto no Word e abria com um parágrafo solto de conversa colado de
  chat. Agora tem gerador no padrão do kit, com a **imagem do organograma
  preservada** (`_geradores/_ativos/organograma.png`, embutida pelo novo helper
  `imagem()` do `kit.py`). Conteúdo dos cargos mantido, mais: capítulo de
  **objetivo** (organizar a Explosão, direcionar a Diretoria, distribuir papéis,
  mapear as divisões do ano e da arena, evitar acúmulo de função e definir de
  quem cobrar), quadro de alçadas, regras de funcionamento, aviso sobre as
  frentes ainda sem dono (Sócio Torcedor, arrecadação, arraiais, parcerias) e
  **quadro de nomeação** para a reunião da Diretoria.
- **Sócio Torcedor — Plano de Implementação** (`gen_socio.py`): atualizado contra
  o repositório do site. Entraram a régua do atraso (em dia / pago com atraso /
  atrasado / suspenso / inativo), entressafra e volta do inativo, corte do dia
  20, valor derivado do nível, login por CPF e nascimento, capítulo novo de
  **missões** (os quatro tipos, custo de validação de cada um, prova por link ou
  texto, pontos retidos), as três travas do sorteio, o que o sócio e a
  coordenação fazem em cada painel, um bloco de segurança e o status real dos
  marcos. As três conquistas que estavam "em breve" passaram a **"no ar"** — o
  módulo de missões ficou pronto.
- **Sócio Torcedor — divulgação** (`gen_socio_divulgacao.py`, gerador **novo**):
  era editado avulso. Ganhou gerador e seções novas — painel do sócio, troféus,
  missões, "e se eu atrasar?" e um FAQ.
- **Projeto Explosão Junina** (`gen_projeto.py`): passou a abrir com **"As
  novidades da temporada 2027"** e o **mapa dos documentos**, como o dono pediu.
  Atualizados: o teto no §10.2, a missão de captação e o aviso de registro no
  §10.1, o status real do site do sócio no §10.3, o cadastro de bancas no §10.4,
  o organograma como coração da reestruturação no §4, o guia e o valor jurídico
  do contrato no §8.4, e o Arraial como projeto (com parceria e taxa das bancas)
  no §11.3.
- **`kit.py`:** helpers `imagem()` e a pasta `_ativos/`.
- **Backups** dos três `.docx` que existiam antes do gerador ficaram em
  `documentos explosão/_backup/`.

> **Sobre rodar os geradores:** nesta máquina o `python-docx` está disponível no
> Python do Laragon (`C:\laragon\bin\python\python-3.13`). A observação antiga do
> `PENDENCIAS.md` sobre o Python *embeddable* sem pip não vale mais.

## 2026-07-28 — Missão de captação de sócios torcedores (módulo novo)

Aplicada no sistema a decisão que estava só no papel — "Programa Socio Torcedor -
Plano de Implementacao.docx" §6: **trazer sócios é uma missão do brincante e vale
desempenho e troféu, não dinheiro**. Era o último item do documento que ainda não
existia em código (o resto já estava no projeto irmão e nos dois `.docx`).

- **Coleção nova `indicacoes/{autoId}`**: `BrincanteID`, `Nome`, `Telefone`,
  `Status` (`pendente`/`confirmada`/`recusada`), `DataDeclaracao`, `DeclaradaPor`,
  `DecididaPor`, `DataDecisao`, `MotivoRecusa`.
- **Privacidade como regra de código, não como recomendação:** guarda-se apenas
  **nome e telefone**. CPF e data de nascimento juntos são a credencial de login
  do sócio no Site Sócio Torcedor — o documento gravado é montado campo a campo,
  então o que o cliente mandar além disso não entra. Há teste provando.
- **Handlers** (`server/handlers.js`): `getIndicacoes`, `addIndicacao`,
  `decidirIndicacao`, `removeIndicacao`, `getCaptacao`. Todos declarados em
  `FUNCOES` com escopo e aridade.
  - `addIndicacao` e `removeIndicacao` são **`autenticado`**: o brincante declara
    por si e o **ID vem da sessão** (mesma trava de `getPerfilBrincante`); apaga
    só a própria indicação e só enquanto pendente. Admin declara em nome de
    alguém e apaga qualquer uma.
  - `getIndicacoes`, `decidirIndicacao` e `getCaptacao` são **`admin`**.
  - Telefone já declarado (e não recusado) é **recusado como duplicata** — dois
    brincantes reivindicando o mesmo contato vira briga na hora do troféu.
- **Nada de dinheiro e nada de frequência:** a missão não entra em `getRanking`,
  `getSimulacaoBonificacao` nem nas contas de presença/nota. Quatro testes
  cobrem exatamente isso, porque é a promessa do contrato que não pode escorregar.
- **Troféu "Chamador de Gente"** ao bater a meta da temporada. Config nova
  `metaSociosPorBrincante` (padrão **2**, o indicador do Plano §15), editável na
  aba **Configurações**. O nome vive numa constante no servidor
  (`TROFEU_CAPTACAO`) e a tela lê dela — já mudou uma vez (era "Padrinho", nome
  aposentado do documento no mesmo dia) e não pode haver duas verdades.
- **Frontend** (`public/index.html`): aba **Sócios** para a coordenação (stats,
  fila de confirmação, ranking de captação, histórico com desfazer/apagar) e card
  **"Missão: traga a torcida"** no perfil do brincante (progresso, troféu, lista
  das próprias indicações e o formulário de declaração). O formulário avisa, na
  tela, para nunca pedir CPF ou data de nascimento.
- **Helper `esc()`** novo no front: o nome do sócio é digitado por brincante, a
  entrada mais aberta do sistema. O nome **não viaja dentro do `onclick`** — o
  navegador decodifica entidades HTML antes do JS, então um nome com apóstrofo
  quebraria o handler mesmo escapado; passa-se o id e busca-se o nome.
- **Testes: 55 asserções, todas passando** (eram 29). O Firestore falso ganhou
  `where`, que faltava — sem ele o teste não alcançava `getPerfilBrincante`.
- **Verificado também contra o Firestore real** (`netlify dev --offline`): as duas
  funções novas devolvem 401 sem token, `getCaptacao` responde com o ranking
  montado, `metaSociosPorBrincante` chega ao `getConfig` e o token morre no logout.
- **Pendente do desenho** (segue no `PENDENCIAS.md`): o cruzamento automático com
  o cadastro do outro sistema. A confirmação manual do admin é a base — o
  automático entra por cima dela, nunca no lugar.

## 2026-07-28 — Plano do Sócio Torcedor: troféus renomeados, M2 pronto e M3 em andamento

Edição do dono no `_geradores/gen_socio.py`, com o `.docx` regerado. **Só
documento** — mas mexe no vocabulário e no status que o resto do projeto usa.

- **Catálogo de troféus refeito** (§9), agora com coluna de situação: Primeira
  Fagulha, Pontual, Trio de Fogo, Temporada Completa, **Chamador de Gente**,
  Veterano e **Sócio Fiel** (físico, entregue a cada dois ou três meses) estão
  "no ar"; Torcedor de Arquibancada, Missão Cumprida e Puxador de Fila ficam
  marcados como **"em breve"** até o módulo de missões do site entrar.
  **"Padrinho" saiu** — "Chamador de Gente" é o troféu de indicar alguém que
  virou sócio de verdade. Foi por isso que o troféu da missão neste sistema
  mudou de nome na entrada acima.
- **Indicação não gera sorteio extra** (§6): quem indica ganha reconhecimento e
  o troféu, e não uma segunda urna — "criar uma segunda urna contradiria a
  promessa feita ao sócio" (todos concorrem com a mesma chance). Este sistema
  não tem sorteio, então nada a mudar aqui; vale para o projeto irmão.
- **Status do site do sócio atualizado** (§12): **M2 Pronto** (painel do sócio,
  carteirinha digital, troca de nível, mural, importação por planilha) e **M3 em
  andamento** (troféus e vitrine prontos; faltam missões com validação em lote,
  ranking, sorteios e notificações). Do M2 falta só o comprovante por imagem,
  preso a credenciais externas. Para o site subir de verdade, faltam **banco e
  hospedagem** — dependem da criação das contas.
- `PENDENCIAS.md` §2 realinhado a esse status.

## 2026-07-28 — Novos valores dos níveis do Sócio Torcedor (10 / 20 / 30)

- **Decisão do dono:** Fogueira passa de R$ 5 para **R$ 10**, Bandeirinha de R$ 10
  para **R$ 20** e Estrela do Arraial de R$ 20 para **R$ 30**. Na temporada de dez
  meses, isso dá R$ 100 / R$ 200 / R$ 300 por sócio, e a meta de 100 sócios sai de
  R$ 8.000 para **R$ 15.000**.
- **`_geradores/gen_socio.py`:** tabela de níveis e cenários atualizados pelo dono;
  os **indicadores do fim do documento** ainda diziam "R$ 800/mês" e "R$ 8.000 na
  temporada" — corrigidos para R$ 1.500 e R$ 15.000, senão o documento fecharia
  contradizendo a própria tabela de metas. Documento **regerado**.
- O material de **divulgação** e o `server/niveis.js` do projeto irmão já haviam
  sido atualizados para os mesmos valores — os três lados estão coerentes.
- `PENDENCIAS.md`: correções dos dois documentos marcadas como concluídas; os novos
  valores ficaram registrados como **proposta até a Diretoria decidir**. Anotado
  também como rodar os geradores nesta máquina (o Python daqui é *embeddable*, sem
  pip) e a extensão *Office Viewer* instalada no VS Code para ler os `.docx`.

## 2026-07-27 — Alinhamento com o Site Sócio Torcedor (decisões e governança)

Leitura cruzada dos dois projetos para alinhá-los, já que são da mesma quadrilha.
As divergências encontradas foram levadas ao dono e decididas. **Fica valendo:
tudo o que foi decidido em 27/07/2026 é a referência** — documento anterior que
conflite é o que muda.

- **Temporada do Sócio Torcedor: 10 meses** (fev–nov), como está no `ARQUITETURA-M2.md`.
  Os documentos calculavam 12 meses (R$ 9.600 para 100 sócios) — passa a **R$ 8.000**.
- **Primeira temporada: 2027**, alinhada ao resto da quadrilha. Campanha no fim de
  2026, captação em **janeiro/2027**, programa começa em **fevereiro/2027**. Como a
  captação toda cai em jan–fev, todo o primeiro grupo é "sócio desde fevereiro" e
  fica elegível aos prêmios da temporada — sem precisar de exceção.
- **Sorteio exige estar em dia** (regra do sistema). O material de divulgação, que
  prometia "todos concorrem com a mesma chance" sem condição, é que será corrigido.
- **Transparência:** por ora o sócio vê apenas a **temporada anterior**. A da
  temporada vigente depende de a coordenação definir a categorização de gastos e
  investimentos para lançamento em tempo real.
- **Carteirinha:** digital no painel do sócio; genérica para impressão gerada pelo
  site; e uma **física exclusiva**, de design próprio, entregue numa reunião só a
  quem aderiu **até fevereiro/2027** — item de colecionador.
- **Captação de sócios por brincante:** vira **módulo de missões neste sistema**,
  valendo **desempenho e troféu, sem dinheiro** (não mexe no contrato nem na
  frequência). A declaração coleta **nome e telefone apenas** — nunca CPF e data de
  nascimento, que juntos são a credencial de login do sócio no outro sistema.
  Confirmação manual do admin como base, com cruzamento automático por cima.
- **`CLAUDE.md`:** passa a mandar ler o `PENDENCIAS.md` no início da sessão (o
  projeto irmão já fazia isso), a riscar de lá o que for concluído, e registra o
  projeto irmão + onde vivem os documentos dele. Novo aviso: handler novo precisa
  entrar em `FUNCOES` com escopo e aridade.
- **`PENDENCIAS.md`:** seção do Sócio Torcedor reescrita — estava desatualizada
  (apontava pasta inexistente e dizia que o projeto não estava no Git). Entraram os
  cruzamentos entre os dois sistemas e a lista de correções dos documentos.

## 2026-07-27 — Sessão por token e escopos na API (falha de segurança corrigida)

**A API estava completamente aberta, em produção.** `netlify/functions/api.js`
validava apenas se o nome da função estava numa lista — nenhuma autenticação. As
27 funções respondiam a qualquer requisição: `getBrincantes` devolvia o **CPF
completo** de todos (e o CPF é a senha de login), e `addBrincante`,
`removeBrincante`, `deleteEnsaio` e `updateConfigMap` podiam ser chamadas por
qualquer um com a URL. O objeto `usuario` gravado nos logs vinha **como argumento
do navegador** — bastava declarar-se "Coordenação".

Portada a solução já em uso no projeto irmão (Site Sócio Torcedor), com as
adaptações deste sistema:

- **`server/sessoes.js` (novo):** coleção `sessoes/{token}` com token de 32 bytes
  (`crypto.randomBytes`), `Tipo` (`admin`/`brincante`), `BrincanteID`, `Nome` e
  `ExpiraEm`. Admin expira em 12 h, brincante em 30 dias. O formato do token é
  validado por regex **antes** de virar caminho no banco — sem isso um token com
  `/` alcançaria outro documento. Faxina de sessões vencidas de carona no login
  (1 em 10), já que Netlify Functions não têm cron.
- **`netlify/functions/api.js`:** a whitelist virou um mapa em que cada função
  declara **escopo** (`publico`/`autenticado`/`brincante`/`admin`) e **aridade**.
  O dispatcher valida o token, confere o escopo e injeta a sessão como último
  argumento do handler.
  - **Anti-forja:** a lista de argumentos é normalizada para exatamente a aridade
    declarada antes de a sessão ser anexada — argumentos a mais são descartados
    (senão o cliente empurraria um objeto para o lugar da sessão) e a menos viram
    `undefined` (para a sessão não escorregar de posição).
  - Respostas 401 carregam `__auth: true`, sinalizando ao front que descarte a sessão.
- **`server/handlers.js`:** `login` cria a sessão e devolve o token; novos
  handlers `logout` e `entrarComoBrincante`. Duas travas de escopo:
  `getPerfilBrincante` e `setDestinoBonificacao` passaram a ler o ID **da
  sessão** quando quem chama não é admin — antes, trocar um parâmetro dava acesso
  ao desempenho, à bonificação e às advertências de outra pessoa. Trocar o **CPF**
  de um brincante agora derruba as sessões dele (o CPF é a senha).
- **Papel duplo virou real:** quem é coordenação **e** item/brincante escolhia no
  login como entrar, mas era só visual — o acesso continuava total. Agora
  escolher "item/brincante" chama `entrarComoBrincante`, que **rebaixa a sessão**
  no servidor. Só rebaixa, nunca promove.
- **`public/index.html`:** guarda o token e o envia em toda chamada; parou de
  mandar `currentUser` como argumento (17 chamadas); `logout` encerra a sessão
  também no servidor; sessão recusada cai para a tela de login com aviso, em vez
  de deixar tela pela metade.
- **`testes/api.test.js` (novo) + `npm test`:** o teste ficou **versionado no
  projeto**, como no repositório irmão. Não precisa de Firebase nem de
  `netlify dev` — injeta um Firestore em memória no lugar do `server/firebase.js`
  e chama o handler da Netlify Function direto.
- **Testes executados: 29, todos passaram** — chamada sem token → 401 (com
  `__auth`); token forjado → 401; token com path
  injection (`../brincantes/DEV`) → 401; token não-string → 401; senha errada não
  devolve token; brincante em função de admin → 403 (e a config **não** foi
  alterada); brincante tentando mudar o destino da bonificação de outro → alterou
  o **próprio**, o do outro ficou intacto; tentativa de injetar
  `{id:'HACKER'}` no lugar da sessão → o log gravou "Coordenação"; sessão
  rebaixada perde acesso admin; troca de CPF invalida o token antigo; logout
  invalida o token.
- **Pendente para o deploy:** todo mundo vai precisar entrar de novo (as sessões
  nascem agora). O usuário `DEV`/`123456` continua existindo — remover quando
  houver um admin real (ver `PENDENCIAS.md`).

## 2026-07-27 — Pendências registradas e publicação de tudo no GitHub

- **Novo `PENDENCIAS.md`** (raiz do repo): registro único de tudo que está em aberto —
  configuração da temporada no Firestore, segurança (token de sessão, remover `DEV`),
  funcionalidades adiadas (fidelidade, checklist de resgate, compartilhar desempenho),
  **site do Sócio Torcedor** (M2–M4, sem repo/Netlify/Firebase próprios), as
  implementações previstas nos documentos de 2027 (votação do Arraial, certificados,
  venda de camisa, painel de transparência, sorteio digital), pendências dos documentos
  e as decisões que dependem da coordenação.
- `.gitignore`: passa a ignorar `__pycache__/` e `*.pyc` (cache dos geradores).
- **Publicado na `main`** todo o trabalho que estava só local desde 09/07 — o código do
  sistema (destino da bonificação, pagamento pós-Festival, atividades com participantes
  designados) e todos os documentos. O push dispara o redeploy no Netlify.
- **Fora deste push:** o *Site Sócio Torcedor* continua em pasta separada e sem
  repositório — por decisão de arquitetura (projeto independente), ele precisa do
  repositório e do site próprios (registrado no `PENDENCIAS.md`).

## 2026-07-27 — Documentos da temporada 2027: plano de reestruturação e novo modelo de arrecadação

Reorganização completa da documentação estratégica da quadrilha para a **temporada
2027**, planejada desde o zero (trabalho começando em **agosto de 2026**). **Nada de
código** — só documentos. Todos os prazos são **previsões**, sem datas fechadas.

- **Novo: `documentos explosão/_geradores/`** — os `.docx` passam a ser **gerados por
  script** (`kit.py` + um `gen_*.py` por documento, via `python-docx`). Padrão visual
  único (Arial, vermelho `922B21`, grafite `2C3E50`, banners e tabelas com cabeçalho
  colorido). Para alterar um documento, edita-se o gerador e roda-se de novo —
  não se edita o `.docx` na mão.
- **Excluído** `Guia Implementacao Explosao Junina.docx` — era a estratégia de entrada
  "com a temporada em andamento"; não faz mais sentido, já que 2027 é planejada desde
  o começo.
- **`Projeto Explosao Junina Beruri.docx` reescrito** como **Plano de Reestruturação**
  (não é mais proposta de agência/investimento): a virada de "movidos a emoção" para
  gestão técnica. 15 capítulos — diagnóstico (incluindo os problemas do tema anterior),
  princípios, **estrutura organizacional baseada no `Organograma - Explosão Junina.docx`**
  (Diretoria, Comissão de Artes, Grupos de Produção, Equipes de Arena, fluxo de decisão),
  tema e espetáculo, identidade visual, comunicação/redes (mostrar bastidor, correria,
  ensaios, desenvolvimento do tema e prévias), gestão e transparência, ensaios, **o
  sistema da Explosão** (avaliação + bonificação + sócio torcedor), captação de recursos,
  linha do tempo (ago/2026 → pós-Festival 2027: identidade visual em jan/fev, contratos
  em fevereiro), indicadores, riscos e visão de futuro.
- **`Projetos Arrecadacao Explosao Junina.docx` reescrito** para o **novo modelo**:
  vira **portfólio em stand by**. Base = repasses públicos + Sócio Torcedor; rifa, bingo,
  venda de comidas, cinema na praça e Cine Explosão só são **acionados por decisão da
  Diretoria** (gatilhos, rito de acionamento e comparativo de esforço/retorno). Ganhou
  seção de ações para o público geral e perdeu o que virou documento próprio.
- **Novos documentos** (um por frente prioritária):
  - `Programa Socio Torcedor - Plano de Implementacao.docx` — o **carro-chefe** da
    arrecadação: metas/cenários, ciclo mensal de operação, papéis, captação, entrega
    de benefícios, parceiros sustentando o programa, troféus, sorteios, transparência,
    marcos do site (M1 feito → M4) e indicadores.
  - `Arraial da Explosao - Plano do Evento.docx` — festa **depois do Festival** (agosto
    ou fim do ano): danças de Beruri e de fora, **competição com votação popular em
    tempo real** (QR code, apuração e premiação na hora), troféu + certificado para
    todos os grupos, feira com comerciantes berurienses, estrutura, equipes, cronograma
    D-60→D+7 e o que o sistema precisa fazer.
  - `Arraial de Lancamento - Plano do Evento.docx` — abertura da temporada (previsão
    março): revelação de tema/itens/camisa, **prestação de contas do ano anterior**,
    venda de camisa, sorteios (público e sócios), captação de sócios, cronograma e riscos.

## 2026-07-13 — Atividades com participantes designados (chamada por grupo)

Para atividades feitas por só um grupo de brincantes (ex.: entregar lembrancinhas
de aniversário aos sócios torcedores), a chamada agora pode mostrar **só o grupo
designado**, evitando o "branco ambíguo" de marcar presença para uns e deixar o
resto sem nada.

- **Campo novo no evento `Participantes`** (IDs separados por vírgula; vazio = todos).
  Só é oferecido para **atividades do compromisso** (arrecadação, braçal, comunitário,
  outra) — ensaios/apresentações seguem com todos.
- **Formulário de evento:** ao escolher um tipo de atividade, aparece a lista de
  brincantes (checkbox, com "Todos"/"Limpar"); marque só quem participa. Nos demais
  tipos o campo fica oculto e grava vazio.
- **Chamada:** quando o evento tem participantes designados, `loadAvaliacao` filtra a
  lista (`participantesDoEvento`) — só o grupo aparece, e o contador do cabeçalho
  reflete o grupo. Detalhe do evento mostra "Atividade de grupo: N participante(s)".
- **Métricas inalteradas:** essas atividades continuam **sem** entrar na frequência
  nem no valor da bonificação (decisão do usuário — "só registrar"). Ausência de quem
  não foi designado nunca é contada.
- Backend (`server/handlers.js`): `Participantes` em `getEnsaios`, `addEnsaio` e no
  `campoMap` de `updateEvento`. Frontend (`public/index.html`): `formEvento`,
  `evParticipantesHtml`/`toggleEvPartBox`/`fEvPartAll`, `ensureBrincantesCache`,
  `saveEvento`, `participantesDoEvento` e filtro na chamada.

## 2026-07-13 — Kit Parceiro (parcerias de beleza) + novo doc Programa Sócio Torcedor

Edições em documentos (via `python-docx`; backup temporário do Kit Parceiro antes de
salvar). **Nada de código.**

- **Kit Parceiro** (`documentos explosão/Kit Parceiro Explosao Junina.docx`):
  - Nova ação promocional **"Parceria com Maquiadores(as) e Cabeleireiros(as)"**
    dentro de *Ações Promocionais Conjuntas* (produção das apresentações grátis por
    divulgação ou pacote com desconto; contrapartida = "beleza/produção oficial da
    Explosão por [Nome]"; portfólio/vitrine). Alinha ao contrato: nas grandes
    apresentações a produção pode virar pacote do grupo, em vez do preço cheio individual.
  - Menção **"Não tem um negócio? Seja Sócio Torcedor"** apontando para o documento
    próprio do programa.
- **Novo documento** `documentos explosão/Programa Socio Torcedor Explosao Junina.docx`
  — **proposta inicial** (ajustável): o que é, como funciona, tabela de níveis
  (🔥 Fogueira R$5/mês · 🎏 Bandeirinha R$10 · ⭐ Estrela do Arraial R$20; também por
  temporada), benefícios progressivos, para onde vai o dinheiro, metas ilustrativas
  (~100 sócios ≈ R$ 800/mês), como se tornar sócio e transparência. Mantém a identidade
  visual e o tom dos outros materiais.
  - Seção **"O que a quadrilha faz por você"**: carteirinha digital e física, Close
    Friends e destaque no Instagram, **sorteios o ano todo com a mesma chance para
    todos os níveis** (dinheiro/kits/descontos de parceiros), descontos (blusa da
    temporada p/ todos; Estrela ganha blusa "Sócio Torcedor" com nome nas costas) e
    acesso à planilha de gastos.
  - **Site próprio** dos sócios descrito como "em desenvolvimento": adesão/pagamento
    pela plataforma, painel de contribuições e finanças, e **troféus/conquistas** ao
    longo do ano.
  - As ações de **aniversário** (story + lembrancinha entregue pessoalmente) foram
    **removidas do documento** a pedido do usuário — a quadrilha fará, mas é surpresa,
    não entra no material do sócio (fica só no planejamento).

## 2026-07-13 — Contrato: Cláusula Terceira (blusa/produção) + doação na bonificação

Editado o `documentos explosão/Contratos Explosao Junina Final.docx` (via
`python-docx`, backup temporário do arquivo antes de salvar). Alterações aplicadas
**nos dois termos** (Brincante Item Dançarino e Item Destaque):

- **Cláusula Terceira – Dos compromissos da quadrilha:**
  - item **a)** passou a "Fornecer, sem custo ao brincante, o **figurino completo e a
    blusa (camisa) do tema da temporada** para as apresentações oficiais;";
  - novo item **b)** "Providenciar a **produção das apresentações oficiais** (montagem
    de figurino, adereços e demais itens de palco);" (sem citar maquiagem/cabelo);
  - os itens seguintes foram re-letrados (antigos b…h → c…i).
- **Cláusula Sexta, VII – Condições para resgate:** novo item **d)** com a opção de
  **doar à quadrilha**, no todo ou em parte, o valor acumulado (registrada no sistema,
  feita ao fim da temporada quando o valor está fechado) — alinha o contrato ao
  recurso de destino da bonificação já implementado no sistema.
- **Não** foi alterada a arrecadação (Cláusula Segunda, "l"): a quadrilha não fica
  amarrada a bancar tudo e ainda pode precisar da ajuda (inclusive financeira) dos
  brincantes. Pagamento pós-Festival já estava explícito (VII, "a") — mantido.

## 2026-07-13 — Bonificação: pagamento pós-Festival + liberação manual da escolha

- **Configurações → "Pagamento da bonificação"** (novos campos, informativos):
  `dataPagamentoBonif` (pagamento previsto, após o Festival), `dataPagamentoBonif2`
  (2ª parcela — modelo 13º, opcional) e `obsPagamentoBonif` (texto livre de como
  será pago). Aparecem no **perfil** de cada brincante para ele saber quando/como
  vai receber.
- **Toggle `escolhaDestinoLiberada`** (bloqueada/liberada): a coordenação ativa
  **manualmente** quando a contagem já fechou (após o Festival) e cada um sabe
  quanto acumulou. Enquanto **bloqueada**, o brincante vê o valor mas **não escolhe**
  (o card do perfil mostra um aviso de cadeado com a opção registrada). Guarda no
  servidor: `setDestinoBonificacao` recusa a troca se o toggle não estiver liberado.
- **Perfil:** o card virou *"Bonificação: pagamento e destino"* — mostra as datas/
  observação de pagamento e, só quando liberado, os botões Resgatar/Doar.
- **Simulação (admin):** banner com data de pagamento, 2ª parcela/observação e o
  status da escolha (liberada/bloqueada).
- Backend (`server/handlers.js`): novas chaves no `DEFAULT_CONFIG`; `getPerfilBrincante`
  e `getSimulacaoBonificacao` devolvem `pagamento` + `escolhaDestinoLiberada`; guarda
  em `setDestinoBonificacao`. Frontend (`public/index.html`): card de Configurações,
  `saveConfig`, `buildDestinoCard`, banner em `renderBonificacao`.

## 2026-07-13 — Bonificação: resgatar ou doar à quadrilha (destino do acumulado)

- Novo campo por brincante **`DestinoBonificacao`** (`resgatar` = padrão / `doar`):
  no fim da temporada o brincante pode **resgatar** o valor acumulado ou **deixar/
  doar à quadrilha** para ajudar ainda mais a Explosão.
- **Auto-serviço no perfil:** o próprio brincante escolhe (card "Destino da sua
  bonificação", com botões Resgatar/Doar). Novo handler `setDestinoBonificacao`
  (só altera esse campo, com log) exposto na whitelist da API.
- **Coordenação** também define no **cadastro** (dentro do bloco de adesão) e na
  **edição** do brincante (`destinoBonificacao` no `campoMap` do `updateBrincante`).
- **Simulação de bonificação** agora consolida: **total acumulado**, **a pagar em
  resgates (sai do caixa)** e **doado à quadrilha (fica no caixa)**; nova coluna
  **Destino** (resgata/doa) por brincante, com o valor de quem doa em verde.
- Backend (`server/handlers.js`): `normalizaBrincante_`, `addBrincante`,
  `updateBrincante`, `getSimulacaoBonificacao` (`totalResgate`/`totalDoacao`) e o
  novo `setDestinoBonificacao`. Frontend (`public/index.html`): forms de cadastro/
  edição, card do perfil (`buildDestinoCard`/`escolherDestino`) e `renderBonificacao`.
- **Valores** da bonificação seguem configuráveis pela aba Configurações (sem mudança
  no `DEFAULT_CONFIG`). *Contexto:* verba pública passa a custear a temporada; a
  bonificação pode subir e o acumulado pode virar doação para a quadrilha.

## 2026-07-10 — Avaliação: seletor visual de evento (cards por categoria e cor)

- Na aba **Chamada e avaliação**, o antigo `<select>` de evento foi substituído por
  uma **grade de cards** (`#avPicker`), mais visual e fácil de escanear.
- Cards **agrupados por categoria**: *Ensaios* (regular, ensaião), *Apresentações*
  (apresentação, festival, igreja) e *Atividades do compromisso* (arrecadação,
  braçal, comunitário, outra). Cada grupo mostra a contagem.
- **Ordem por data** (mais recente primeiro) dentro de cada categoria. Cada card tem
  **cor por tipo** (borda/realce via `--accent` + badge reaproveitando as classes
  `chip-*`), dia em destaque, mês/ano, horário, badge de status (planejado/realizado/
  cancelado) e descrição.
- Ao clicar num card, abre a chamada normalmente; surge a barra **"Trocar evento"**
  (`avVoltar()`) para voltar à grade. Um `<select id="selEnsaioAv">` **oculto** foi
  mantido para não quebrar `goAvaliar()` (botão "avaliar agora" do detalhe do evento).
- Tudo em `public/index.html`: novo CSS (`.av-pick-*`, `.av-back-bar`), HTML da página
  e funções `renderAvPicker`/`avPickCard`/`pickAvEvento`/`avVoltar`; `loadEnsaioSelect`
  agora preenche o select oculto **e** renderiza os cards; `loadAvaliacao` alterna
  picker↔chamada. Sem mudança no backend.

## 2026-07-10 — Importação em lote com paridade total ao cadastro direto

- O **import de planilha/CSV** ganhou as duas colunas que faltavam para igualar o
  cadastro individual: **Assinatura** (data de assinatura do contrato) e **Adesão**
  (data de adesão à bonificação). Adicionadas **no fim** da ordem de colunas, então
  planilhas antigas (10 colunas) continuam funcionando sem alteração.
- Atualizados no `public/index.html`: texto de instruções do modal, `placeholder`
  do textarea, `parseImport` (lê `cols[10]`/`cols[11]` → `dataAssinatura`/`dataAdesao`),
  a **prévia** (novas colunas "Assin." e "Adesão"; mostra "hoje" quando em branco) e
  o **modelo CSV** de download (`baixarModeloCsv`).
- Sem mudança no backend: `addBrincante` já lia `dados.dataAssinatura`/`dados.dataAdesao`
  (com fallback para hoje) e valida a adesão contra `fimAdesao`. Antes, pelo lote,
  esses campos nunca chegavam e caíam sempre no default de hoje — o que podia
  rebaixar silenciosamente o opt-in de quem aderiu dentro do prazo. Agora a data
  real pode ser informada na planilha.

## 2026-07-09 — Sistema alinhado ao contrato (datas de ativação, perfil, menor de idade)

### Novos campos do brincante
- `DataNascimento`, `AnexoI` e `AnexoII` (`sim`/vazio). No **cadastro** e na
  **edição**, ao informar a data de nascimento, se for **menor de 18** aparece um
  bloco para marcar **Anexo I** (autorização do responsável) e **Anexo II**
  (viagem). O **import em lote/CSV** ganhou as colunas Nascimento, AnexoI, AnexoII
  (modelo e prévia atualizados).
- Backend: `normalizaBrincante_`, `addBrincante`, `updateBrincante` e o mapa de
  campos passam a gravar/ler esses campos.

### Datas de ativação e início da bonificação
- No **cadastro guiado**, ao digitar a data de adesão o sistema destaca agora
  **início da ativação**, **fim da ativação** e **a partir de quando começa a
  acumular** (até o Festival).
- `avaliarAtivacao` passou a devolver `bonificacaoInicio` = o maior entre o piso
  `inicioContagem` e o dia seguinte ao fim da ativação individual. A **contagem
  da bonificação** (perfil e simulação) agora começa nessa data individual, não
  mais num piso único — alinhado ao contrato (começa ao fim da ativação de cada um).
- **Perfil do brincante**: o card de Ativação mostra as datas (adesão, fim da
  ativação, desde quando acumula / quando começa, e até o Festival) e os
  critérios (presença/nota) em tempo real. Correção: os alertas usam a ativação
  **calculada** (`ativacao.status`), não mais o override manual.

### Dicas por nível (perfil)
- Novo card **"Dicas para você"**: por nível de desempenho, o sistema orienta —
  ex.: presença baixa → avisar faltas e procurar o líder de fila; nota baixa →
  procurar coordenação/coreógrafos para reforço; bom desempenho → continuar e
  ajudar os colegas. Gerado em `montarDicas_` (backend), renderizado no perfil.

### Config padrão → temporada 2027
- `DEFAULT_CONFIG` e os fallbacks do frontend passaram a 2027 (temporada, datas de
  contagem e adesão), alinhando os padrões ao contrato revisado. A config **viva**
  no Firestore continua mandando; se estiver 2026, ajustar pela aba Configurações.

## 2026-07-09 — Revisão dos documentos (contrato + material) na pasta "documentos explosão"

Revisão dos 5 `.docx` da pasta `documentos explosão/` (backup em
`documentos explosão/_backup/`). **Nada de código mudou** — só documentos.

### Contrato (`Contratos Explosao Junina Final.docx`)
- **Terminologia:** `brincante` passou a designar todo integrante; divisão em
  **Item Dançarino** (cordão) e **Item Destaque** (Marcador/Rei/Rainha/Noivo/
  Noiva). Definição na Cláusula Primeira + **seleção de categoria** nos dados.
- **Base de frequência:** 75% para Item Dançarino, **85% para Item Destaque**
  (inclusive ativação, resgate e manutenção da bonificação) — explicitado nas
  Cláusulas Segunda, Sexta e no Termo do Item.
- **Cláusula Sexta renumerada** (corrigido II/III repetidos e VIII pulado →
  agora I…X) e referência "seção II" → "seção I".
- **Início da bonificação** deixou de ser fixo em "maio": agora inicia **ao fim
  do período de ativação de cada um** (proporcional à adesão).
- **Falta grave definida** (10 faltas consecutivas ou 20 alternadas
  injustificadas = abandono, com direito a defesa); **perda de 50%** esclarecida
  como incidente sobre o acumulado ao fim do período; **advertência formal**
  detalhada; **desligamento pela quadrilha** condicionado ao esgotamento das
  sanções (salvo gravidade extrema); nova falta grave: faltar a apresentação.
- **Avaliação acolhedora** (Cláusula Quinta): caráter formativo, não punitivo,
  com apoio reforçado a quem tem mais dificuldade.
- **Cessão de imagem** ampliada (stories, reels, transmissões ao vivo, feed).
- **Ativação automática pelo sistema** citada na Cláusula Sexta.
- **Fidelidade** pode ser ajustada também **dentro da temporada** (orçamento).
- **Coordenação** com campos (nome/função/CPF/contato) para preencher; **Anexo
  II** passou a coletar RG/CPF do responsável (igual ao Anexo I).
- **Termo do Item Destaque:** ensaios individuais/surpresa mais intensos, menor
  de idade cobre Anexos I/II, exclusividade reforçada; "dobro do brincante"
  corrigido (15 dias vs 7).
- **"quadrilha concorrente" → "quadrilha rival"** e projeção do cenário realista
  corrigida (80% → R$ 35 ≈ R$ 1.330).
- **Ano:** contrato passou a **Temporada 2027**; Programa de Fidelidade para
  **2028** (por decisão de deslocar todo o ciclo +1 ano).

### Documentos de apoio (Guia, Projeto, Kit Parceiro, Arrecadação)
- Ano deslocado **+1** (2026→2027, 2027→2028; preservados 2025 do título de
  campeã e 2017 da fundação) e **"quadrilha concorrente" → "quadrilha rival"**.

### Sincronização Projeto ↔ Projetos de Arrecadação
- **Projeto Explosão · Eixo 4 (Captação de Recursos)** ganhou uma subseção para
  **cada projeto** do documento de Arrecadação: 7.1 Rifas, 7.2 Bingo, 7.3 Venda
  de Batata Frita, 7.4 Cinema na Praça, 7.5 Cine Explosão, 7.6 Arraial da
  Explosão, 7.7 Arraial de Lançamento, 7.8 Parcerias Comerciais (mantida a tabela
  de cotas) e 7.9 Outras Ações. Cada uma com descrição curta, remetendo ao
  documento Projetos de Arrecadação para o detalhamento.
- **Projetos de Arrecadação** ganhou a seção que faltava: **Parcerias Comerciais**
  — com "O que é", **tabela de cotas** (Ouro/Prata/Bronze/Produto-Serviço, com
  contrapartidas e perfil), **ações promocionais conjuntas** e **checklist de
  execução**, no mesmo formato dos demais projetos.

### Termo do Item Destaque agora é autossuficiente
- O documento continua único, mas cada termo é **entregue separadamente**, então
  o **Termo do Item Destaque** passou a ser **completo por si só**: reúne **todas
  as cláusulas do Termo do Brincante** (Objeto, Compromissos, Quadrilha, Imagem,
  Avaliação, Bonificação, Conduta/Sanções, Desligamento, Vigência e Disposições)
  **+ as específicas do item** (Exclusividade, Disponibilidade/Ensaios do item,
  Representação, Figurino, Confidencialidade, Substituição) — 16 cláusulas — com
  **frequência 85%**, seu **próprio opt-in de bonificação** e **Anexos I e II**.
- O **bloco de seleção de categoria saiu do Termo do Brincante** (que agora é,
  por definição, o termo do **Item Dançarino** / cordão). No **Termo do Item
  Destaque** entrou a **seleção de função** (Marcador/Rei/Rainha/Noivo/Noiva),
  já assumindo que o signatário é item destaque.
- Os dois termos ficam em páginas separadas (quebra de página entre eles).

> Observação: o **sistema** ainda usa `temporada = 2026` (piloto). Se a intenção
> for rodar o ciclo completo de bonificação já alinhado ao contrato de 2027,
> ajustar a config depois.

## 2026-07-08 — Fluxo de cadastro guiado (adesão com validação e cálculo)

- **Novo brincante** reordenado: identidade → **Data de assinatura do contrato** →
  **Programa de Bonificação** (opções "Não aderiu" / "Aderiu"). A **Data de adesão**
  só aparece quando escolhe "Aderiu".
- Ao digitar a data de adesão, o sistema **valida contra o contrato** e **calcula ao
  vivo**: se a data estiver fora do prazo (`inicioTemporada`..`fimAdesao`), mostra
  **erro** e bloqueia o cadastro; se válida, mostra o **fim do período de ativação**
  (adesão + 3 meses) e quando passa a acumular; se a ativação terminar depois do
  Festival, avisa que fica **não elegível** (mas permite cadastrar).
- Backend (`addBrincante`): a trava de adesão passou a olhar a **data de adesão**
  (não "hoje"). Assim dá para cadastrar em julho quem aderiu em fevereiro sem perder
  o opt-in; data de adesão após o prazo derruba o opt-in automaticamente.
- Import em lote: instrução do modal agora lista os **valores de Tipo** aceitos
  (inclui as combinações com coordenação).

## 2026-07-08 — Papéis (item/coordenação duplos), item 85% e acesso do brincante

### Tipos de brincante com papel duplo
- O campo `Tipo` passou a aceitar 5 valores: `brincante`, `item`, `coordenacao`,
  **`brincante_coord`** e **`item_coord`** (pessoa que dança E coordena — existe
  no grupo). Não existe brincante+item (são exclusivos). Selects de novo/editar e
  o import em lote reconhecem as combinações; a tabela mostra badges de papel +
  "coord.". Helpers no back (`ehCoordenacao_/papelDanca_/ehDancarino_/ehItem_`) e
  no front (`ehCoordTipo/papelDancaTipo/ehDancarinoTipo/tipoBadge`).
- Métricas (dashboard, ranking, bonificação) passaram a incluir **quem dança**
  (`ehDancarino_`) e excluir só coordenação pura.

### Regra do Item (Cláusula Segunda do Termo do Item)
- Item exige **frequência mínima de 85%** (config nova `frequenciaItem=85`,
  editável na aba Configurações). `avaliarAtivacao` e o perfil usam 85% para item
  e 75% para brincante; o perfil retorna `freqMinima` e ajusta textos/barras.

### Acesso e login
- **Login com papel duplo:** quem é coordenação **e** item/brincante escolhe, ao
  entrar, se acessa como **Coordenação** (admin) ou como **Item/Brincante**
  (só desempenho). Login puro segue direto. `login` agora retorna `papel` e
  `podeCoord`; o front decide o papel (`entrarNoApp`/`escolherPapel`).
- **Brincante/Item** agora veem **apenas o próprio perfil** (removido o Ranking do
  menu deles) — desempenho, histórico (incl. atividades), presença, bonificação e
  ativação. Cada um loga com o próprio ID e CPF (senha), como antes.

## 2026-07-08 — Cadastro de brincantes em lote (importar planilha/CSV)

- Botão **"Carregar lista"** na aba Cadastro. Modal onde a coordenação **cola os
  dados** de uma planilha (Excel/Google Sheets) ou seleciona um **arquivo CSV**.
- Colunas (nesta ordem): **Nome** (obrigatório), Apelido, CPF, Fila, Posição,
  Tipo, Bonificação (sim/não). Detecta separador (tab/;/,) e pula cabeçalho.
- **Prévia com validação** antes de gravar (linhas sem nome são ignoradas) e botão
  para baixar um **modelo CSV**.
- Backend: novo handler **`addBrincantesLote(lista, usuario)`** (`server/handlers.js`
  + whitelist) — cria todos numa requisição só, reaproveitando `addBrincante`
  (contador transacional de IDs), e retorna criados/erros por linha.

## 2026-07-08 — Responsividade mobile (passada completa)

Revisão de CSS em `public/index.html` para o app ficar confortável em celulares.
Breakpoints em **820px** (tablet), **600px** (celular) e **400px** (celular pequeno),
somados aos que já existiam para o calendário (640px) e criação em lote.

- **Topbar** permanece em linha, compacta: logo menor, subtítulo escondido, nome
  do usuário truncado. **Nav** com botões menores e rolagem horizontal.
- **Páginas** com padding reduzido; títulos menores. **Stats** em 2 colunas.
- **Tabelas** mais densas (fonte/padding menores) — seguem rolando na horizontal
  dentro do `.table-wrap`, sem estourar a largura da tela.
- **Modais** ocupam quase toda a largura/altura no celular, com rolagem interna.
- **Chamada** e **barra flutuante de seleção** ajustadas para telas estreitas;
  removidos deslocamentos de hover que atrapalham no toque.
- Nada de novo no backend/regra; só apresentação.

## 2026-07-08 — Alinhamento com o contrato · Fases C, D e E

### Fase C — Adesão/assinatura + ativação proporcional e automática
- Brincante ganhou **`DataAssinatura`** e a **`DataAdesao`** virou editável
  (nos formulários de novo/editar). Início do período de ativação = data de adesão.
- Novo helper `avaliarAtivacao` (`server/handlers.js`): calcula o status de
  ativação **automaticamente** — janela = adesão + `mesesAtivacao`; exige 75% de
  presença e nota ≥ 4 em 75% dos ensaios da janela. Status possíveis:
  `em_ativacao`, `ativado`, `nao_ativado`, `nao_elegivel` (adesão tarde demais),
  `sem_adesao`, `sem_bonificacao`. `StatusAtivacao` deixou de ser "pendente/ativado"
  manual e virou **override**: `auto` (padrão, calcula), `ativado` (força),
  `nao_elegivel` (força). A elegibilidade da bonificação em `getPerfilBrincante` e
  `getSimulacaoBonificacao` passou a usar o cálculo. O **Perfil** ganhou um card de
  ativação (janela, presença/nota da janela, status).

### Fase D — Situação do membro + desligamento
- Brincante ganhou **`StatusMembro`** (`ativo`/`afastado`/`desligado`),
  **`MotivoDesligamento`** e **`DataDesligamento`** (editáveis no formulário, com
  seção "Situação do membro"). Motivos conforme Cláusula Oitava.
- **Desligamento com perda integral** (`penalidadeDesligamento_`): motivos
  `concorrente`, `pre_festival` e `quadrilha` zeram a bonificação (−100%). A
  penalidade efetiva é o **pior entre advertências e desligamento**
  (`penalidadeTotal_`). A tabela de brincantes mostra badge de desligado/afastado.

### Fase E — Falta justificada × injustificada
- Avaliação ganhou **`Justificada`** (booleano, só para faltas). `upsertAvaliacao`
  aceita `justificada`; `getAvaliacoes` retorna o campo. Na **chamada**, ao marcar
  falta aparece um checkbox **"justificada"** (avisou 24h) ao lado do motivo, com
  autosave. O **Perfil** marca as faltas justificadas no histórico.

## 2026-07-08 — Alinhamento com o contrato · Fase B (advertências) + atividades

### Advertências / sanções (Cláusula Sétima)
- Nova coleção **`advertencias`** (`{BrincanteID, Nivel, Motivo, Data, RegistradoPor,
  DataRegistro}`). Níveis: **verbal** (só registra), **formal** (−50%),
  **desligamento** (−100%), **gravidade extrema** (−100%). Vale o **pior nível**.
- Backend (`server/handlers.js`): `getAdvertencias`, `addAdvertencia`,
  `removeAdvertencia` + helper `penalidadeDasAdvs_`. A sanção é aplicada como
  **desconto sobre o total acumulado** (decisão do usuário) em
  `getSimulacaoBonificacao` (novos campos `valorBruto`, `sancaoPct`) e
  `getPerfilBrincante` (`bonificacaoBruta`, `sancaoPct`, `advertencias`).
- Frontend: botão **Advertências** na linha do brincante → modal que lista, mostra
  a sanção ativa, registra (nível/data/motivo) e remove. A tela de **Bonificação**
  ganhou coluna **Sanção** (mostra −% e o bruto); o **Perfil** exibe aviso quando
  há sanção.

### Atividades do compromisso (Cláusula Segunda, "l")
- Novos tipos de evento: **arrecadação, trabalho braçal, trabalho comunitário,
  outra atividade** (agrupados no seletor). Aparecem na agenda (chip roxo) e na
  chamada, com **presença registrada** normalmente.
- Essas atividades **não geram bonificação** (`valorBonifEvento_` retorna 0) e
  **não entram na frequência/nota de ensaios**: novo helper `eventosMetrica_`
  exclui atividades (e cancelados) do cálculo em `getDashboard`, `getRanking` e
  `getPerfilBrincante`. Assim a presença é acompanhada sem distorcer o 75%.

## 2026-07-08 — Alinhamento com o contrato · Fase A (config + valor por dia + período)

Início do alinhamento do sistema ao **Termo de Compromisso do Brincante** (contrato
adicionado ao projeto: `Contratos Explosao Junina Final.docx`). Roadmap acordado:
A) config + valor por evento + período de contagem (esta entrada); B) advertências/
sanções; C) adesão/assinatura + ativação proporcional e automática; D) status de
membro + desligamento com motivos; E) atividades externas + falta justificada.

### Aba Configurações (`public/index.html`)
- Nova aba **Configurações** (só admin) para editar pela interface o que antes só
  dava via script no banco: **valores** da bonificação, **metas** (frequência,
  nota, % nota, meses de ativação) e **datas** (início da temporada, início da
  contagem, fim da contagem, fim da adesão, ano). Aviso destacado de que alterar
  recalcula a bonificação de todos retroativamente. Confirmação in-app ao salvar.

### Backend (`server/handlers.js`, `netlify/functions/api.js`)
- `DEFAULT_CONFIG` ganhou **`inicioContagem`** (padrão `2026-05-01`): início da
  contagem da bonificação. Fev–abr passam a valer **só como ativação**.
- Evento ganhou **`ValorBonificacao`** (override opcional): `getEnsaios`,
  `addEnsaio` e `updateEvento` já gravam/retornam o campo.
- Novo helper `valorBonifEvento_` (usa o override do evento ou o valor padrão do
  tipo; igreja = 0) e `noPeriodoBonif_` (evento dentro de `inicioContagem`..`fimContagem`).
- **`getSimulacaoBonificacao` e `getPerfilBrincante`** agora só acumulam eventos
  **dentro do período de contagem** e usam o **valor por evento** quando definido.
  Corrige a inflação: antes contava todos os eventos, inclusive os de ativação.
- Novo handler **`updateConfigMap`** (salva várias chaves de uma vez) + whitelist.

### Frontend do evento
- Formulário de evento ganhou campo opcional **"Valor da bonificação neste dia"**
  (vazio = usa o padrão do tipo). O detalhe do evento mostra o valor quando definido.

Melhorias em cima da agenda/chamada, todas em `public/index.html`.

### Calendário
- **Chip "hoje"** no canto superior direito da célula do dia atual (além da
  borda destacada que já existia).
- **Modo "Selecionar"** (botão novo na toolbar): permite escolher **vários dias**
  de uma vez — clicando dia a dia ou **clicando e arrastando** um intervalo.
  Os dias selecionados ficam destacados e aparece uma **barra flutuante** com a
  contagem e as ações "Criar eventos" / "Limpar".
- **Criação em lote**: um formulário cria o mesmo evento (tipo, hora início/fim,
  descrição) em todos os dias selecionados de uma vez. Opção **"Personalizar cada
  dia"** revela uma lista para ajustar tipo/horário por data individualmente.
  Cria os eventos em paralelo (`addEnsaio` por data). Ao ligar "personalizar",
  os **campos principais somem** e o que já estava preenchido é copiado para cada
  linha (a Descrição segue compartilhada) — evita ambiguidade sobre qual valor
  vale na criação.
- Ao sair da aba Agenda ou trocar para a visão Lista, o modo seleção é desligado.

### Confirmações in-app
- Todas as caixas de confirmação do navegador (`confirm()`) viraram **modais do
  próprio sistema** (`confirmDialog`, retorna Promise). Aplicado em: excluir
  brincante, excluir evento e marcar evento como "não aconteceu". Clicar fora do
  modal = cancelar.

### Sessão persistente (login não cai ao atualizar)
- O login agora **persiste** (localStorage) e é restaurado ao recarregar a página.
- **Expira após 1 hora sem atividade** (mouse, teclado, toque, scroll). Um
  vigia checa a cada 30s e, se estourou o tempo, faz logout com aviso. A cada
  interação o "último uso" é atualizado (no máx. 1x a cada 20s).
- `doLogout` e a expiração limpam a sessão salva.

---

## 2026-07-08 — Agenda de eventos + chamada (Fase 1: backend)

Reformulação de Ensaios → **Agenda de eventos** e da Avaliação →
**chamada em tempo real**. Backend na fase 1; UI do calendário na fase 2;
chamada em tempo real na fase 3.

### Fase 3 — Chamada em tempo real (`public/index.html`)
- A aba de Avaliação virou **"Chamada e avaliação"**. Fluxo repensado para o
  coordenador fazer a chamada ao vivo, logo após o evento.
- **3 estados de presença** por brincante: *não marcado* (padrão) / *presente* /
  *falta*, via dois botões (clicar de novo desmarca). Antes era binário e já
  começava todo mundo presente.
- **Justificativa da falta** aparece quando o brincante é marcado como falta;
  **nota (1–5) + obs de desempenho** aparecem só para presentes. A nota fica
  destravada da presença (pode ser lançada depois).
- **Autosave a cada toque** via `upsertAvaliacao` (presença, nota, justificativa,
  obs) — não há mais botão "Salvar". Cada linha mostra um "salvo" discreto.
- **Cabeçalho do evento** com contadores ao vivo (presentes / faltas /
  marcados) e a **confirmação embutida**: fazer a chamada muda o evento de
  `planejado` → `realizado` automaticamente. Botões **"Ajustar"** (hora real de
  início/fim + observação, via `updateEvento`) e **"Não aconteceu"** (cancela o
  evento; some da frequência/bonificação). Evento cancelado mostra **"Reativar"**.
- Ao salvar, os caches derivados (dashboard, ranking, bonificação, perfil) são
  invalidados para refletir na hora.
- CSS reescrito para a grade (`.av-row` em flex com 3 estados, `.av-pgroup`,
  `.av-dyn`, `.av-saved`) e novo cabeçalho `.av-ev-*` / `.av-progress`.

### Fase 2 — Agenda com calendário (`public/index.html`)
- A seção **"Ensaios" virou "Agenda"** (menu, título, ícone). "Ensaio" agora é só
  um dos tipos de **evento**. Rótulo do dashboard: "Ensaios" → "Eventos".
- Nova **visão de calendário** (grade de mês em JS puro, sem biblioteca):
  navegação mês anterior/próximo/hoje, chips coloridos por tipo, dia de hoje
  destacado. **Clicar num dia** abre "Novo evento" com a data preenchida;
  **clicar num chip** abre o detalhe do evento.
- **Toggle Calendário ↔ Lista** na toolbar. A lista (tabela) ganhou colunas de
  **Horário** e **Status**, e eventos cancelados aparecem esmaecidos.
- **Formulário de evento** unificado (criar/editar) com data, tipo, **hora de
  início e fim** e descrição. `saveEvento` chama `addEnsaio` (novo) ou
  `updateEvento` (edição).
- **Detalhe do evento** (modal) com Data/Horário/Status/Descrição/Observação e
  ações: **Fazer chamada**, **Editar**, **Excluir**.
- CSS novo: `.agenda-toolbar`, `.view-toggle`, `.cal-*` (calendário) e
  `.chip-*` (cores por tipo), com ajustes responsivos p/ telas ≤640px.

### Fase 1 — Modelo de evento ampliado (`server/handlers.js`)
- `getEnsaios` agora retorna também `HoraInicio`, `HoraFim`, `Status`
  (`planejado`/`realizado`/`cancelado`), `HoraInicioReal`, `HoraFimReal` e
  `ObsEvento`. **Eventos antigos** não têm esses campos: `Status` ausente é
  tratado como `planejado`, então continuam contando normalmente.
- `addEnsaio` passou a gravar `HoraInicio`/`HoraFim` e nasce com
  `Status: 'planejado'`.
- **Nova função `updateEvento(id, dados, usuario)`**: edita data/tipo/descrição,
  horários planejados, `status` (cancelar/reativar) e horários reais + observação
  (o "ajuste" pós-evento). Substitui a ideia de uma etapa separada de confirmação:
  cancelar = `status: 'cancelado'`; ajustar = gravar hora real/obs.

### Chamada com autosave (`server/handlers.js`)
- **Nova função `upsertAvaliacao(eventoId, brincanteId, patch, usuario)`**: salva
  a avaliação de **um** brincante por vez (autosave a cada toque), em vez do
  `salvarAvaliacoes` que apagava tudo e regravava. `patch` aceita
  `presente` (`sim`/`nao`/`null`), `justificativa`, `nota`, `observacao`.
  `presente: null` remove o registro (estado "não marcado"). `salvarAvaliacoes`
  foi mantido por compatibilidade.

### Eventos cancelados não contam (`server/handlers.js`)
- Novo helper `filtrarCancelados_` remove eventos com `Status === 'cancelado'` e
  as avaliações ligadas a eles. Aplicado em `getDashboard`, `getRanking`,
  `getSimulacaoBonificacao` e `getPerfilBrincante` — evento que não aconteceu
  não entra em frequência, ranking nem bonificação.

### API
- `netlify/functions/api.js`: `updateEvento` e `upsertAvaliacao` adicionados à
  whitelist `PUBLICAS` (e ao `module.exports` dos handlers).

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

### Documentação e regras fixas
- Criados `CONTEXTO.md` (o que é o sistema, arquitetura, regras, infra),
  `ATUALIZACOES.md` (este histórico) e `CLAUDE.md` (regras fixas: ler o contexto
  no início de cada sessão e registrar toda mudança aqui).

### Limpeza
- `deno.lock` (gerado pelo `netlify dev`) removido do versionamento e adicionado
  ao `.gitignore`.
