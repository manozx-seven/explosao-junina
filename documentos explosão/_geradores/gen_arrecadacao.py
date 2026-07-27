# -*- coding: utf-8 -*-
"""Gera 'Projetos Arrecadacao Explosao Junina.docx' — portfolio em stand by."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["PROJETOS DE", "ARRECADAÇÃO"],
    "Portfólio em stand by · Temporada 2027",
    "Projetos prontos para serem acionados quando houver necessidade.",
    nota="Este documento não é um calendário. É uma reserva: cada projeto fica "
         "documentado e pronto, e só é executado por decisão da Diretoria.",
    rodape="Beruri – Amazonas",
)

# ------------------------------------------------------------- novo modelo --
h1(doc, "O QUE MUDOU NESTE DOCUMENTO")
p(doc, "Até aqui, a arrecadação era a base do custeio da Explosão: rifa, bingo, "
       "venda de comida e eventos aconteciam o ano todo, quase sempre no aperto, "
       "competindo com o tempo de ensaio e sem previsibilidade de caixa.")
p(doc, "Com os repasses municipais, estaduais e federais, a quadrilha passou a ter "
       "folga para planejar o espetáculo. E com o Programa Sócio Torcedor passou a "
       "ter uma receita recorrente e previsível. Isso muda o papel destes projetos: "
       "eles deixam de ser rotina e viram reserva estratégica.")

tabela(doc, ["Antes", "Agora"], [
    ["Arrecadação era a base do custeio",
     "A base são os repasses públicos e o Sócio Torcedor"],
    ["Vários projetos acontecendo ao mesmo tempo",
     "Foco em três frentes: Sócio Torcedor, Arraial de Lançamento e Arraial da Explosão"],
    ["Projeto puxado pela urgência, sem planejamento",
     "Projeto acionado por decisão, com responsável e reunião de planejamento"],
    ["Brincante em campanha permanente de venda",
     "Brincante convocado pontualmente, sem competir com o ensaio"],
    ["Documento de execução mensal",
     "Documento de consulta: fica de stand by até que se decida acionar"],
], larguras=[8.0, 8.0])

banner(doc, "REGRA DE OURO DESTE DOCUMENTO",
       "Nenhum projeto daqui começa sem decisão da Diretoria, responsável designado e reunião de planejamento.",
       VERMELHO)

# ------------------------------------------------------------- quando/como --
h1(doc, "QUANDO ACIONAR UM PROJETO")
p(doc, "Não se faz arrecadação por hábito. Um projeto deste documento é acionado "
       "quando existe um motivo concreto:")
tabela(doc, ["Gatilho", "O que significa", "Exemplo"], [
    ["Urgência de caixa", "Despesa não prevista que não pode esperar",
     "Conserto ou reforço de alegoria, som extra, transporte de emergência"],
    ["Meta específica", "Um objetivo com valor definido",
     "Custear a viagem de uma apresentação fora de Beruri"],
    ["Oportunidade", "Data com público garantido na cidade",
     "Feriado, festa da comunidade, movimento de fim de ano"],
    ["Reforço pré-Festival", "Fechar a conta da montagem final",
     "Últimos materiais de figurino e alegoria"],
    ["Engajamento", "Ação que também aproxima a comunidade",
     "Cinema na praça, ensaio aberto"],
], larguras=[3.5, 5.5, 7.0])

h1(doc, "COMO ACIONAR (O RITO)")
for i, (rot, txt) in enumerate([
    ("Alguém propõe: ", "qualquer diretor ou responsável de grupo leva a proposta à "
     "Diretoria, com o motivo e o valor pretendido."),
    ("A Diretoria decide: ", "aprova ou não, e registra em ata. Sem ata, o projeto não "
     "está autorizado."),
    ("Um responsável é designado: ", "uma pessoa com nome responde pelo projeto do "
     "começo ao fim."),
    ("Reunião de planejamento: ", "data, equipe, materiais, preços, metas e escala "
     "definidos antes de qualquer compra."),
    ("Execução: ", "conforme o checklist da ficha do projeto."),
    ("Mini-balanço: ", "receitas, custos e resultado fechados logo depois e entregues ao "
     "Diretor Financeiro."),
    ("Publicação: ", "o resultado é publicado nas redes — faz parte da transparência da "
     "quadrilha."),
], start=1):
    numero(doc, txt, rotulo=rot)

h1(doc, "QUAL PROJETO ESCOLHER")
p(doc, "Comparação rápida para a Diretoria decidir com base no que se precisa: "
       "dinheiro rápido, dinheiro alto ou aproximação com a comunidade.")
tabela(doc, ["Projeto", "Esforço", "Retorno", "Tempo de montagem", "Quando faz sentido"], [
    ["Rifa", "Baixo", "Médio", "1 a 3 semanas",
     "Precisa de dinheiro sem montar evento; todo brincante ajuda a vender"],
    ["Bingo", "Médio", "Médio a alto", "2 a 4 semanas",
     "Há público disponível e espaço para uma noite de evento"],
    ["Venda de comidas", "Baixo", "Baixo por vez, bom no acumulado", "Dias",
     "Reforço rápido e recorrente, com pouca gente"],
    ["Cinema na praça", "Médio", "Médio", "2 a 3 semanas",
     "Quer arrecadar e ao mesmo tempo aparecer para a comunidade"],
    ["Cine Explosão", "Alto", "Alto", "1 a 2 meses",
     "Meta grande e tempo para organizar; é o projeto mais ambicioso"],
    ["Ações com parceiros", "Baixo", "Variável", "Dias",
     "Há parceiro disposto a dividir custo e divulgação"],
], larguras=[3.0, 2.0, 2.5, 3.0, 5.5], tam=9.5)

# ------------------------------------------------------------------- rifas --
doc.add_page_break()
banner(doc, "RIFAS", "Versátil, baixo custo, alta margem", VERMELHO)
h2(doc, "O que é")
p(doc, "Venda de bilhetes numerados com sorteio de prêmios. Pode seguir diferentes "
       "linhas temáticas, cada uma com apelo para um público diferente. É o projeto "
       "mais fácil de acionar: não precisa de estrutura, só de organização.")
h2(doc, "Linhas de rifa")
tabela(doc, ["Linha", "Prêmios", "Público-alvo"], [
    ["Rifa de Doces", "Cestas de chocolates, bolos, brigadeiros, tortas",
     "Famílias, jovens, crianças"],
    ["Rifa de Comidas", "Marmitas, cestas básicas, frangos, bolos salgados",
     "Famílias, adultos"],
    ["Rifa Prêmios Variados", "Eletrônicos, vouchers, produtos de parceiros", "Público geral"],
    ["Rifa em Dinheiro", "Prêmio em espécie", "Todos"],
    ["Rifa com Desconto", "Vale-desconto em comércios parceiros (custo compartilhado)",
     "Clientes dos parceiros"],
], larguras=[4.0, 7.0, 5.0])
h2(doc, "Planejamento (reunião obrigatória)")
for rot, txt in [
    ("Data do sorteio: ", "quando e onde vai acontecer."),
    ("Linha da rifa: ", "qual tipo de prêmio (pode combinar mais de uma linha)."),
    ("Valor do bilhete: ", "preço acessível para Beruri."),
    ("Quantidade de bilhetes: ", "quantos imprimir no total."),
    ("Distribuição: ", "quantos bilhetes cada brincante fica responsável por vender."),
    ("Canais de venda: ", "presencial (porta a porta, ensaios, eventos) e online."),
    ("Premiação: ", "quais prêmios e quem vai conseguir ou comprar."),
    ("Produção: ", "quem faz o design dos bilhetes, quem imprime e quem corta."),
    ("Contabilidade: ", "registrar custos (impressão, prêmios) e receitas (vendas)."),
    ("Prestação de contas: ", "cada brincante devolve o dinheiro e os bilhetes não vendidos."),
]:
    bullet(doc, txt, rotulo=rot)
checklist(doc, [
    "Definir data, linha e valor do bilhete",
    "Conseguir ou comprar os prêmios",
    "Criar o design dos bilhetes",
    "Imprimir e cortar os bilhetes",
    "Distribuir bilhetes aos brincantes (registrar quantidade por pessoa)",
    "Estabelecer prazo para devolução do dinheiro e dos bilhetes",
    "Realizar o sorteio na data marcada",
    "Contabilizar receitas e custos",
    "Publicar resultado e balanço",
])

# ------------------------------------------------------------------- bingo --
doc.add_page_break()
banner(doc, "BINGO", "Evento social + arrecadação", AZUL)
h2(doc, "O que é")
p(doc, "Evento presencial com venda de cartelas e premiação por rodada. Além da "
       "arrecadação com as cartelas, gera receita com a venda de alimentação e "
       "bebidas no local — que muitas vezes é onde está o lucro maior.")
h2(doc, "Planejamento (reunião obrigatória)")
for rot, txt in [
    ("Local e data: ", "espaço amplo (praça, salão, escola), preferencialmente à noite."),
    ("Número de rodadas: ", "5 a 10 rodadas, com prêmios crescentes."),
    ("Valor da cartela: ", "preço simbólico, pensado para o público de Beruri."),
    ("Prêmios por rodada: ", "doados por parceiros ou comprados."),
    ("Venda de comida e bebida: ", "cardápio, preços e equipe de preparo e venda."),
    ("Sistema de sorteio: ", "globo e bolas, ou solução equivalente."),
    ("Apresentador: ", "quem conduz o bingo — voz e animação fazem diferença."),
    ("Contabilidade: ", "custos (prêmios, ingredientes) x receitas (cartelas, comida)."),
]:
    bullet(doc, txt, rotulo=rot)
checklist(doc, [
    "Definir local, data e horário",
    "Conseguir prêmios (compra ou parceiros)",
    "Produzir ou comprar as cartelas",
    "Definir cardápio e comprar ingredientes",
    "Montar equipe: apresentador, vendedores, cozinha",
    "Divulgar nas redes sociais e boca a boca",
    "Montar a estrutura no local (mesas, cadeiras, som)",
    "Realizar o evento",
    "Contabilizar receitas e custos",
    "Publicar balanço",
])

# ---------------------------------------------------------------- comidas ---
doc.add_page_break()
banner(doc, "VENDA DE COMIDAS", "Simples, econômico, recorrente", LARANJA)
h2(doc, "O que é")
p(doc, "Venda de batata frita e outras comidas na saída das missas ou em pontos de "
       "movimento. É o projeto mais simples e econômico: baixo investimento, poucas "
       "pessoas e margem alta. Pode ser repetido sempre que houver necessidade.")
h2(doc, "O que precisa")
for rot, txt in [
    ("Material: ", "batatas, óleo, sal, embalagens, guardanapos."),
    ("Equipamento: ", "fogão ou fogareiro, panela grande, escumadeira."),
    ("Equipe mínima: ", "2 a 3 pessoas (uma frita, uma embala, uma vende)."),
    ("Local: ", "saída das missas é o ponto ideal — fluxo garantido de pessoas."),
    ("Preço: ", "definido por porção, conforme o custo do dia."),
]:
    bullet(doc, txt, rotulo=rot)
h2(doc, "Planejamento")
for txt in [
    "Definir os dias de venda e a escala de quem frita, embala e vende (rotativa).",
    "Comprar material em quantidade para reduzir o custo unitário.",
    "Registrar custos e receitas a cada dia de venda.",
    "Avaliar variações: pastel, churros, tapioca, bebidas geladas.",
]:
    bullet(doc, txt)
checklist(doc, [
    "Definir dias e horários de venda",
    "Comprar ingredientes e embalagens",
    "Definir escala de brincantes por dia",
    "Conseguir equipamento (fogão, panela)",
    "Definir preço por porção",
    "Vender no ponto definido",
    "Contabilizar custos e receitas do dia",
])

# ------------------------------------------------------------ cinema praça --
doc.add_page_break()
banner(doc, "CINEMA NA PRAÇA", "Evento cultural + arrecadação", VERDE)
h2(doc, "O que é")
p(doc, "Exibição de filmes ao ar livre em tela grande na praça pública. O público "
       "paga um valor simbólico pela cadeira (ou entra de graça) e consome pipoca, "
       "refrigerante, suco e doces vendidos pela quadrilha. Evento simples, atrativo "
       "e com boa margem — e ainda coloca a Explosão no meio da comunidade.")
tabela(doc, ["Modelo A", "Modelo B", "Recomendado"], [
    ["Cadeira com valor simbólico + venda de consumo", "Cadeira grátis + venda de consumo",
     "Modelo A: gera receita dupla e o valor é simbólico"],
], larguras=[5.5, 5.0, 5.5])
h2(doc, "Sessões temáticas")
for rot, txt in [
    ("Infantil: ", "animações para crianças e famílias — costuma ser a sessão mais cheia."),
    ("Romântico: ", "filmes de romance, bom para datas comemorativas."),
    ("Ação: ", "filmes de ação e aventura para o público jovem."),
    ("Patrocinado: ", "cada sessão pode ter um patrocinador diferente do Kit Parceiro."),
]:
    bullet(doc, txt, rotulo=rot)
checklist(doc, [
    "Definir data, local e horário",
    "Conseguir projetor (empréstimo de escola ou parceiro)",
    "Conseguir tela ou superfície branca",
    "Conseguir caixa de som",
    "Selecionar os filmes (adequados ao público)",
    "Definir cardápio e comprar ingredientes",
    "Definir preços e promoções (combos)",
    "Conseguir cadeiras (empréstimo da igreja, escola ou levar as próprias)",
    "Divulgar nas redes sociais e boca a boca",
    "Montar equipe: projeção, vendas, organização",
    "Contabilizar receitas e custos",
    "Publicar balanço",
])

# --------------------------------------------------------------- cine expl ---
doc.add_page_break()
banner(doc, "CINE EXPLOSÃO", "Projeto estruturado de grande porte", ROXO)
h2(doc, "O que é")
p(doc, "O projeto mais ambicioso do portfólio: um cinema multi-sala montado dentro "
       "de uma escola parceira, com sessões infantis e adultas, venda de ingressos "
       "online e presencial e venda de alimentos. Repetível e escalável a cada "
       "edição — mas exige mais tempo de preparação e mais gente.")
h2(doc, "Locais propostos")
tabela(doc, ["Local", "Uso"], [
    ["Escola Municipal Castelo Branco",
     "Salas de aula como salas de cinema (sessões infantis e adultas). Contrapartida: a "
     "quadrilha se apresenta nas festas da escola"],
    ["Centro Comunitário Irmã Cristina Noskoski",
     "Sessão especial noturna. Espaço maior, para sessão premium ou filme de destaque"],
], larguras=[6.0, 10.0])
h2(doc, "Infraestrutura necessária")
tabela(doc, ["Item", "Quantidade", "Como conseguir"], [
    ["Projetor / datashow", "1 por sala em uso", "Empréstimo das escolas"],
    ["Notebook", "1 por sala", "Empréstimo de membros ou parceiros"],
    ["Caixa de som", "Pelo menos 1 por sala", "Empréstimo ou aluguel"],
    ["Cobertura para janelas", "Por sala (todas as frestas)", "Papelão ou papel alumínio"],
    ["Cadeiras", "As da própria sala", "Já disponíveis na escola"],
    ["Numeração de cadeiras", "Todas as cadeiras e salas", "Etiquetas ou fita adesiva"],
], larguras=[5.0, 4.5, 6.5])
h2(doc, "Ingressos e consumo")
for rot, txt in [
    ("Online: ", "sistema de venda próprio — o cliente escolhe sessão, filme, sala e "
     "cadeira, e paga por Pix."),
    ("Presencial: ", "parte das cadeiras reservada para venda na hora, em dinheiro ou Pix."),
    ("Numeração: ", "todas as salas e cadeiras numeradas; o ingresso indica sala, cadeira, "
     "sessão e horário."),
    ("Consumo: ", "pipoca (doce e salgada), refrigerante, suco, água, doces e combos "
     "promocionais. Ponto de venda na entrada ou no corredor, nunca dentro das salas."),
]:
    bullet(doc, txt, rotulo=rot)
h2(doc, "Divulgação")
for rot, txt in [
    ("Redes sociais: ", "artes com programação, horários, filmes e preços; contagem "
     "regressiva nos stories."),
    ("Convites impressos nas escolas: ", "fundamental. Entregar convites para os alunos "
     "levarem para casa impulsiona as vendas de forma significativa."),
    ("Boca a boca: ", "brincantes divulgam para família e amigos."),
]:
    bullet(doc, txt, rotulo=rot)
checklist(doc, [
    "Fechar parceria com a escola e o centro comunitário",
    "Definir a data do evento",
    "Conseguir projetores, notebooks e caixas de som (1 por sala)",
    "Selecionar filmes por classificação e preparar nos notebooks",
    "Cobrir janelas e frestas das salas",
    "Posicionar projeção e som em cada sala",
    "Numerar todas as cadeiras e identificar as salas",
    "Criar e lançar o sistema de venda online",
    "Definir a quantidade de cadeiras para venda presencial",
    "Criar, imprimir e distribuir convites nas escolas",
    "Criar artes de divulgação para as redes",
    "Definir cardápio, preços e promoções de consumo",
    "Comprar ingredientes",
    "Definir equipe por função: direção, projeção, vendas, cozinha, organização",
    "Testar som e projeção antes do evento",
    "Realizar o evento",
    "Contabilizar todos os custos e receitas",
    "Publicar balanço e registro fotográfico",
])

# ------------------------------------------------------------ público geral --
doc.add_page_break()
h1(doc, "AÇÕES PARA O PÚBLICO GERAL")
p(doc, "Além dos projetos acima, existem ações leves que podem acontecer a qualquer "
       "momento, com pouca estrutura, e que servem tanto para arrecadar quanto para "
       "aproximar a comunidade da quadrilha.")
for rot, txt in [
    ("Venda de camisa e produtos oficiais: ", "camisa da temporada, camisa de torcedor, "
     "leque, chapéu e brindes. Vende o ano todo, não só no lançamento."),
    ("Ensaio aberto: ", "público assiste a um ensaio, com venda de comida e bebida no "
     "local — e ainda vira conteúdo para as redes."),
    ("Promoções com parceiros: ", "combos e descontos em comércios parceiros, com parte "
     "revertida para a quadrilha."),
    ("Vaquinha para item específico: ", "campanha online para uma meta concreta e "
     "visível (um figurino, um equipamento de som, uma alegoria)."),
    ("Torneio esportivo beneficente: ", "futebol ou futsal com inscrição paga, boa para "
     "a entressafra."),
]:
    bullet(doc, txt, rotulo=rot)
caixa(doc, "Atenção ao tempo do brincante",
      "Toda ação para o público geral precisa caber no calendário de ensaios. Se "
      "conflita com o preparo do espetáculo, ou muda de data, ou não acontece. O "
      "espetáculo é a prioridade da temporada.", AMBAR)

# ------------------------------------------------------- saiu deste documento
h1(doc, "O QUE SAIU DESTE DOCUMENTO")
p(doc, "Três frentes que antes eram tratadas aqui viraram documentos próprios, "
       "porque deixaram de ser “projetos de arrecadação” e passaram a ser pilares da "
       "temporada:")
tabela(doc, ["Frente", "Onde está agora", "Por quê"], [
    ["Programa Sócio Torcedor", "“Programa Sócio Torcedor — Plano de Implementação”",
     "Virou o carro-chefe da arrecadação: receita recorrente o ano todo"],
    ["Arraial de Lançamento", "“Arraial de Lançamento — Plano do Evento”",
     "É a abertura oficial da temporada e a prestação de contas anual"],
    ["Arraial da Explosão", "“Arraial da Explosão — Plano do Evento”",
     "É projeto cultural e tradição da cidade, não só arrecadação"],
    ["Parcerias comerciais", "“Kit Parceiro”",
     "Passaram a sustentar o Sócio Torcedor e as ações para o público geral"],
], larguras=[4.0, 6.5, 5.5])

# ---------------------------------------------------------------- regras -----
h1(doc, "REGRAS GERAIS PARA TODOS OS PROJETOS")
tabela(doc, ["Regra", "O que significa"], [
    ["1. Todo gasto é registrado",
     "Sem nota, sem recibo, sem registro: não existiu. A transparência é inegociável"],
    ["2. Todo projeto gera mini-balanço",
     "Custos, receitas e resultado líquido — publicados nas redes"],
    ["3. Todos participam",
     "Brincantes, itens e coordenação. Quem dança também vende, monta, carrega e limpa, "
     "conforme o Termo de Compromisso"],
    ["4. Reunião antes, balanço depois",
     "Nenhum projeto começa sem reunião de planejamento nem termina sem prestação de contas"],
    ["5. Registrar para aprender",
     "O que funcionou, o que não funcionou e o que melhorar. Esse registro é patrimônio da "
     "quadrilha para os anos seguintes"],
], larguras=[4.5, 11.5])

citacao(doc, "Cada real arrecadado é um passo mais perto do palco.")
p(doc, "Explosão Junina de Beruri · Temporada 2027", centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Projetos Arrecadacao Explosao Junina.docx")
