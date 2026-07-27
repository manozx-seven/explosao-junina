# -*- coding: utf-8 -*-
"""Gera 'Programa Socio Torcedor - Plano de Implementacao.docx'."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["PROGRAMA SÓCIO TORCEDOR", "PLANO DE IMPLEMENTAÇÃO"],
    "O carro-chefe da arrecadação · Temporada 2027",
    "Como o programa vai funcionar por dentro: operação, papéis, metas e sistema.",
    nota="Documento interno. Complementa o material de divulgação “Programa Sócio "
         "Torcedor”, que é a peça voltada ao público. Prazos são previsões.",
    rodape="Beruri – Amazonas",
)

# ------------------------------------------------------------- por que ------
h1(doc, "POR QUE É O CARRO-CHEFE", 1)
p(doc, "A Explosão passou anos vivendo de arrecadação pontual: rifa, bingo, venda de "
       "comida — sempre no aperto, sempre consumindo o tempo dos brincantes. Com os "
       "repasses públicos cobrindo a montagem do espetáculo, a quadrilha pode agora "
       "construir algo que nunca teve: uma receita própria, previsível e que entra o "
       "ano todo.")
p(doc, "Esse é o papel do Sócio Torcedor. Ele não substitui os repasses nem os "
       "eventos — ele dá à quadrilha independência para decidir, reagir a imprevistos "
       "e planejar o ano seguinte sem depender de uma verba chegar na hora certa.")
tabela(doc, ["Vantagem", "O que isso resolve"], [
    ["Receita recorrente", "Entra todo mês, não só na temporada do Festival"],
    ["Previsibilidade", "Dá para planejar o orçamento sabendo com quanto se pode contar"],
    ["Custo de operação baixo", "Não exige montar evento, comprar material nem parar o ensaio"],
    ["Comunidade", "Transforma público em torcida organizada e fiel à quadrilha"],
    ["Argumento para parceiros", "Uma base de sócios ativa é audiência — e isso vale para o comércio"],
    ["Transparência como produto", "O sócio acompanha as contas: apoiar vira algo confiável"],
], larguras=[5.0, 11.0])

# ------------------------------------------------------------- o programa ---
h1(doc, "O QUE JÁ ESTÁ DEFINIDO", 2)
p(doc, "O desenho do programa está no material de divulgação. Resumo do que vale "
       "como base — valores e benefícios podem ser ajustados pela coordenação a cada "
       "temporada.")
tabela(doc, ["Nível", "Por mês", "Por temporada", "Benefícios"], [
    ["Fogueira", "R$ 5", "R$ 50",
     "Carteirinha, Close Friends, sorteios, descontos e acesso à prestação de contas"],
    ["Bandeirinha", "R$ 10", "R$ 100", "Tudo do Fogueira + brinde da temporada"],
    ["Estrela do Arraial", "R$ 20", "R$ 200",
     "Tudo do Bandeirinha + blusa “Sócio Torcedor” com o nome nas costas + bastidores e "
     "encontro com a quadrilha"],
], larguras=[3.5, 2.2, 2.8, 7.5])
for rot, txt in [
    ("Contribuição: ", "mensal ou por temporada, à escolha do torcedor."),
    ("Adesão: ", "Pix + cadastro na lista oficial (e, quando o site estiver no ar, pela "
     "própria plataforma)."),
    ("Mudança de nível: ", "o sócio pode subir ou descer de nível quando quiser."),
    ("Sorteios: ", "todos concorrem com a mesma chance, independentemente do nível."),
    ("Sem juros e sem multa: ", "quem atrasa não paga nada a mais — apenas não bate a "
     "meta do mês para efeito de troféu."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------------ metas ---
h1(doc, "METAS E CENÁRIOS", 3)
p(doc, "Os números abaixo são cenários para dimensionar o programa, não promessas. "
       "A distribuição usada é a mesma proporção em todos os cenários (60% Fogueira, "
       "30% Bandeirinha, 10% Estrela).")
tabela(doc, ["Cenário", "Sócios", "Receita mensal", "Receita anual aproximada"], [
    ["Início", "50", "R$ 400", "R$ 4.800"],
    ["Meta da temporada", "100", "R$ 800", "R$ 9.600"],
    ["Consolidado", "200", "R$ 1.600", "R$ 19.200"],
    ["Sonho grande", "400", "R$ 3.200", "R$ 38.400"],
], larguras=[4.0, 3.0, 4.0, 5.0])
caixa(doc, "Como ler esses números",
      "Cem sócios em Beruri é uma meta realista: é menos gente do que a Explosão "
      "costuma reunir num único ensaio aberto. O valor não vem do preço alto, vem da "
      "recorrência — R$ 5 por mês, doze vezes, com cem pessoas, é mais do que a "
      "maioria dos eventos de arrecadação já rendeu à quadrilha.", VERDE)

# ---------------------------------------------------------------- operação ---
doc.add_page_break()
h1(doc, "COMO O PROGRAMA OPERA", 4)
banner(doc, "O CICLO MENSAL",
       "Captar → cobrar com carinho → receber → confirmar com data real → entregar benefício → prestar contas",
       VERMELHO)
tabela(doc, ["Etapa", "O que acontece", "Responsável"], [
    ["1. Captação",
     "Divulgação nas redes, convite pessoal dos brincantes, posto de adesão nos eventos, "
     "indicação de quem já é sócio",
     "Comunicação + brincantes"],
    ["2. Adesão",
     "Escolha do nível, cadastro (nome, contato, nível, forma de pagamento) e entrada no "
     "Close Friends",
     "Secretaria do programa"],
    ["3. Lembrete",
     "Mensagem simpática no início do mês, sem cobrança agressiva. Quem atrasa não é "
     "constrangido",
     "Secretaria do programa"],
    ["4. Pagamento",
     "Pix da quadrilha ou dinheiro entregue a alguém da coordenação",
     "Sócio"],
    ["5. Confirmação",
     "Registro no sistema com a data e a hora reais em que o sócio pagou — separadas da "
     "data em que a coordenação confirmou",
     "Financeiro"],
    ["6. Benefício",
     "Carteirinha, conteúdo exclusivo, sorteio do mês, desconto e brinde conforme o nível",
     "Comunicação"],
    ["7. Prestação de contas",
     "Relatório simples do mês: quanto entrou, quantos sócios, onde foi aplicado",
     "Financeiro"],
], larguras=[3.2, 8.3, 4.5])

caixa(doc, "A regra da data real",
      "Se o sócio pagou no dia 3 e a coordenação só conseguiu confirmar no dia 8, o "
      "registro fica como pago no dia 3. Quem cumpriu o combinado não pode ser "
      "penalizado por atraso da coordenação — e é essa data que vale para os troféus.",
      AMBAR)

h1(doc, "QUEM CUIDA DE QUÊ", 5)
tabela(doc, ["Papel", "Responsabilidade"], [
    ["Diretor Financeiro",
     "Confere pagamentos, mantém o caixa do programa separado, autoriza o uso do dinheiro "
     "e fecha o relatório mensal"],
    ["Diretor Secretário",
     "Mantém a lista oficial de sócios, registra adesões, mudanças de nível e saídas"],
    ["Grupo de Comunicação",
     "Conteúdo do Close Friends, artes, carteirinha digital, destaque no perfil, divulgação "
     "dos sorteios e prestação de contas visual"],
    ["Diretor de Tecnologia",
     "Site do Sócio Torcedor: cadastro, pagamentos, painel do sócio, troféus e "
     "transparência"],
    ["Brincantes (embaixadores)",
     "Captação. Cada brincante convida a própria rede — família, vizinhos, colegas de "
     "trabalho e amigos"],
    ["Presidência",
     "Representa o programa publicamente e assegura que as promessas feitas sejam cumpridas"],
], larguras=[4.5, 11.5])

# ---------------------------------------------------------------- captação ---
h1(doc, "COMO CAPTAR SÓCIOS", 6)
for rot, txt in [
    ("Meta por brincante: ", "cada brincante traz um número combinado de sócios na "
     "temporada. Com cinquenta brincantes trazendo dois cada, a meta de cem é atingida "
     "sem depender de campanha externa."),
    ("Campanha de lançamento: ", "o Arraial de Lançamento é o momento de maior captação "
     "do ano — posto de adesão no evento, com meta do dia e anúncio no palco."),
    ("Indicação: ", "quem indica um novo sócio entra em um sorteio extra ou ganha "
     "reconhecimento público."),
    ("Presença nos eventos: ", "em todo evento da quadrilha há um ponto de adesão, com "
     "QR code e alguém explicando o programa."),
    ("Prova social: ", "publicar a lista de sócios e o que o dinheiro comprou é o melhor "
     "argumento para novos sócios entrarem."),
    ("Comércio local: ", "parceiros divulgam o programa aos clientes; alguns podem "
     "patrocinar cotas de sócio para funcionários ou clientes."),
]:
    bullet(doc, txt, rotulo=rot)

# --------------------------------------------------------------- benefícios --
doc.add_page_break()
h1(doc, "BENEFÍCIOS: COMO ENTREGAR DE VERDADE", 7)
p(doc, "O maior risco do programa é prometer e não entregar. Cada benefício abaixo "
       "tem responsável e momento de entrega definidos.")
tabela(doc, ["Benefício", "Quem entrega", "Quando", "Custo"], [
    ["Carteirinha digital", "Comunicação", "Na adesão", "Zero"],
    ["Carteirinha física", "Comunicação", "Em reunião da torcida", "Baixo (impressão)"],
    ["Close Friends do Instagram", "Comunicação", "Na adesão", "Zero"],
    ["Destaque “Sócios Torcedores” no perfil", "Comunicação", "Permanente", "Zero"],
    ["Sorteios do ano", "Comunicação + Financeiro", "Calendário definido", "Baixo (prêmios de parceiros)"],
    ["Desconto na blusa da temporada", "Financeiro", "No lançamento da camisa", "Margem reduzida"],
    ["Desconto nos eventos", "Financeiro", "Em cada evento", "Margem reduzida"],
    ["Brinde da temporada (Bandeirinha)", "Comunicação", "Uma vez por temporada", "Baixo"],
    ["Blusa “Sócio Torcedor” com nome (Estrela)", "Comunicação", "Uma vez por temporada", "Médio"],
    ["Encontro com a quadrilha (Estrela)", "Presidência", "Uma vez por temporada", "Zero"],
    ["Acesso à prestação de contas", "Financeiro", "Mensal", "Zero"],
], larguras=[5.5, 4.0, 3.5, 3.0], tam=9.5)

h1(doc, "PARCEIROS QUE SUSTENTAM O PROGRAMA", 8)
p(doc, "As parcerias comerciais mudaram de função: em vez de serem apenas cotas de "
       "patrocínio, passam a alimentar o Sócio Torcedor. É uma troca em que os dois "
       "lados ganham — o parceiro recebe divulgação e clientes; o sócio recebe "
       "vantagem real; a quadrilha entrega benefício sem gastar caixa.")
tabela(doc, ["O parceiro oferece", "A quadrilha entrega"], [
    ["Desconto exclusivo para sócios torcedores",
     "Divulgação do parceiro nas redes e na carteirinha do programa"],
    ["Prêmios para os sorteios (kits, vales, produtos)",
     "Menção do parceiro em cada sorteio, com alcance garantido"],
    ["Brindes da temporada",
     "Logo aplicada no brinde e agradecimento público"],
    ["Patrocínio de cotas de sócio (para clientes ou funcionários)",
     "Reconhecimento como apoiador do programa e presença nos eventos"],
    ["Espaço ou estrutura para encontros da torcida",
     "Divulgação do espaço e associação com a quadrilha campeã"],
], larguras=[8.0, 8.0])
p(doc, "Além disso, ficam mantidas as ações para o público geral — promoções, combos "
       "e campanhas abertas a qualquer pessoa, não só a sócios. Detalhes de cotas e "
       "contrapartidas estão no documento “Kit Parceiro”.")

# ------------------------------------------------------------------ troféus --
h1(doc, "TROFÉUS E CONQUISTAS", 9)
p(doc, "Os troféus são o mecanismo que mantém o sócio engajado ao longo do ano. São "
       "gratuitos para a quadrilha e transformam o pagamento em jogo, não em cobrança.")
tabela(doc, ["Conquista", "Como se desbloqueia"], [
    ["Em dia", "Pagar até o dia 5 do mês (usa a data real do pagamento)"],
    ["Sequência", "Meses seguidos pagando em dia — a sequência aparece no painel"],
    ["Temporada completa", "Contribuir em todos os meses da temporada"],
    ["Torcedor de arquibancada", "Presença registrada nos eventos da quadrilha"],
    ["Padrinho", "Indicar novos sócios que efetivamente aderirem"],
    ["Veterano", "Renovar o apoio de uma temporada para outra"],
], larguras=[4.5, 11.5])
for rot, txt in [
    ("Sem punição: ", "quem paga depois do dia 5 não tem juros nem multa. Apenas não "
     "conquista o troféu daquele mês."),
    ("Visível: ", "os troféus aparecem no painel do sócio no site e podem ser destacados "
     "nas redes."),
    ("Reconhecimento físico: ", "a quadrilha pode entregar lembranças a quem acumula "
     "conquistas — decisão interna, sem promessa no material de divulgação."),
]:
    bullet(doc, txt, rotulo=rot)

h1(doc, "SORTEIOS", 10)
for rot, txt in [
    ("Regra central: ", "todos os sócios concorrem com a mesma chance, independentemente "
     "do nível. Todo apoio vale igual na hora do sorteio."),
    ("Frequência: ", "calendário definido no início da temporada, com pelo menos um "
     "sorteio por trimestre e sorteios extras nos eventos-âncora."),
    ("Prêmios: ", "dinheiro, kits de mercado, vales de parceiros, camisa da temporada e "
     "brindes."),
    ("Quem participa: ", "sócios com a contribuição em dia no período do sorteio."),
    ("Transparência do sorteio: ", "lista de participantes publicada antes, sorteio "
     "transmitido ou gravado, resultado divulgado na hora e prêmio entregue com registro."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------ transparência --
doc.add_page_break()
h1(doc, "TRANSPARÊNCIA PARA O SÓCIO", 11)
p(doc, "Transparência é o principal produto do programa. Quem contribui precisa ver "
       "para onde foi o dinheiro — e ver isso sem precisar pedir.")
tabela(doc, ["Entrega", "Conteúdo", "Frequência"], [
    ["Relatório do mês", "Quantos sócios, quanto entrou, onde foi aplicado", "Mensal"],
    ["Painel de finanças", "Receitas e despesas da quadrilha, com destino de cada recurso",
     "Sempre disponível no site"],
    ["Balanço da temporada", "Consolidado do ano, apresentado no Arraial de Lançamento",
     "Anual"],
    ["Registro de sorteios", "Participantes, resultado e entrega dos prêmios", "A cada sorteio"],
], larguras=[4.0, 8.0, 4.0])
p(doc, "O mesmo padrão de dois níveis vale aqui: recurso público tem detalhamento "
       "completo e aberto; arrecadação própria tem total divulgado e detalhe interno. "
       "O sócio tem acesso à planilha de gastos e investimentos do programa.")

# ---------------------------------------------------------------- o sistema --
h1(doc, "O SITE DO SÓCIO TORCEDOR", 12)
p(doc, "O programa tem sistema próprio, separado do Sistema de Avaliação dos "
       "brincantes. Enquanto o site não está completo, a operação roda com Pix, "
       "WhatsApp e o painel da coordenação — que já existe.")
tabela(doc, ["Marco", "O que entrega", "Situação"], [
    ["M1 — Painel da coordenação",
     "Login da coordenação, cadastro de sócios por nível, registro e confirmação de "
     "pagamentos (Pix ou dinheiro) com data e hora reais, cards de arrecadação",
     "Pronto"],
    ["M2 — Painel do sócio",
     "Login do próprio sócio: histórico de contribuições, situação do mês e acesso às "
     "finanças da quadrilha",
     "A fazer"],
    ["M3 — Troféus e conquistas",
     "Regras de conquista, sequência de meses em dia, total contribuído e exibição no "
     "painel",
     "A fazer"],
    ["M4 — Página pública e adesão",
     "Página aberta explicando o programa, adesão online, geração da carteirinha digital "
     "e acabamento visual",
     "A fazer"],
    ["Futuro — Pagamento automático",
     "Cobrança recorrente e confirmação automática do Pix",
     "Ideia"],
], larguras=[4.5, 8.5, 3.0])

h1(doc, "CALENDÁRIO DE IMPLANTAÇÃO", 13)
p(doc, "Previsões, não datas fechadas.")
tabela(doc, ["Período previsto", "O que acontece"], [
    ["Agosto de 2026", "Decisão da Diretoria sobre valores, benefícios e responsáveis; "
     "definição do Pix oficial do programa"],
    ["Setembro de 2026", "Lançamento público do programa; primeira campanha de adesão; "
     "brincantes começam a captar"],
    ["Outubro a dezembro de 2026", "Operação mensal rodando; primeiros sorteios; primeiro "
     "relatório mensal publicado; site avança para o painel do sócio"],
    ["Janeiro e fevereiro de 2027", "Carteirinha e identidade do programa dentro da nova "
     "identidade visual; renovação para a temporada"],
    ["Março de 2027 (previsão)", "Grande campanha de adesão no Arraial de Lançamento, com "
     "prestação de contas do ano anterior"],
    ["Ao longo de 2027", "Sorteios, troféus, relatórios mensais e captação contínua"],
    ["Agosto de 2027 em diante", "Renovação da torcida para a temporada seguinte e "
     "presença no Arraial da Explosão"],
], larguras=[5.0, 11.0])

# ------------------------------------------------------------------ riscos ---
h1(doc, "RISCOS E COMO REDUZIR", 14)
tabela(doc, ["Risco", "Como reduzir"], [
    ["Promessa não cumprida", "Lista de benefícios com responsável e prazo, conferida "
     "mensalmente pela Diretoria"],
    ["Inadimplência", "Lembrete simpático, sem constrangimento; opção de contribuição por "
     "temporada; troféu como incentivo positivo"],
    ["Sobrecarga de quem opera", "Sistema fazendo o controle e responsáveis definidos por "
     "papel, não uma pessoa fazendo tudo"],
    ["Programa esquecido depois do lançamento", "Rotina mínima: um post por semana e um "
     "relatório por mês, no calendário editorial"],
    ["Dinheiro do programa misturado com o resto", "Caixa e registro separados, com "
     "prestação de contas específica"],
    ["Sócio sem sentir diferença", "Conteúdo exclusivo de verdade no Close Friends e "
     "reconhecimento público nominal"],
], larguras=[6.0, 10.0])

h1(doc, "INDICADORES", 15)
tabela(doc, ["Indicador", "Meta de referência"], [
    ["Número de sócios ativos", "100 na temporada 2027"],
    ["Receita recorrente mensal", "R$ 800 na meta da temporada"],
    ["Taxa de pagamento em dia (até o dia 5)", "Acima de 70% dos sócios"],
    ["Renovação de uma temporada para outra", "Acima de 60% dos sócios"],
    ["Sócios captados por brincante", "2 por brincante na temporada"],
    ["Relatórios mensais publicados", "12 por ano, sem falha"],
], larguras=[8.0, 8.0])

citacao(doc, "A Explosão é de Beruri. E Beruri é de quem faz junto.")
p(doc, "Explosão Junina de Beruri · Programa Sócio Torcedor · Temporada 2027",
  centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Programa Socio Torcedor - Plano de Implementacao.docx")
