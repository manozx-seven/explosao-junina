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
    ["Fogueira", "R$ 10", "R$ 100",
     "Carteirinha, Close Friends, sorteios, descontos e acesso à prestação de contas"],
    ["Bandeirinha", "R$ 20", "R$ 200", "Tudo do Fogueira + brinde da temporada"],
    ["Estrela do Arraial", "R$ 30", "R$ 300",
     "Tudo do Bandeirinha + blusa “Sócio Torcedor” com o nome nas costas + bastidores e "
     "encontro com a quadrilha"],
], larguras=[3.5, 2.2, 2.8, 7.5])
for rot, txt in [
    ("Temporada: ", "dez meses de contribuição, de fevereiro a novembro. Dezembro e "
     "janeiro são entressafra: não há cobrança e ninguém acumula atraso — janeiro é a "
     "janela de captação e renovação, dezembro fica livre para as festas de fim de ano."),
    ("Contribuição: ", "mensal ou por temporada, à escolha do torcedor."),
    ("Adesão: ", "Pix + cadastro na lista oficial (e, quando o site estiver no ar, pela "
     "própria plataforma)."),
    ("Mudança de nível: ", "o sócio pode subir ou descer de nível quando quiser."),
    ("Sorteios: ", "abertos a quem está com a contribuição em dia. Entre os elegíveis, "
     "todos concorrem com a mesma chance, independentemente do nível."),
    ("Sem juros e sem multa: ", "quem atrasa não paga nada a mais — apenas não bate a "
     "meta do mês para efeito de troféu e fica fora do sorteio até regularizar."),
    ("O valor é o do nível, e não se digita: ", "quem quer contribuir mais sobe de "
     "nível. Deixar alguém no Fogueira pagando valor de Bandeirinha faria o sistema "
     "cobrar um preço e entregar outro benefício — um número só decide as duas coisas."),
    ("Quem cadastra é a coordenação: ", "o sócio preenche o formulário (WhatsApp ou "
     "presencial) e a coordenação lança no sistema. O site do sócio serve para "
     "entrar e acompanhar. A adesão online entra com a página pública (M4)."),
    ("Como o sócio entra no painel: ", "CPF e data de nascimento. São os dois campos "
     "que a coordenação não pode errar no cadastro, e os dois que o sistema nunca "
     "devolve para tela nenhuma — juntos, são a senha dele."),
    ("Corte do dia 20: ", "quem adere do dia 1 ao 20 contribui já pelo mês corrente; "
     "do dia 21 em diante, a primeira contribuição é do mês seguinte. Evita cobrar "
     "duas vezes em poucos dias."),
    ("Vencimento: ", "dia 5 de cada mês. A chave Pix oficial fica no painel do sócio, "
     "com o nome do titular ao lado — é a única conferência que ele consegue fazer "
     "sozinho no aplicativo do banco antes de mandar o dinheiro."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------------ metas ---
h1(doc, "METAS E CENÁRIOS", 3)
p(doc, "Os números abaixo são cenários para dimensionar o programa, não promessas. "
       "A distribuição usada é a mesma proporção em todos os cenários (60% Fogueira, "
       "30% Bandeirinha, 10% Estrela).")
tabela(doc, ["Cenário", "Sócios", "Receita mensal", "Receita da temporada (10 meses)"], [
    ["Início", "50", "R$ 750", "R$ 7.500"],
    ["Meta da temporada", "100", "R$ 1.500", "R$ 15.000"],
    ["Consolidado", "200", "R$ 3.000", "R$ 30.000"],
    ["Sonho grande", "400", "R$ 6.000", "R$ 60.000"],
], larguras=[4.0, 3.0, 4.0, 5.0])
caixa(doc, "Como ler esses números",
      "A temporada tem dez meses de contribuição, de fevereiro a novembro — dezembro "
      "e janeiro são entressafra, sem cobrança. Cem sócios em Beruri é uma meta "
      "realista: é menos gente do que a Explosão costuma reunir num único ensaio "
      "aberto. O valor não vem do preço alto, vem da recorrência — R$ 10 por mês, dez "
      "vezes, com cem pessoas, é mais do que a maioria dos eventos de arrecadação já "
      "rendeu à quadrilha.", VERDE)

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

h2(doc, "4.1 A régua do atraso")
p(doc, "Nunca há multa, juros ou cobrança retroativa. O que muda é o que o sócio "
       "deixa de acessar enquanto estiver devendo — e é sempre reversível.")
tabela(doc, ["Situação", "Quando acontece", "O que muda para o sócio"], [
    ["Em dia", "Pagou até o dia 5", "Ganha o troféu do mês e concorre aos sorteios"],
    ["Pago com atraso", "Pagou depois do dia 5",
     "Vale como pago. Perde o troféu daquele mês e a sequência recomeça"],
    ["Atrasado", "Passou do dia 5 com o mês em aberto",
     "Fica fora dos sorteios e recebe um lembrete amigável. Painel, mural, missões e "
     "finanças continuam. Pontos de missão ficam retidos até pagar"],
    ["Suspenso", "Um mês fechado sem pagar", "Sai dos sorteios e do mural; o painel "
     "segue acessível"],
    ["Inativo", "Dois meses seguidos sem pagar",
     "Sai do quadro ativo e o progresso da temporada zera"],
], larguras=[3.0, 5.0, 8.0])
p(doc, "A situação é calculada a partir dos pagamentos confirmados — nunca digitada "
       "por alguém. Isso evita o caso clássico do sócio que pagou e continua marcado "
       "como devedor porque ninguém lembrou de mudar o status.")

h2(doc, "4.2 Entressafra e volta do inativo")
for rot, txt in [
    ("Na entressafra o relógio congela: ", "dezembro e janeiro não acumulam mês novo "
     "em aberto. Mas não perdoa: quem já estava suspenso ou inativo continua assim "
     "até regularizar."),
    ("Quem volta não recomeça do zero: ", "o sócio inativo que retorna mantém para "
     "sempre o número da carteirinha, a antiguidade e todo o histórico de "
     "pagamentos. O que zera é o progresso e os troféus da temporada."),
    ("Volta pagando só o mês corrente: ", "sem cobrança retroativa dos meses em que "
     "esteve fora, e podendo trocar de nível na volta."),
    ("Ele continua entrando no painel: ", "em versão reduzida. É a tela de quem a "
     "quadrilha mais quer de volta — fechá-la seria fechar a porta."),
]:
    bullet(doc, txt, rotulo=rot)

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
    ("Indicação: ", "quem indica um novo sócio ganha reconhecimento público e o troféu "
     "“Chamador de Gente” no painel — não um sorteio à parte. A urna é única: todo apoio "
     "vale igual na hora do sorteio, e criar uma segunda urna contradiria a promessa "
     "feita ao sócio. A indicação é registrada no sistema com o nome e o "
     "telefone de quem foi trazido — nunca CPF ou data de nascimento, que juntos são "
     "a senha de acesso do sócio ao painel."),
    ("Captação pelo brincante: ", "para o brincante, trazer sócios é uma missão no "
     "Sistema de Avaliação e conta como desempenho e troféu — reconhecimento, não "
     "dinheiro. Ele declara quem trouxe e a coordenação confirma."),
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
    ["Carteirinha digital", "Comunicação", "Na adesão, no painel do sócio", "Zero"],
    ["Carteirinha física exclusiva", "Comunicação",
     "Reunião da torcida, fevereiro de 2027", "Baixo (impressão)"],
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
caixa(doc, "A carteirinha da primeira torcida",
      "Todo sócio tem a carteirinha digital no painel do site, e o sistema gera o modelo "
      "genérico para impressão a qualquer momento. Além disso, quem aderir até fevereiro "
      "de 2027 recebe uma carteirinha física exclusiva, de design próprio, entregue "
      "pessoalmente na reunião da torcida — é a carteirinha da primeira temporada, item "
      "de colecionador que só esse grupo terá. Quem entrar depois recebe a carteirinha "
      "comum. É um motivo concreto para aderir cedo, e custa à quadrilha apenas a "
      "impressão.", AMBAR)

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
tabela(doc, ["Conquista", "Como se desbloqueia", "Situação"], [
    ["Primeira Fagulha", "A primeira contribuição confirmada. Começou", "No ar"],
    ["Pontual", "Pagar dentro do prazo — até o dia 5, pela data real do pagamento", "No ar"],
    ["Trio de Fogo", "Três meses seguidos pagando dentro do prazo", "No ar"],
    ["Temporada Completa", "Contribuir em todos os meses da própria temporada", "No ar"],
    ["Chamador de Gente", "Indicar alguém que virou sócio de verdade", "No ar"],
    ["Veterano", "Apoiar a quadrilha em mais de uma temporada", "No ar"],
    ["Sócio Fiel (físico)", "Três meses seguidos no prazo — troféu entregue na mão pela "
     "coordenação", "No ar"],
    ["Torcedor de Arquibancada", "Presença registrada nos eventos da quadrilha", "No ar"],
    ["Missão Cumprida", "A primeira missão aprovada pela coordenação", "No ar"],
    ["Puxador de Fila", "Cinco missões aprovadas na temporada", "No ar"],
], larguras=[4.5, 8.5, 3.0], tam=9.5)
for rot, txt in [
    ("Sem punição: ", "quem paga depois do dia 5 não tem juros nem multa. Apenas não "
     "conquista o troféu daquele mês — e a sequência recomeça."),
    ("Visível: ", "os troféus aparecem no painel do sócio no site, com barra de progresso "
     "para os que ainda faltam, e podem ser destacados nas redes."),
    ("Reconhecimento físico: ", "o Sócio Fiel é entregue pessoalmente, a cada dois ou três "
     "meses — nunca todo mês. A quadrilha pode criar outras lembranças para quem acumula "
     "conquistas: decisão interna, sem promessa no material de divulgação."),
    ("Todas no ar: ", "as dez conquistas já são calculadas pelo site, inclusive as "
     "três que dependiam do módulo de missões (Torcedor de Arquibancada, Missão "
     "Cumprida e Puxador de Fila), concluído em julho de 2026."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------------ missões --
h1(doc, "MISSÕES: O QUE FAZER ENTRE UM DIA 5 E O OUTRO", 10)
p(doc, "O troféu premia quem paga. A missão dá o que fazer no resto do mês. Sem "
       "isso, o programa só dá sinal de vida no vencimento — e apoio que só aparece "
       "na hora de cobrar não cria torcida.")
p(doc, "A coordenação publica cerca de uma missão por semana, mais relâmpagos "
       "ocasionais. Cada missão vale pontos, e os pontos alimentam o ranking da "
       "temporada e as conquistas.")
tabela(doc, ["Tipo", "O que é", "Como valida", "Custo para a coordenação"], [
    ["Missão rápida", "Enquete, quiz sobre a quadrilha, pergunta do dia — respondida "
     "no próprio site", "Sozinha", "Zero — é o que permite cadência sem gerar fila"],
    ["Rede social", "Curtir, comentar, compartilhar ou postar story marcando a "
     "Explosão", "Link da publicação, conferido por uma pessoa",
     "Alto — use cadência semanal; diária, com cem sócios, dá cem validações por dia"],
    ["Presença", "Ensaio, apresentação ou reunião", "A coordenação marca quem veio, "
     "de uma vez", "Baixo — não gera fila"],
    ["Indicação", "Trazer um sócio novo", "Sozinha, conferindo o cadastro de quem foi "
     "indicado", "Zero — só conta quando o indicado tem contribuição confirmada"],
], larguras=[2.8, 5.2, 4.0, 4.0], tam=9.5)
for rot, txt in [
    ("Prova por link ou por escrito, não por print: ", "a coordenação abre a "
     "publicação e vê o estado real dela, e link não se edita no editor de fotos. "
     "Para o que some em 24 horas, como story, vale a descrição por escrito com "
     "conferência por amostragem."),
    ("Missão nasce como rascunho: ", "publicar é um segundo clique. E não se encerra "
     "missão com entrega pendente na fila — o sócio enviou, alguém precisa "
     "responder."),
    ("Pontos congelam na aprovação: ", "mudar depois o valor de uma missão já "
     "aprovada é recusado pelo sistema. O que foi ganho, foi ganho."),
    ("Quem está devendo joga, mas os pontos ficam retidos: ", "libera quando o mês "
     "for pago. É o desenho que dá algo concreto a perder sem expulsar ninguém da "
     "brincadeira. Quem deixa o mês fechar (suspenso) sai das missões."),
    ("Validação em lote: ", "a coordenação valida agrupando por missão, não uma a "
     "uma. É o que torna o módulo sustentável numa base de cem sócios."),
]:
    bullet(doc, txt, rotulo=rot)

h1(doc, "SORTEIOS", 11)
for rot, txt in [
    ("Regra central: ", "o sorteio é aberto a quem está com a contribuição em dia. Entre "
     "os elegíveis, todos concorrem com a mesma chance, independentemente do nível — todo "
     "apoio vale igual na hora do sorteio."),
    ("Quem pagou atrasado concorre: ", "a limitação é sobre estar devendo, não sobre ter "
     "atrasado. Quem regulariza volta a concorrer no sorteio seguinte, porque a "
     "elegibilidade é apurada na data do sorteio."),
    ("É a única perda de quem está atrasado: ", "mural, missões, troféus, painel e "
     "finanças continuam abertos. O sorteio é o que fica de fora."),
    ("Frequência: ", "calendário definido no início da temporada, com pelo menos um "
     "sorteio por trimestre e sorteios extras nos eventos-âncora."),
    ("Prêmios: ", "dinheiro, kits de mercado, vales de parceiros, camisa da temporada e "
     "brindes."),
    ("Transparência do sorteio: ", "lista de participantes publicada antes, sorteio "
     "transmitido ou gravado, resultado divulgado na hora e prêmio entregue com registro."),
]:
    bullet(doc, txt, rotulo=rot)
caixa(doc, "O sorteio precisa se defender sozinho",
      "Sorteio de dinheiro entre vizinhos gera desconfiança mais cedo ou mais tarde. "
      "Por isso o sistema congela a lista de participantes no momento do sorteio "
      "(com os nomes, para a prova não depender do cadastro de depois), recusa "
      "sortear duas vezes o mesmo sorteio, recusa sortear antes da data anunciada e "
      "escolhe o vencedor por sorteio criptográfico, sem viés. A entrega do prêmio "
      "fica registrada com data e com quem entregou.", AZUL)

# ------------------------------------------------------------ transparência --
doc.add_page_break()
h1(doc, "TRANSPARÊNCIA PARA O SÓCIO", 12)
p(doc, "Transparência é o principal produto do programa. Quem contribui precisa ver "
       "para onde foi o dinheiro — e ver isso sem precisar pedir.")
tabela(doc, ["Entrega", "Conteúdo", "Frequência"], [
    ["Relatório do mês", "Quantos sócios, quanto entrou, onde foi aplicado", "Mensal"],
    ["Painel de finanças", "Receitas e despesas da quadrilha, com destino de cada recurso",
     "Por temporada, liberada pela coordenação"],
    ["Balanço da temporada", "Consolidado do ano, apresentado no Arraial de Lançamento",
     "Anual"],
    ["Registro de sorteios", "Participantes, resultado e entrega dos prêmios", "A cada sorteio"],
], larguras=[4.0, 8.0, 4.0])
p(doc, "O mesmo padrão de dois níveis vale aqui: recurso público tem detalhamento "
       "completo e aberto; arrecadação própria tem total divulgado e detalhe interno.")
caixa(doc, "Como a liberação funciona",
      "O painel de finanças é liberado por temporada, uma de cada vez, pela coordenação. "
      "A temporada em andamento só é aberta ao sócio depois que a categorização de "
      "gastos e investimentos estiver definida e o lançamento estiver em dia — abrir "
      "antes disso significa mostrar número errado a quem confiou na quadrilha. As "
      "temporadas passadas entram pela importação de uma planilha, e ficam disponíveis "
      "assim que a coordenação marca a temporada como visível.", AZUL)

# ---------------------------------------------------------------- o sistema --
h1(doc, "O SITE DO SÓCIO TORCEDOR", 13)
p(doc, "O programa tem sistema próprio, separado do Sistema de Avaliação dos "
       "brincantes. Desde julho de 2026 ele está no ar, ligado ao banco de dados de "
       "verdade: o painel da coordenação e o painel do sócio funcionam, e a operação "
       "roda com Pix e WhatsApp ao lado deles.")

h2(doc, "13.1 O que o sócio faz no painel dele")
tabela(doc, ["Recurso", "O que ele consegue"], [
    ["Entrar", "Com CPF e data de nascimento, na página inicial do site"],
    ["Carteirinha digital", "Sempre à mão, com o número e o nível; há também um "
     "modelo genérico para imprimir"],
    ["Situação do mês", "Se está em dia, o que falta pagar e até quando"],
    ["Avisar o pagamento", "Informa que pagou, com data e hora reais; a coordenação "
     "confirma depois. Enquanto não confirma, não entra no caixa"],
    ["Chave Pix", "Com o nome do titular e botão de copiar, no topo do aviso de "
     "pagamento"],
    ["Progresso da temporada", "Quanto já contribuiu no ano e quanto falta"],
    ["Histórico", "Todas as contribuições, com data real e forma de pagamento"],
    ["Troféus", "Vitrine das conquistas, com barra de progresso das que faltam"],
    ["Missões", "Missões abertas, envio da prova e os pontos — inclusive os retidos"],
    ["Trocar de nível", "Sobe ou desce na hora, valendo do primeiro mês ainda não "
     "pago; mês já pago não muda de valor"],
    ["Mural", "Recados e novidades da quadrilha para a torcida"],
    ["Finanças", "Prestação de contas das temporadas liberadas pela coordenação"],
    ["Meus dados", "Corrige nome, apelido, contato e e-mail. CPF e nascimento ficam "
     "travados — são a senha dele; para mudar, fala com a coordenação"],
], larguras=[4.0, 12.0], tam=9.5)

h2(doc, "13.2 O que a coordenação faz no painel dela")
tabela(doc, ["Recurso", "Para que serve"], [
    ["Cadastro de sócios", "Nome completo, CPF, nascimento, contato e nível. O valor "
     "vem do nível, não se digita"],
    ["Registro de pagamento", "Pix ou dinheiro, com data e hora reais e quem recebeu"],
    ["Fila de confirmação", "Avisos de pagamento dos sócios esperando conferência"],
    ["Lista de lembretes", "Quem está para vencer e quem está devendo, com o contato "
     "à mão"],
    ["Configuração das regras", "Temporada, vencimento, corte de adesão, régua de "
     "suspensão, chave Pix e o que fica visível ao sócio"],
    ["Missões", "Criação, publicação e validação em lote das entregas"],
    ["Sorteios", "Abertura, sorteio e registro da entrega do prêmio"],
    ["Troféus", "Acompanhamento de quem conquistou o quê, para a entrega dos físicos"],
    ["Finanças", "Lançamentos da quadrilha e importação das temporadas passadas por "
     "planilha, com prévia e detecção de linha repetida"],
    ["Importação de sócios", "Entrada em lote por planilha, para a virada da "
     "temporada"],
    ["Administradores", "Quem da coordenação tem acesso, com troca de senha "
     "obrigatória no primeiro login"],
], larguras=[4.0, 12.0], tam=9.5)

h2(doc, "13.3 Marcos")
tabela(doc, ["Marco", "O que entrega", "Situação"], [
    ["M1 — Painel da coordenação",
     "Login da coordenação, cadastro de sócios por nível, registro e confirmação de "
     "pagamentos (Pix ou dinheiro) com data e hora reais, cards de arrecadação",
     "Pronto"],
    ["M2 — Painel do sócio",
     "Login do próprio sócio com CPF e data de nascimento: carteirinha digital, situação "
     "do mês, progresso da temporada, histórico de contribuições, troca de nível, aviso "
     "de pagamento, mural e acesso às finanças da quadrilha. Do lado da coordenação: "
     "configuração das regras, fila de confirmação, lista de lembretes e importação de "
     "sócios e de finanças por planilha",
     "Pronto"],
    ["M3 — Troféus, sorteios e missões",
     "Troféus calculados com vitrine e progresso, sorteios com lista congelada e "
     "registro de entrega, e o módulo de missões com pontos retidos e validação em "
     "lote. Falta o ranking da temporada no mural e as notificações",
     "Em andamento"],
    ["M4 — Página pública e adesão",
     "Página aberta explicando o programa, adesão online, geração da carteirinha digital "
     "e acabamento visual",
     "A fazer"],
    ["Futuro — Pagamento automático",
     "Cobrança recorrente e confirmação automática do Pix",
     "Ideia"],
], larguras=[4.5, 8.5, 3.0])
p(doc, "Do M2 falta apenas o envio do comprovante por imagem, que depende de conta e "
       "credenciais externas ainda não provisionadas — hoje o sócio descreve o pagamento "
       "por texto e a coordenação confirma. Do M3 faltam o ranking da temporada e as "
       "notificações; a mensagem pronta para WhatsApp é a de melhor retorno e custo zero.")

h2(doc, "13.4 Segurança: o que o site protege")
for rot, txt in [
    ("CPF e nascimento nunca saem: ", "juntos, são a senha do sócio. O painel mostra "
     "o CPF mascarado, e nenhuma tela devolve os dois."),
    ("Quem o usuário é vem do servidor: ", "não do navegador. Não há como pedir os "
     "dados de outro sócio trocando um parâmetro na tela."),
    ("Trava de força bruta nos dois logins: ", "cinco erros em quinze minutos "
     "bloqueiam por meia hora. Numa cidade pequena, o CPF de alguém não é segredo."),
    ("O caixa só soma o que foi confirmado: ", "aviso de pagamento do sócio não entra "
     "na arrecadação nem quita mês nenhum até a coordenação conferir."),
    ("A chave Pix é validada por tipo: ", "é o único campo do sistema em que um erro "
     "de digitação manda dinheiro para um desconhecido."),
    ("A coordenação entra por e-mail e senha: ", "com troca obrigatória no primeiro "
     "acesso e recuperação por e-mail. Cada administrador tem o próprio acesso."),
]:
    bullet(doc, txt, rotulo=rot)

h1(doc, "CALENDÁRIO DE IMPLANTAÇÃO", 14)
p(doc, "Previsões, não datas fechadas.")
tabela(doc, ["Período previsto", "O que acontece"], [
    ["Agosto de 2026", "Reunião da Diretoria — o próximo passo do programa não é "
     "código, é decisão: valores e benefícios dos níveis, chave Pix oficial, "
     "categorização de gastos para liberar as finanças da temporada vigente, e a "
     "data da reunião de entrega da carteirinha física"],
    ["Setembro a dezembro de 2026", "Campanha de divulgação: apresentar o programa à "
     "cidade e formar a lista de interessados. Ainda sem cobrança. O site fecha o M3 "
     "(ranking e notificações) e avança para a página pública"],
    ["Janeiro de 2027", "Captação: adesões efetivadas e cadastro no sistema. Carteirinha "
     "e identidade do programa dentro da nova identidade visual"],
    ["Fevereiro de 2027", "Início da temporada e da primeira cobrança. Reunião da torcida "
     "com a entrega da carteirinha física exclusiva a quem aderiu até fevereiro"],
    ["Março de 2027 (previsão)", "Grande campanha de adesão no Arraial de Lançamento, com "
     "prestação de contas do ano anterior"],
    ["Fevereiro a novembro de 2027", "Temporada rodando: sorteios, troféus, relatórios "
     "mensais e captação contínua"],
    ["Dezembro de 2027 e janeiro de 2028", "Entressafra: sem cobrança. Balanço da "
     "temporada e renovação da torcida para o ciclo seguinte"],
], larguras=[5.0, 11.0])

# ------------------------------------------------------------------ riscos ---
h1(doc, "RISCOS E COMO REDUZIR", 15)
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
    ["Fila de validação de missões estourar", "Missão de rede social só em cadência "
     "semanal, validação em lote e preferência pelos tipos que se aprovam sozinhos"],
    ["Chave Pix errada no painel", "Validada por tipo na gravação e conferida com o "
     "nome do titular ao lado; alteração só pela coordenação"],
    ["O programa começar sem benefício pronto", "A primeira cobrança é fevereiro de "
     "2027: até lá, carteirinha, Close Friends e calendário de sorteios precisam "
     "existir de fato"],
], larguras=[6.0, 10.0])

h1(doc, "INDICADORES", 16)
tabela(doc, ["Indicador", "Meta de referência"], [
    ["Número de sócios ativos", "100 na temporada 2027"],
    ["Receita recorrente mensal", "R$ 1.500 na meta da temporada"],
    ["Receita da temporada", "R$ 15.000 (dez meses)"],
    ["Taxa de pagamento em dia (até o dia 5)", "Acima de 70% dos sócios"],
    ["Renovação de uma temporada para outra", "Acima de 60% dos sócios"],
    ["Sócios captados por brincante", "2 por brincante na temporada"],
    ["Relatórios mensais publicados", "10 por temporada, sem falha"],
], larguras=[8.0, 8.0])

citacao(doc, "A Explosão é de Beruri. E Beruri é de quem faz junto.")
p(doc, "Explosão Junina de Beruri · Programa Sócio Torcedor · Temporada 2027",
  centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Programa Socio Torcedor - Plano de Implementacao.docx")
