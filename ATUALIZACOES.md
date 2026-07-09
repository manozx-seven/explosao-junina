# ATUALIZAÇÕES — Sistema de Avaliação · Explosão Junina

> Histórico de tudo que foi feito no projeto, do mais recente para o mais antigo.
> **Regra fixa:** toda modificação no projeto deve ser registrada aqui (ver `CLAUDE.md`).
> Formato de cada entrada: data, título e o que mudou / por quê.

---

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
