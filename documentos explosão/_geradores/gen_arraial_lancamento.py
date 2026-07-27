# -*- coding: utf-8 -*-
"""Gera 'Arraial de Lancamento - Plano do Evento.docx'."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["ARRAIAL", "DE LANÇAMENTO"],
    "Plano do evento · Temporada 2027",
    "A abertura oficial da temporada: tema, itens, camisa e prestação de contas.",
    nota="Previsão: começo da temporada — pode ser em março. Sem data fechada.",
    rodape="Beruri – Amazonas",
    cor=VERMELHO,
)

# ---------------------------------------------------------------- o que é ---
h1(doc, "O QUE É E POR QUE EXISTE", 1)
p(doc, "O Arraial de Lançamento é o evento que abre oficialmente a temporada da "
       "Explosão Junina. É nele que a quadrilha revela o tema do ano, apresenta os "
       "itens, lança a camisa da temporada e presta contas do que arrecadou e gastou "
       "no ano anterior.")
p(doc, "Ele resolve um problema concreto identificado no diagnóstico da "
       "reestruturação: até aqui, tema, camisa e itens apareciam aos poucos, sem "
       "evento próprio e sem impacto — enquanto a concorrência lançava tudo junto, de "
       "forma coordenada e com identidade visual profissional. Lançamento espalhado "
       "não gera expectativa; lançamento concentrado, sim.")
caixa(doc, "A regra do evento",
      "Tema, itens e camisa são revelados no mesmo dia, no mesmo lugar, com a "
      "identidade visual pronta. Nada é divulgado antes. O que sai antes é teaser — "
      "nunca a revelação.", VERMELHO)

h2(doc, "1.1 Objetivos")
for rot, txt in [
    ("Abrir a temporada: ", "marcar o início oficial do ano de trabalho da quadrilha."),
    ("Revelar o tema: ", "apresentar a história que será contada na arena, com a "
     "identidade visual completa."),
    ("Apresentar os itens: ", "marcador, casal de noivos e casal real da temporada."),
    ("Lançar e vender a camisa: ", "início imediato das vendas, com promoções e "
     "desconto para sócios."),
    ("Prestar contas: ", "mostrar publicamente o que entrou e o que saiu no ano anterior."),
    ("Captar sócios torcedores: ", "é o maior momento de adesão do ano."),
    ("Arrecadar: ", "venda de camisa, comidas, bebidas e ações no próprio evento."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "1.2 Quando acontece")
p(doc, "Sempre no começo da temporada, com previsão de março. O evento deve acontecer "
       "depois de os contratos assinados e os ensaios iniciados (previstos para "
       "fevereiro), para que o público veja um grupo já em atividade — e antes que a "
       "temporada avance demais, para que o tema tenha tempo de ser trabalhado nas "
       "redes até o Festival.")

# ------------------------------------------------------------- programação --
doc.add_page_break()
h1(doc, "PROGRAMAÇÃO", 2)
tabela(doc, ["Momento", "Descrição"], [
    ["Abertura",
     "Boas-vindas da Presidência, breve histórico da quadrilha e agradecimento a "
     "parceiros, sócios e apoiadores"],
    ["Prestação de contas",
     "Apresentação do balanço do ano anterior: recursos públicos recebidos e aplicados, "
     "total da arrecadação própria e patrimônio da quadrilha"],
    ["Apresentação da estrutura",
     "Quem é quem na temporada: diretoria, comissões e grupos de produção. Mostra que a "
     "quadrilha tem organização, não só vontade"],
    ["Lançamento do tema",
     "Revelação do tema com arte oficial, sinopse contada ao público e primeira exibição "
     "da identidade visual da temporada"],
    ["Apresentação dos itens",
     "Revelação do marcador, do casal de noivos e do casal real, caracterizados"],
    ["Lançamento da camisa",
     "Apresentação da camisa oficial e início imediato das vendas, com promoções"],
    ["Sorteios",
     "Sorteios para o público presente e sorteio exclusivo dos sócios torcedores"],
    ["Prévia da Explosão",
     "Trecho de coreografia ou apresentação dos itens dançando — o primeiro gosto da "
     "temporada"],
    ["Convite ao Sócio Torcedor",
     "Explicação do programa no palco, com posto de adesão funcionando durante todo o "
     "evento"],
    ["Encerramento",
     "Próximos passos da temporada, calendário de ensaios e convite para acompanhar a "
     "quadrilha"],
], larguras=[4.5, 11.5])

# ------------------------------------------------------- prestação de contas
h1(doc, "PRESTAÇÃO DE CONTAS", 3)
p(doc, "A prestação de contas é o que diferencia o Arraial de Lançamento de qualquer "
       "outro evento de quadrilha na região. Ela acontece todo ano, sempre no "
       "lançamento, cobrindo a temporada anterior.")
tabela(doc, ["Nível", "O que é apresentado"], [
    ["I — Recursos públicos\n(detalhamento completo)",
     "Verbas recebidas (Lei Paulo Gustavo, editais e fomentos municipais, estaduais e "
     "federais), com valor, aplicação detalhada, entregas realizadas e comprovação. É "
     "obrigação legal e será apresentado com clareza"],
    ["II — Arrecadação própria\n(apenas o total)",
     "Valor total arrecadado com recursos próprios: parcerias, camisas, eventos, "
     "doações e Sócio Torcedor. O detalhamento por fonte e por parceiro fica registrado "
     "internamente, disponível em reunião interna — é informação estratégica"],
    ["III — Patrimônio\n(opcional, recomendado)",
     "O que a quadrilha possui hoje: figurinos, equipamento de som, materiais, alegorias "
     "e estoque de camisas. Mostra o que foi construído com o dinheiro"],
], larguras=[4.5, 11.5])
for rot, txt in [
    ("Formato: ", "apresentação visual simples — slides projetados ou painel impresso — "
     "com linguagem acessível, sem juridiquês. Qualquer pessoa de Beruri tem que "
     "entender."),
    ("Quem apresenta: ", "Diretor Financeiro, com apoio da Presidência."),
    ("Publicação: ", "o mesmo material é publicado nas redes logo depois do evento, para "
     "quem não pôde ir."),
    ("Tempo: ", "objetiva. Prestação de contas longa esvazia o evento — o detalhe fica no "
     "material publicado."),
]:
    bullet(doc, txt, rotulo=rot)

# ----------------------------------------------------------------- revelação
doc.add_page_break()
h1(doc, "REVELAÇÃO DO TEMA E DOS ITENS", 4)
p(doc, "A revelação é o momento mais esperado da noite e precisa ser tratada como "
       "produção, não como aviso. A Comissão de Artes define, com antecedência, o que "
       "é revelado no evento e o que continua em segredo até o Festival.")
tabela(doc, ["Etapa", "Como fazer"], [
    ["Aquecimento",
     "Semanas antes: teasers nas redes, contagem regressiva e pistas do tema, sem entregar "
     "o nome"],
    ["Revelação do nome",
     "Anúncio no palco com arte oficial projetada e trilha preparada. É o clímax do evento"],
    ["A história",
     "Alguém da Comissão de Artes conta a sinopse: o que o espetáculo vai contar e por que "
     "esse tema"],
    ["Os itens",
     "Marcador, casal de noivos e casal real entram caracterizados, um a um, com "
     "apresentação individual"],
    ["A camisa",
     "Apresentada logo em seguida, já com a identidade do tema aplicada, e posta à venda "
     "na hora"],
    ["O que fica em segredo",
     "Alegorias, efeitos, coreografia completa e surpresas de cena. Definido em ata pela "
     "Comissão de Artes"],
], larguras=[4.0, 12.0])

h1(doc, "CAMISA DA TEMPORADA", 5)
for rot, txt in [
    ("Estoque inicial: ", "produzir lote suficiente para venda imediata no evento — "
     "público empolgado compra na hora; se não tiver camisa, a venda esfria."),
    ("Pré-venda: ", "abrir encomenda antecipada com pagamento por Pix, para dimensionar "
     "o lote e reduzir o risco de encalhe."),
    ("Desconto para sócios: ", "sócio torcedor tem desconto em todos os níveis — é um dos "
     "benefícios do programa e argumento de adesão no próprio evento."),
    ("Tabela de preços: ", "definida antes do evento pelo Diretor Financeiro, com margem "
     "calculada e promoções previstas (combos, segunda peça, famílias)."),
    ("Controle: ", "registro de cada venda, forma de pagamento e tamanho, para controle "
     "de estoque e balanço."),
]:
    bullet(doc, txt, rotulo=rot)

h1(doc, "SORTEIOS E PROMOÇÕES", 6)
tabela(doc, ["Ação", "Público", "Como funciona"], [
    ["Sorteio do público", "Qualquer pessoa presente",
     "Cupom entregue na entrada ou na compra da camisa; sorteio durante o evento"],
    ["Sorteio dos sócios", "Somente sócios torcedores em dia",
     "Sorteio exclusivo, anunciado no palco — mostra na prática a vantagem de ser sócio"],
    ["Promoção da camisa", "Público geral",
     "Combos e descontos por tempo limitado durante o evento"],
    ["Prêmios de parceiros", "Público e sócios",
     "Kits, vales e produtos doados pelos parceiros do Kit Parceiro, com menção no palco"],
    ["Adesão premiada", "Novos sócios",
     "Quem aderir ao programa durante o evento concorre a um prêmio extra"],
], larguras=[4.0, 4.5, 7.5])

h1(doc, "O SÓCIO TORCEDOR NO EVENTO", 7)
p(doc, "O Arraial de Lançamento é a maior oportunidade de captação do ano para o "
       "Programa Sócio Torcedor: público reunido, clima de festa e prestação de contas "
       "recém-apresentada — ou seja, confiança em alta.")
for rot, txt in [
    ("Posto de adesão: ", "espaço fixo e sinalizado, com QR code, formulário e alguém "
     "explicando o programa o tempo todo."),
    ("Anúncio no palco: ", "explicação curta do programa logo depois da prestação de "
     "contas, quando o público acabou de ver para onde vai o dinheiro."),
    ("Meta do dia: ", "número de novas adesões definido antes do evento e acompanhado "
     "durante a noite."),
    ("Carteirinha na hora: ", "quem aderir sai do evento com a carteirinha digital e "
     "entra no Close Friends."),
    ("Vantagem visível: ", "desconto na camisa e sorteio exclusivo aplicados no próprio "
     "evento — o benefício precisa ser sentido no mesmo dia."),
]:
    bullet(doc, txt, rotulo=rot)

# -------------------------------------------------------- receitas/estrutura
doc.add_page_break()
h1(doc, "RECEITAS E DESPESAS", 8)
tabela(doc, ["Receitas previstas", "Despesas previstas"], [
    ["Venda da camisa oficial", "Produção do lote de camisas"],
    ["Venda de comidas e bebidas", "Estrutura: som, iluminação, palco e projeção"],
    ["Rifa ou bingo no evento (opcional)", "Material gráfico e artes de divulgação"],
    ["Cotas de patrocínio do evento", "Prêmios não doados por parceiros"],
    ["Novas adesões ao Sócio Torcedor", "Ingredientes e insumos da banca"],
    ["Produtos oficiais (leque, chapéu, brindes)", "Decoração junina e cenografia do evento"],
], larguras=[8.0, 8.0])

h1(doc, "ESTRUTURA E EQUIPES", 9)
tabela(doc, ["Item / equipe", "Detalhe"], [
    ["Espaço", "Praça, quadra ou salão com capacidade para o público esperado"],
    ["Som e microfone", "Essencial: o evento é falado. Testar antes"],
    ["Projeção", "Projetor ou telão para a prestação de contas e a revelação do tema"],
    ["Iluminação e decoração", "Clima junino e cenografia com a identidade do tema"],
    ["Equipe de palco", "Locução, ordem dos momentos e condução do tempo"],
    ["Equipe de vendas", "Camisas, comidas e bebidas, com controle de caixa"],
    ["Equipe do Sócio Torcedor", "Posto de adesão e atendimento"],
    ["Equipe de comunicação", "Fotos, vídeos, transmissão e stories ao vivo"],
    ["Recepção", "Recebe autoridades, parceiros, imprensa e grupos convidados"],
], larguras=[4.5, 11.5])

h1(doc, "CRONOGRAMA DE PRODUÇÃO", 10)
tabela(doc, ["Prazo", "O que fazer"], [
    ["D-60", "Definir data e local; confirmar que tema, itens e camisa estarão prontos"],
    ["D-45", "Fechar a arte do tema e da camisa; iniciar a produção do lote de camisas"],
    ["D-30", "Captar patrocínio do evento; definir programação; começar os teasers nas "
     "redes"],
    ["D-20", "Fechar o balanço do ano anterior e preparar o material de prestação de contas"],
    ["D-15", "Divulgação pesada; convidar autoridades, parceiros, imprensa e danças "
     "convidadas"],
    ["D-7", "Reunião final da equipe e escala por função; conferir estoque de camisas e "
     "prêmios"],
    ["D-2", "Montagem, decoração e teste de som e projeção"],
    ["D-1", "Ensaio da ordem do evento: revelação, entrada dos itens e prévia da coreografia"],
    ["Dia", "Realizar o evento e registrar tudo"],
    ["D+2", "Publicar a prestação de contas, as artes do tema e o registro do evento"],
    ["D+7", "Mini-balanço financeiro e reunião de aprendizados"],
], larguras=[2.5, 13.5])

h1(doc, "O QUE O SISTEMA FAZ", 11)
tabela(doc, ["Recurso", "Como ajuda no evento"], [
    ["Adesão ao Sócio Torcedor", "Cadastro na hora pelo site, com carteirinha digital "
     "gerada na sequência"],
    ["Registro de vendas da camisa", "Controle de pedidos, tamanhos, pagamento e estoque"],
    ["Painel de prestação de contas", "Balanço alimentado pelos registros financeiros, "
     "pronto para projetar e publicar"],
    ["Sorteio digital", "Sorteio entre os presentes e entre os sócios em dia, com registro "
     "do resultado"],
    ["Agenda da temporada", "Calendário de ensaios divulgado no evento e disponível no "
     "sistema para os brincantes"],
], larguras=[4.5, 11.5])

# ---------------------------------------------------------------- checklist --
doc.add_page_break()
checklist(doc, [
    "Definir data e local do Arraial de Lançamento",
    "Confirmar tema, itens e camisa prontos para revelação",
    "Fechar a identidade visual da temporada",
    "Preparar o balanço e o material de prestação de contas",
    "Produzir o estoque inicial de camisas",
    "Definir tabela de preços e promoções",
    "Captar patrocínio específico do evento",
    "Convidar autoridades, parceiros, imprensa e danças convidadas",
    "Organizar sorteios do público e dos sócios",
    "Conseguir prêmios com os parceiros",
    "Definir cardápio e comprar insumos da banca",
    "Montar estrutura: som, projeção, iluminação e decoração",
    "Montar o posto de adesão do Sócio Torcedor",
    "Criar artes de divulgação (teasers antes, programação depois)",
    "Ensaiar a ordem do evento e a revelação",
    "Realizar o evento",
    "Registrar tudo (fotos, vídeos, transmissão)",
    "Publicar prestação de contas, artes do tema e balanço do evento",
], titulo="CHECKLIST DE EXECUÇÃO")

h1(doc, "RISCOS E COMO REDUZIR", 12)
tabela(doc, ["Risco", "Como reduzir"], [
    ["Tema ou camisa não ficarem prontos a tempo",
     "Tema definido ainda em 2026 e arte fechada no D-45; sem isso, o evento muda de data"],
    ["Vazamento da revelação",
     "Lista do que é segredo definida em ata; acesso restrito às artes finais"],
    ["Camisa esgotar ou encalhar",
     "Pré-venda com Pix para dimensionar o lote antes de produzir"],
    ["Prestação de contas confusa",
     "Material visual simples, ensaiado antes, com linguagem acessível"],
    ["Evento longo demais",
     "Roteiro cronometrado; o detalhe do balanço fica no material publicado"],
    ["Público baixo",
     "Divulgação começando 30 dias antes, com teasers e convite direto às famílias dos "
     "brincantes"],
    ["Falha de som ou projeção",
     "Teste no D-2 e no D-1, com equipamento reserva combinado"],
], larguras=[6.0, 10.0])

citacao(doc, "A temporada começa quando a cidade descobre o nosso tema.")
p(doc, "Explosão Junina de Beruri · Arraial de Lançamento", centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Arraial de Lancamento - Plano do Evento.docx")
