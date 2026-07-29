# -*- coding: utf-8 -*-
"""Gera 'Organograma - Explosao Junina.docx'.

Passa a ter gerador (antes era o unico documento editado direto no Word, e
comecava com um paragrafo solto de conversa colado de chat). O conteudo dos
cargos e dos grupos e o do dono; o que este script acrescenta e o padrao visual
do kit, o objetivo do documento e os quadros de quem responde por que.

A imagem do organograma macro vive em `_ativos/organograma.png` — regerar o
.docx sem ela deixaria o documento sem o desenho.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["ORGANOGRAMA"],
    "Estrutura, cargos e responsabilidades · Temporada 2027",
    "Quem faz o quê na Explosão Junina de Beruri — o ano inteiro e no dia do "
    "espetáculo.",
    nota="Este documento é o coração do projeto Super Explosão. Os cargos estão "
         "definidos; os nomes de cada um serão decididos em reunião da "
         "Diretoria (previsão: agosto de 2026).",
    rodape="Beruri – Amazonas",
    cor=VERMELHO,
)

# ---------------------------------------------------------------- objetivo ---
h1(doc, "OBJETIVO DESTE DOCUMENTO", 1)
p(doc, "Organizar a Explosão. É esse o objetivo — e ele é maior do que parece, "
       "porque hoje a quadrilha funciona muito mais por dedicação individual do que "
       "por estrutura. Sempre há alguém que resolve; o problema é que é quase sempre "
       "a mesma pessoa, e ninguém sabe dizer de antemão quem é.")
caixa(doc, "O coração do projeto Super Explosão",
      "Este é o documento que começa a virar o jogo. É a partir dele que a Diretoria "
      "se organiza, que os papéis são distribuídos e que cada pessoa passa a saber "
      "exatamente o que se espera dela. Sem organograma, todo o resto da "
      "reestruturação — Arraiais, Sócio Torcedor, arrecadação, sistema, novos "
      "projetos — depende de improviso.", VERMELHO)

h2(doc, "1.1 O que este documento resolve")
for rot, txt in [
    ("Direciona a Diretoria: ", "cada diretor sabe qual é a sua alçada, o que decide "
     "sozinho e o que precisa passar por outro."),
    ("Distribui papéis: ", "as funções deixam de ser “quem estiver disponível” e "
     "passam a ter dono."),
    ("Deixa as responsabilidades claras: ", "para cada cargo e cada grupo está "
     "escrito o que ele entrega."),
    ("Mapeia as divisões necessárias: ", "tanto as do projeto de produção que roda o "
     "ano inteiro quanto as dos grupos que operam na arena, no dia do espetáculo — "
     "que são coisas diferentes e exigem gente diferente."),
    ("Evita acúmulo de função: ", "quando uma pessoa concentra três frentes, o "
     "grupo inteiro trava quando ela falta. Espalhar não é burocracia; é segurança."),
    ("Define de quem cobrar: ", "sem isso, cobra-se de todo mundo — ou seja, de "
     "ninguém. Com o organograma, cada entrega tem um responsável a quem perguntar."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "1.2 Como ele deve ser usado")
tabela(doc, ["Momento", "Como usar"], [
    ["Reunião de nomeação (agosto/2026)", "Preencher o nome de cada cargo e de cada "
     "grupo, olhando para o acúmulo de função antes de confirmar"],
    ["Início da temporada", "Cada responsável recebe a sua parte por escrito e "
     "confirma que aceitou"],
    ["Durante o ano", "Toda cobrança começa aqui: procura-se o responsável da "
     "frente, não a coordenação inteira"],
    ["Dia do espetáculo", "Vale a coluna das Equipes de Arena — quem está em qual "
     "posição e a quem obedece"],
    ["Fim da temporada", "Revisão: o que faltou, o que sobrou, que grupo precisa ser "
     "criado ou dividido"],
], larguras=[5.0, 11.0])

# ----------------------------------------------------------------- macro -----
h1(doc, "VISÃO MACRO", 2)
p(doc, "A estrutura tem quatro camadas. A Diretoria decide e responde pela "
       "quadrilha; a Comissão de Artes decide o espetáculo; os Grupos de Produção "
       "constroem durante o ano; as Equipes de Arena operam no dia.")
imagem(doc, "organograma.png", 16.0,
       "Organograma geral da Explosão Junina de Beruri")
tabela(doc, ["Camada", "O que é", "Quando funciona"], [
    ["Diretoria", "Presidência e diretores — decisão, representação e responsabilidade "
     "institucional", "O ano inteiro"],
    ["Comissão de Artes", "A própria Diretoria reunida para decidir o espetáculo",
     "Da escolha do tema até a estreia"],
    ["Grupos de Produção", "Execução do que a Comissão de Artes definiu",
     "O ano inteiro"],
    ["Equipes de Arena", "Operação do espetáculo", "No dia da apresentação"],
], larguras=[4.0, 8.0, 4.0])

# -------------------------------------------------------------- diretoria ----
doc.add_page_break()
h1(doc, "DIRETORIA", 3)
p(doc, "A Diretoria é quem responde pela quadrilha — para dentro e para fora. Cada "
       "cargo tem alçada própria: o que está na coluna do meio é decisão dele, e o "
       "que está na coluna da direita é o que se cobra dele.")

h3(doc, "Presidente")
p(doc, "Representação institucional externa, assinatura final de contratos e "
       "documentos oficiais, decisão de última instância em conflitos entre grupos. "
       "É quem “bate o martelo” quando algo passa da alçada dos outros diretores.")

h3(doc, "Vice-Presidente")
p(doc, "Suplência direta do Presidente (assume ausências e impedimentos) e apoio na "
       "representação institucional. Papel de continuidade — evita que a estrutura "
       "trave se o Presidente estiver indisponível.")

h3(doc, "Diretor Financeiro")
p(doc, "Orçamento, controle de gastos, prestação de contas, pagamento de "
       "fornecedores e colaboradores contratados. Assina e formaliza qualquer valor "
       "acordado por outros diretores (por exemplo, o cachê de um show negociado "
       "pelo Diretor de Eventos). Tem acesso de leitura ao painel de Bonificação do "
       "sistema.")

h3(doc, "Diretor Secretário")
p(doc, "Atas de reunião, documentação oficial, ofícios, registro formal das decisões "
       "da Diretoria e da Comissão de Artes. É quem formaliza por escrito o que foi "
       "decidido — sem ele, decisão importante fica só na palavra.")

h3(doc, "Diretor de Eventos")
p(doc, "Relações externas, negociação e fechamento de shows em outros municípios, "
       "contratos de apresentação. Negocia o acordo, mas o valor final passa pelo "
       "Financeiro para formalização e pagamento.")

h3(doc, "Diretor de Tecnologia")
p(doc, "Sistemas web (Sistema de Avaliação, Site do Sócio Torcedor, Cine Explosão), "
       "site e toda a parte de hardware e mecânica aplicada ao espetáculo — LEDs de "
       "figurino, mecanismos de alegoria, tecnologia embarcada na arena. Também tem "
       "assento na Comissão de Artes, contribuindo com a viabilidade técnica das "
       "ideias criativas.")

h2(doc, "3.1 Quadro de alçadas")
tabela(doc, ["Cargo", "Decide sozinho", "O que se cobra"], [
    ["Presidente", "Conflito entre grupos, representação da quadrilha, palavra final",
     "Que a decisão exista e seja comunicada"],
    ["Vice-Presidente", "O que o Presidente decidiria, na ausência dele",
     "Que a estrutura não pare quando faltar o Presidente"],
    ["Financeiro", "Autorização de despesa dentro do orçamento aprovado",
     "Orçamento em dia, contas pagas e prestação de contas publicada"],
    ["Secretário", "Forma e registro dos documentos",
     "Ata de cada reunião e arquivo organizado"],
    ["Eventos", "Condução das negociações externas",
     "Agenda de apresentações fechada e contratos assinados"],
    ["Tecnologia", "Arquitetura e prioridades dos sistemas e da tecnologia de arena",
     "Sistemas no ar, dados corretos e o que foi prometido para a arena funcionando"],
], larguras=[3.5, 6.0, 6.5])
caixa(doc, "A regra dos dois olhares para dinheiro",
      "Nenhum diretor fecha valor sozinho. Quem negocia (Eventos, por exemplo) não é "
      "quem formaliza e paga (Financeiro). Não é desconfiança: é o que protege as "
      "duas pessoas quando alguém perguntar quanto foi e por quê.", AMBAR)

# ------------------------------------------------------- comissao de artes ---
h1(doc, "COMISSÃO DE ARTES", 4)
p(doc, "Não é um cargo — é a própria Diretoria reunida, com um responsável designado "
       "para conduzir a pauta do dia a dia, evitando que toda decisão pequena "
       "dependa de reunião coletiva.")
p(doc, "Decide: tema do ano, história e roteiro, atos, script do espetáculo de "
       "arena, estética, cores, conceito de figurino e de alegoria por ato. A partir "
       "dessas decisões, formaliza os Grupos de Produção.")
caixa(doc, "Por que ela existe separada da Diretoria",
      "Administrar a quadrilha e criar o espetáculo são trabalhos de natureza "
      "diferente. Misturar os dois na mesma reunião faz o assunto urgente (dinheiro, "
      "prazo, ofício) engolir o assunto importante (o que a Explosão vai contar este "
      "ano). Separar a pauta garante que o espetáculo tenha hora marcada para ser "
      "pensado.", ROXO)

# ------------------------------------------------------ grupos de producao ---
doc.add_page_break()
h1(doc, "GRUPOS DE PRODUÇÃO (ano todo)", 5)
p(doc, "São as frentes que executam o que a Comissão de Artes definiu. Trabalham "
       "durante todo o ano e cada uma precisa de um responsável nomeado.")

tabela(doc, ["Grupo", "O que faz", "Entrega"], [
    ["Alegorias e Cenário",
     "Desenho e construção física das alegorias e do cenário definidos pela Comissão "
     "de Artes, incluindo o planejamento de translado até o local da apresentação",
     "Alegoria pronta, testada e transportada"],
    ["Figurino",
     "Desenho e confecção das indumentárias e figurinos conforme o conceito estético "
     "definido pela Comissão",
     "Figurino de cada brincante pronto e provado"],
    ["Música e Coreografia",
     "Coordenação de dança, planejamento de ensaios, criação de coreografia, escolha "
     "de repertório e trilha sonora entre atos, gravação do áudio do teatro",
     "Coreografia montada e áudio final gravado"],
    ["Planejamento de Arena e Cronograma",
     "Calcula o tamanho da arena, define onde cada coisa e cada brincante fica "
     "posicionado e planeja a duração de cada etapa: montagem de cenário e alegoria, "
     "tempo de show e desmontagem",
     "Mapa da arena e cronômetro do espetáculo"],
    ["Comunicação",
     "Divulgação do grupo e do espetáculo, com a equipe de designers e jornalista",
     "Presença constante nas redes e cobertura dos eventos"],
], larguras=[3.5, 8.5, 4.0])

caixa(doc, "Grupos que ainda precisam ser formalizados",
      "A reestruturação de 2027 criou frentes que não existiam quando este "
      "organograma nasceu e que hoje estão sem dono claro: o Programa Sócio "
      "Torcedor, os projetos de arrecadação, a produção dos Arraiais (Lançamento e "
      "Explosão) e a captação de parcerias e patrocínio. Enquanto não tiverem "
      "responsável nomeado, caem sobre quem sobrar — que é exatamente o que este "
      "documento existe para evitar.", AMBAR)

# --------------------------------------------------------- equipes de arena --
h1(doc, "EQUIPES DE ARENA (dia do espetáculo)", 6)
p(doc, "No dia do espetáculo a estrutura muda. Não há tempo para consultar "
       "diretoria: existe uma cadeia de comando curta e cada equipe age no momento "
       "exato em que é chamada.")

tabela(doc, ["Equipe", "O que faz na arena"], [
    ["Regência de Cena", "Comanda em tempo real durante a apresentação — distribui "
     "função e indica o momento exato de cada equipe agir. É a autoridade central no "
     "dia do show"],
    ["Equipe de Palco", "Empurra alegoria, abre e fecha painel de cenário"],
    ["Efeitos e Movimentação Mecânica", "Aciona efeitos especiais e comanda a "
     "movimentação mecânica das alegorias (por exemplo, o mecanismo da onda do São "
     "Pedro)"],
    ["Figurino e Camarim", "Troca de figurino em cena, sincronizada com os atos"],
    ["Adereços em Cena", "Recolhe adereços e peças de figurino que caem na arena "
     "durante a dança"],
    ["Som", "Sonoplastia, playback e sincronia direta com a Regência"],
], larguras=[4.5, 11.5])

caixa(doc, "No dia do show, quem manda é a Regência de Cena",
      "Presidente, diretores e coordenadores obedecem à Regência durante a "
      "apresentação. Não é hierarquia invertida: é a única forma de um espetáculo "
      "com dezenas de pessoas e alegorias em movimento não ter duas ordens "
      "diferentes ao mesmo tempo.", VERMELHO)

# --------------------------------------------------------------- as regras ---
doc.add_page_break()
h1(doc, "REGRAS DE FUNCIONAMENTO", 7)
for rot, txt in [
    ("Todo grupo tem um responsável nomeado: ", "grupo sem nome na frente é grupo "
     "sem dono, e trabalho sem dono não acontece."),
    ("Ninguém acumula duas frentes sem decisão registrada: ", "se for inevitável, a "
     "Diretoria registra em ata que é temporário e por quanto tempo."),
    ("Quem participa de grupo de produção pode dançar: ", "o organograma não tira "
     "ninguém da arena — organiza o trabalho de fora dela."),
    ("Cada frente responde ao diretor da área: ", "e o diretor responde à Diretoria. "
     "A cobrança sobe por esse caminho, não por atalho."),
    ("Decisão da Comissão de Artes vira tarefa: ", "toda decisão sai da reunião com "
     "grupo responsável e prazo, registrados pelo Secretário."),
    ("O que muda no meio da temporada é anotado: ", "troca de responsável sem "
     "registro é a origem mais comum de tarefa que ninguém fez."),
]:
    bullet(doc, txt, rotulo=rot)

h1(doc, "QUADRO DE NOMEAÇÃO", 8)
p(doc, "A ser preenchido na reunião da Diretoria (previsão: agosto de 2026). Enquanto "
       "estiver em branco, a função não tem dono.")
tabela(doc, ["Função", "Nome", "Contato", "Aceitou em"], [
    ["Presidente", "", "", ""],
    ["Vice-Presidente", "", "", ""],
    ["Diretor Financeiro", "", "", ""],
    ["Diretor Secretário", "", "", ""],
    ["Diretor de Eventos", "", "", ""],
    ["Diretor de Tecnologia", "", "", ""],
    ["Condução da Comissão de Artes", "", "", ""],
    ["Grupo de Alegorias e Cenário", "", "", ""],
    ["Grupo de Figurino", "", "", ""],
    ["Grupo de Música e Coreografia", "", "", ""],
    ["Planejamento de Arena e Cronograma", "", "", ""],
    ["Comunicação", "", "", ""],
    ["Programa Sócio Torcedor", "", "", ""],
    ["Projetos de Arrecadação", "", "", ""],
    ["Produção dos Arraiais", "", "", ""],
    ["Parcerias e Patrocínio", "", "", ""],
    ["Regência de Cena", "", "", ""],
    ["Equipe de Palco", "", "", ""],
    ["Efeitos e Movimentação Mecânica", "", "", ""],
    ["Figurino e Camarim", "", "", ""],
    ["Adereços em Cena", "", "", ""],
    ["Som", "", "", ""],
], larguras=[6.0, 4.5, 3.5, 2.0])

checklist(doc, [
    "Levar o organograma à reunião da Diretoria",
    "Nomear cada cargo e cada grupo, um a um",
    "Verificar quem ficou com mais de uma função e redistribuir",
    "Formalizar as frentes novas (Sócio Torcedor, arrecadação, arraiais, parcerias)",
    "Entregar por escrito a cada responsável o que ele assumiu",
    "Registrar tudo em ata (Diretor Secretário)",
    "Publicar a estrutura para todos os brincantes",
    "Revisar ao fim da temporada",
], titulo="PRÓXIMOS PASSOS")

citacao(doc, "Quadrilha não trava por falta de gente. Trava por falta de quem "
             "responda por cada coisa.")
p(doc, "Explosão Junina de Beruri · Organograma", centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Organograma - Explosão Junina.docx")
