# -*- coding: utf-8 -*-
"""Gera 'Projeto Explosao Junina Beruri.docx' — Plano de Reestruturacao 2027."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

# ------------------------------------------------------------------ capa ----
capa(
    doc,
    ["PLANO DE", "REESTRUTURAÇÃO"],
    "Organização, técnica e gestão · Temporada 2027",
    "Da emoção ao método: como a Explosão vai trabalhar a partir de agora.",
    nota="Documento interno da coordenação. Todos os prazos são previsões — "
         "nenhuma data está fechada.",
    rodape="Beruri – Amazonas",
)

# --------------------------------------------------------------- sumário ----
h1(doc, "O QUE TEM NESTE DOCUMENTO")
for item in [
    ("1. Por que este plano existe", "a virada da emoção para a técnica"),
    ("2. O que aprendemos", "diagnóstico honesto, inclusive do tema anterior"),
    ("3. Princípios da reestruturação", "as regras que valem para tudo"),
    ("4. Estrutura organizacional", "diretoria, comissões, grupos e equipes"),
    ("5. O tema e o espetáculo", "como o tema nasce, vira roteiro e vira arena"),
    ("6. Identidade visual e marca", "a cara da Explosão"),
    ("7. Comunicação e redes sociais", "mostrar o trabalho, não só o resultado"),
    ("8. Gestão e transparência", "reuniões, contratos, dinheiro e prestação de contas"),
    ("9. Organização dos ensaios", "filas, método, disputa e evolução"),
    ("10. O sistema da Explosão", "avaliação, bonificação e sócio torcedor"),
    ("11. Captação de recursos", "o novo modelo de arrecadação"),
    ("12. Linha do tempo da temporada", "de agosto de 2026 ao pós-Festival"),
    ("13. Como vamos medir", "indicadores da temporada"),
    ("14. Riscos e como reduzir", "o que pode dar errado"),
    ("15. Visão de futuro", "onde a Explosão quer chegar"),
]:
    bullet(doc, f" — {item[1]}", rotulo=item[0])
p(doc, "Antes dos capítulos, duas páginas de panorama: as novidades da temporada e "
       "o mapa de todos os documentos do projeto.")

doc.add_page_break()

# ------------------------------------------------------------- novidades ----
h1(doc, "AS NOVIDADES DA TEMPORADA 2027")
p(doc, "A reestruturação não é um ajuste — é uma mudança de patamar. Esta página "
       "reúne tudo o que passa a existir e que não existia antes. Cada item tem "
       "capítulo próprio neste documento ou documento inteiro dedicado a ele.")

banner(doc, "A IDEIA QUE COSTURA TUDO",
       "A Explosão deixa de ser uma quadrilha que aparece em julho e passa a ser um "
       "grupo ativo o ano inteiro — sempre em movimento, sempre inovando, sempre "
       "puxando o cenário junino de Beruri.",
       VERMELHO)

tabela(doc, ["Novidade", "O que é", "Onde está detalhado"], [
    ["Novo modelo de custeio",
     "Repasses públicos cobrem a montagem do espetáculo. O brincante não paga blusa "
     "nem produção; a arrecadação deixa de ser sobrevivência e vira estratégia",
     "Capítulo 11"],
    ["Programa Sócio Torcedor",
     "A torcida oficial: contribuição mensal simbólica, com carteirinha, sorteios, "
     "troféus, missões e transparência. É o carro-chefe da arrecadação — e o site "
     "dele já está no ar",
     "Capítulo 11.2 e os dois documentos do programa"],
    ["Arraial de Lançamento",
     "Evento de abertura da temporada: revela tema, itens e camisa, presta contas do "
     "ano anterior e capta sócios",
     "Documento próprio"],
    ["Arraial da Explosão",
     "Projeto de festa própria depois do Festival, com danças convidadas, votação "
     "popular pelo celular e feira do comércio local em parceria com a Prefeitura. "
     "Ainda não aconteceu: é o que se pretende criar",
     "Documento próprio"],
    ["Organograma com nome e responsabilidade",
     "Cargos, grupos de produção e equipes de arena definidos, cada um com o que "
     "entrega e a quem responde. É o que acaba com o acúmulo de função",
     "Capítulo 4 e documento próprio"],
    ["Termo de Compromisso do Brincante",
     "Contrato assinado por todos, com direitos e deveres dos dois lados, anexos "
     "para menores de idade e cessão de imagem",
     "Capítulo 8.4 e o guia do contrato"],
    ["Teto de R$ 80 na bonificação",
     "O Programa de Bonificação passa a ter limite por brincante na temporada: "
     "retorno simbólico garantido, orçamento sob controle",
     "Capítulo 10.2 e o guia do contrato"],
    ["Sistema de Avaliação",
     "Chamada, nota, ranking, ativação automática, advertências e bonificação — no "
     "celular, com o brincante acompanhando o próprio desempenho",
     "Capítulo 10.1"],
    ["Missão de captação de sócios",
     "Trazer sócio torcedor vira missão do brincante, valendo troféu e "
     "reconhecimento — nunca dinheiro, para não tocar o contrato",
     "Capítulo 10.1"],
    ["Ensaio com método",
     "Liderança por filas, estrutura fixa de ensaio, disputa mensal e treinamento "
     "cruzado",
     "Capítulo 9"],
    ["Prestação de contas em dois níveis",
     "Recurso público detalhado e aberto; arrecadação própria com o total divulgado",
     "Capítulo 8.3"],
    ["Identidade visual e comunicação",
     "Marca institucional separada da marca do tema, calendário editorial e rotina "
     "mínima de publicação",
     "Capítulos 6 e 7"],
], larguras=[4.0, 8.0, 4.0], tam=9.5)

h1(doc, "O MAPA DOS DOCUMENTOS")
p(doc, "Este plano é o documento guarda-chuva: ele conta a história inteira e "
       "aponta para os demais. Nenhum outro documento contradiz este — quando "
       "houver divergência, o mais recente vale e os dois são corrigidos.")
tabela(doc, ["Documento", "Para que serve", "Público"], [
    ["Plano de Reestruturação (este)", "A visão completa da temporada 2027",
     "Coordenação"],
    ["Organograma", "Quem faz o quê, o ano todo e no dia do espetáculo",
     "Coordenação e responsáveis"],
    ["Contratos (Termo do Brincante e do Item)", "O instrumento que se assina",
     "Brincantes e responsáveis"],
    ["Guia do Contrato e da Bonificação", "Por que o contrato existe, o que protege "
     "e como a bonificação funciona no sistema", "Coordenação e brincantes"],
    ["Programa Sócio Torcedor — Plano de Implementação", "Como o programa opera por "
     "dentro: papéis, metas, regras e sistema", "Coordenação"],
    ["Programa Sócio Torcedor (divulgação)", "A peça de convite à torcida",
     "Público"],
    ["Arraial de Lançamento — Plano do Evento", "Produção do evento de abertura",
     "Coordenação"],
    ["Arraial da Explosão — Plano do Evento", "Projeto da festa própria da quadrilha",
     "Coordenação e Prefeitura"],
    ["Projetos de Arrecadação", "O portfólio de projetos de reserva",
     "Coordenação"],
    ["Kit Parceiro", "Cotas, contrapartidas e ações com o comércio",
     "Empresas e parceiros"],
], larguras=[5.0, 8.0, 3.0], tam=9.5)

doc.add_page_break()

# ------------------------------------------------------------- 1. porque ----
h1(doc, "POR QUE ESTE PLANO EXISTE", 1)
p(doc, "A Explosão Junina nasceu e cresceu na emoção. Foi a emoção que juntou "
       "gente na quadra, que fez o figurino sair da máquina de costura de "
       "madrugada, que levantou o público e que trouxe o título do Festival "
       "Folclórico de Beruri. Nada disso vai ser jogado fora — a emoção continua "
       "sendo o combustível da quadrilha.")
p(doc, "O que muda é que a emoção deixa de ser o método. Até aqui, boa parte das "
       "decisões foi tomada na urgência, na conversa de corredor e na boa vontade "
       "de poucas pessoas. Isso funcionou enquanto a Explosão era pequena. Hoje a "
       "quadrilha tem mais de cinquenta brincantes, recursos públicos para prestar "
       "contas, parceiros para atender, público para responder e uma reputação a "
       "defender. Nesse tamanho, boa vontade sem organização vira desgaste.")
caixa(doc, "A frase que resume este plano",
      "A Explosão não vai deixar de ser emoção. Ela vai deixar de ser SÓ emoção. "
      "A partir de 2027, cada função tem um dono, cada decisão tem registro, cada "
      "real tem destino anotado e cada brincante tem desempenho medido.",
      VERMELHO)
p(doc, "Este documento é o plano de reestruturação da Explosão Junina de Beruri. "
       "Ele organiza o trabalho que começa em agosto de 2026 — logo depois da "
       "temporada anterior — e se estende até o encerramento da temporada 2027. "
       "Não é um documento de propaganda: é o manual de como a quadrilha passa a "
       "funcionar por dentro.")

h2(doc, "O que muda, na prática")
tabela(doc, ["Antes", "A partir de 2027"], [
    ["Decisão tomada na conversa, sem registro",
     "Decisão de reunião, com ata assinada pelo Secretário"],
    ["Todo mundo faz um pouco de tudo (e ninguém responde por nada)",
     "Organograma com cargos, grupos e responsáveis por nome"],
    ["Tema definido em cima da hora",
     "Tema escolhido e documentado ainda no ano anterior"],
    ["Dinheiro controlado de cabeça",
     "Orçamento por grupo, registro de todo gasto e prestação de contas pública"],
    ["Ensaio conduzido só pelo coreógrafo",
     "Método de ensaio, líderes de fila e avaliação registrada no sistema"],
    ["Arrecadação em regime de emergência o ano todo",
     "Base fixa (repasses + Sócio Torcedor) e projetos pontuais só quando preciso"],
    ["Divulgação só do resultado (o dia do Festival)",
     "Conteúdo o ano todo: bastidor, tema, ensaio, prévia"],
], larguras=[7.5, 8.5])

# ---------------------------------------------------------- 2. diagnóstico --
doc.add_page_break()
h1(doc, "O QUE APRENDEMOS (DIAGNÓSTICO)", 2)
p(doc, "Este diagnóstico não é crítica a quem trabalhou — é registro do que "
       "atrapalhou, para não repetir. Todo ponto listado aqui tem resposta em "
       "algum capítulo deste plano.")

h2(doc, "2.1 O tema anterior: o maior aprendizado")
p(doc, "O tema é o coração do espetáculo. Quando ele chega tarde e mal definido, "
       "todo o resto corre atrás: figurino, alegoria, coreografia, trilha, arte e "
       "divulgação começam sem saber exatamente o que estão construindo. Foi o que "
       "aconteceu no último ciclo, e os efeitos apareceram em todas as frentes.")
for rot, txt in [
    ("Tema definido tarde: ",
     "a produção começou sem conceito fechado, e cada grupo interpretou o tema "
     "do seu jeito. O resultado foi um espetáculo com partes que não conversavam "
     "entre si."),
    ("Conceito sem roteiro escrito: ",
     "“A Bolha do Amor” existia como ideia, não como história. Não havia sinopse, "
     "divisão de atos nem descrição do que cada momento da arena deveria contar. "
     "Sem roteiro, a coreografia não tem a que servir."),
    ("Identidade visual genérica: ",
     "querubins, corações 3D e chamas sem paleta definida, sem tipografia padrão e "
     "sem unidade entre a logo do tema, a camisa e as artes de divulgação. Cada "
     "peça parecia de um grupo diferente."),
    ("Tema não contado ao público: ",
     "quem assistiu chegou na arena sem entender a história. Hoje, boa parte da "
     "disputa acontece fora da arena — quem consegue contar o tema antes chega no "
     "dia com o público já do seu lado."),
    ("Lançamento fragmentado: ",
     "tema, camisa e itens foram aparecendo aos poucos, sem evento próprio. "
     "Enquanto isso, a quadrilha rival lançou tema, camisa e casal de noivos num "
     "único evento coordenado, com identidade visual profissional."),
]:
    bullet(doc, txt, rotulo=rot)
caixa(doc, "A lição",
      "Tema não é ideia: é projeto. Precisa de sinopse, atos, paleta, referências, "
      "responsáveis e calendário — tudo escrito e aprovado antes de a produção "
      "começar. É por isso que, em 2027, o tema é escolhido ainda em 2026.")

h2(doc, "2.2 Identidade visual")
p(doc, "A Explosão não tinha um sistema visual: tinha artes soltas, feitas por "
       "pessoas diferentes, em momentos diferentes, sem paleta, sem tipografia e "
       "sem padrão de assinatura. Marca de quadrilha campeã precisa ser reconhecida "
       "de longe — e a nossa ainda muda de cara a cada publicação.")

h2(doc, "2.3 Comunicação")
p(doc, "As publicações não seguiam calendário: saíam quando alguém lembrava. O "
       "engajamento ficou abaixo da concorrência, o trabalho interno (que é enorme) "
       "não aparecia, e a narrativa do tema nunca foi apresentada ao público de "
       "forma organizada. Perdemos oportunidades de construir expectativa e de "
       "mostrar valor para patrocinadores.")

h2(doc, "2.4 Gestão e organização")
for txt in [
    "Não havia registro público de governança, planejamento ou prestação de contas.",
    "Decisões importantes ficavam apenas na palavra, sem ata — o que gera ruído e "
    "retrabalho quando alguém entende diferente.",
    "A responsabilidade se concentrava em poucas pessoas, que acabavam sobrecarregadas "
    "e sem poder delegar (porque não havia estrutura para delegar).",
    "Os ensaios não seguiam metodologia por filas nem fases de evolução coreográfica.",
    "A relação com os brincantes não era formalizada: ninguém sabia exatamente o que "
    "podia cobrar nem o que tinha direito a receber.",
]:
    bullet(doc, txt)

h2(doc, "2.5 Arrecadação")
p(doc, "A quadrilha vivia em regime de arrecadação permanente: rifa, bingo, venda de "
       "comida, tudo ao mesmo tempo e quase sempre no aperto. Isso consumia a energia "
       "dos brincantes, competia com o tempo de ensaio e ainda assim não dava "
       "previsibilidade de caixa. Com os repasses públicos e o Programa Sócio Torcedor, "
       "esse modelo pode e deve mudar (capítulo 11).")

# -------------------------------------------------------------- 3. princípios
doc.add_page_break()
h1(doc, "PRINCÍPIOS DA REESTRUTURAÇÃO", 3)
p(doc, "Sete princípios valem para todas as áreas. Quando houver dúvida sobre como "
       "agir, a resposta começa por aqui.")
for i, (titulo, texto) in enumerate([
    ("Emoção no palco, técnica nos bastidores",
     "O público tem que se emocionar. Quem organiza, não. Fora da arena, decisão é "
     "critério, prazo e registro."),
    ("Toda função tem um dono com nome",
     "Não existe tarefa “da quadrilha”. Existe tarefa de alguém, com prazo. Sem nome, "
     "a tarefa não foi distribuída."),
    ("Decisão que não é registrada não existe",
     "Reunião sem ata é conversa. O Secretário registra o que foi decidido, quem ficou "
     "responsável e até quando."),
    ("O tema começa fora da arena",
     "A história do ano é contada em prévias, bastidores e conteúdo, desde o "
     "lançamento. No dia do Festival o público já deve conhecer o enredo."),
    ("Dinheiro tem registro e destino",
     "Sem nota, sem recibo, sem lançamento: não existiu. Recurso público tem prestação "
     "de contas detalhada; arrecadação própria tem total público e detalhe interno."),
    ("Desempenho é medido, não sentido",
     "Presença e nota entram no sistema a cada ensaio. Promoção de fila, item e "
     "bonificação seguem dado, não impressão."),
    ("O ano de trabalho começa logo depois do Festival",
     "Agosto não é férias: é quando se faz o balanço, se define a estrutura e se "
     "começa a pensar o tema seguinte."),
], start=1):
    h3(doc, f"{i}. {titulo}")
    p(doc, texto)

# ------------------------------------------------------------- 4. estrutura --
doc.add_page_break()
h1(doc, "ESTRUTURA ORGANIZACIONAL", 4)
p(doc, "A estrutura abaixo é o organograma oficial da Explosão Junina. Ela separa "
       "quem decide, quem produz o ano todo e quem opera no dia do espetáculo. Cada "
       "bloco tem responsáveis designados pela Diretoria.")

banner(doc, "COMO A ESTRUTURA SE ORGANIZA",
       "Diretoria → Comissão de Artes → Grupos de Produção (ano todo) → Equipes de Arena (dia do espetáculo)",
       GRAFITE)
caixa(doc, "O organograma é o coração desta reestruturação",
      "É a partir dele que a Diretoria se organiza, que os papéis são distribuídos e "
      "que cada pessoa passa a saber o que se espera dela. Ele existe para acabar "
      "com o acúmulo de função — quando alguém concentra três frentes, o grupo trava "
      "quando essa pessoa falta — e para responder à pergunta mais prática de todas: "
      "de quem se cobra cada coisa. O documento “Organograma – Explosão Junina” traz "
      "a estrutura completa, com o quadro de nomeação a ser preenchido na reunião da "
      "Diretoria.", VERMELHO)

h2(doc, "4.1 Diretoria")
p(doc, "A Diretoria responde pela quadrilha: institucionalmente, financeiramente e "
       "juridicamente. São seis cargos, com atribuições que não se sobrepõem.")
tabela(doc, ["Cargo", "O que responde"], [
    ["Presidente",
     "Representação institucional externa, assinatura final de contratos e documentos "
     "oficiais e decisão de última instância em conflito entre grupos. É quem bate o "
     "martelo quando o assunto passa da alçada dos outros diretores."],
    ["Vice-Presidente",
     "Suplência direta do Presidente (assume ausências e impedimentos) e apoio na "
     "representação institucional. Papel de continuidade: a estrutura não pode travar "
     "quando o Presidente não está."],
    ["Diretor Financeiro",
     "Orçamento, controle de gastos, prestação de contas, pagamento de fornecedores e "
     "colaboradores. Formaliza qualquer valor acordado por outro diretor (ex.: cachê "
     "negociado pelo Diretor de Eventos). Tem acesso de leitura ao painel de "
     "Bonificação do sistema."],
    ["Diretor Secretário",
     "Atas de reunião, documentação oficial, ofícios e registro formal das decisões da "
     "Diretoria e da Comissão de Artes. É quem transforma decisão em documento."],
    ["Diretor de Eventos",
     "Relações externas, negociação e fechamento de apresentações em outros municípios "
     "e contratos de apresentação. Negocia o acordo; o valor final passa pelo "
     "Financeiro para formalização e pagamento."],
    ["Diretor de Tecnologia",
     "Sistemas web (Sistema de Avaliação, Sócio Torcedor, Cine Explosão), site e toda a "
     "parte de hardware e mecânica aplicada ao espetáculo — LEDs de figurino, "
     "mecanismos de alegoria, tecnologia embarcada na arena. Tem assento na Comissão de "
     "Artes, respondendo pela viabilidade técnica das ideias."],
], larguras=[4.0, 12.0])

h2(doc, "4.2 Comissão de Artes")
p(doc, "A Comissão de Artes não é um cargo: é a própria Diretoria reunida em função "
       "artística, com um responsável designado para conduzir a pauta do dia a dia — "
       "assim nem toda decisão pequena precisa de reunião coletiva.")
p(doc, "Ela decide:")
for txt in [
    "tema do ano, história e roteiro;",
    "divisão em atos e script do espetáculo de arena;",
    "estética, cores e conceito visual da temporada;",
    "conceito de figurino e de alegoria por ato;",
    "o que é surpresa (não vai para as redes) e o que pode virar prévia.",
]:
    bullet(doc, txt)
p(doc, "A partir dessas decisões, a Comissão formaliza as encomendas para os Grupos "
       "de Produção — por escrito, com prazo. Nenhum grupo começa a produzir sem a "
       "encomenda registrada.")

h2(doc, "4.3 Grupos de Produção (ano todo)")
tabela(doc, ["Grupo", "O que faz"], [
    ["Alegorias e Cenário",
     "Desenho e construção física das alegorias e do cenário definidos pela Comissão de "
     "Artes, incluindo o planejamento de translado até o local da apresentação."],
    ["Figurino",
     "Desenho e confecção das indumentárias conforme o conceito estético aprovado, "
     "controle de medidas, provas e manutenção das peças."],
    ["Música e Coreografia",
     "Coordenação de dança, planejamento dos ensaios, criação da coreografia, escolha "
     "do repertório, trilha entre atos e gravação do áudio do teatro."],
    ["Planejamento de Arena e Cronograma",
     "Calcula o tamanho da arena, define a posição de cada elemento e de cada brincante "
     "e cronometra cada etapa: montagem de cenário e alegoria, tempo de show e "
     "desmontagem."],
    ["Comunicação",
     "Divulgação do grupo e do espetáculo: identidade visual, artes, fotografia, vídeo, "
     "calendário editorial, cobertura de ensaios e relação com a imprensa. Reúne os "
     "designers e o jornalista da equipe."],
], larguras=[4.5, 11.5])

h2(doc, "4.4 Equipes de Arena (dia do espetáculo)")
tabela(doc, ["Equipe", "O que faz no dia"], [
    ["Regência de Cena",
     "Comanda em tempo real durante a apresentação: distribui função e indica o momento "
     "exato de cada equipe agir. É a autoridade central no dia do show."],
    ["Equipe de Palco", "Empurra alegoria, abre e fecha painel de cenário."],
    ["Efeitos e Movimentação Mecânica",
     "Aciona efeitos especiais e comanda a movimentação mecânica das alegorias."],
    ["Figurino e Camarim", "Troca de figurino em cena, sincronizada com os atos."],
    ["Adereços em Cena",
     "Recolhe adereços e peças de figurino que caem na arena durante a dança."],
    ["Som", "Sonoplastia, playback e sincronia direta com a Regência de Cena."],
], larguras=[4.5, 11.5])

h2(doc, "4.5 Como as decisões fluem")
tabela(doc, ["Assunto", "Quem decide", "Quem registra/formaliza"], [
    ["Tema, roteiro, estética, figurino, alegoria", "Comissão de Artes", "Secretário"],
    ["Qualquer valor a pagar ou receber", "Diretor Financeiro", "Financeiro + Secretário"],
    ["Apresentação fora de Beruri, cachê, contrato externo", "Diretor de Eventos", "Financeiro + Presidente"],
    ["Viabilidade técnica de efeito, mecanismo e sistema", "Diretor de Tecnologia", "Comissão de Artes"],
    ["Conflito entre grupos ou impasse", "Presidente", "Secretário"],
    ["Convocação, escala e método de ensaio", "Grupo de Música e Coreografia", "Sistema de Avaliação"],
    ["O que vai (e o que não vai) para as redes", "Comissão de Artes + Comunicação", "Comunicação"],
], larguras=[7.0, 4.5, 4.5])

h2(doc, "4.6 Regras de funcionamento")
for rot, txt in [
    ("Reunião da Diretoria: ", "mensal fora da temporada e quinzenal a partir do início "
     "dos ensaios; extraordinária sempre que houver decisão urgente."),
    ("Ata obrigatória: ", "toda reunião gera ata com decisões, responsáveis e prazos. "
     "A ata é arquivada e compartilhada com a Diretoria."),
    ("Responsável por grupo: ", "cada Grupo de Produção tem um responsável designado, que "
     "responde pelas entregas e leva as demandas à Comissão de Artes."),
    ("Orçamento por grupo: ", "cada grupo apresenta a previsão de custos da sua área ao "
     "Diretor Financeiro antes de começar a produzir."),
    ("Ninguém compra por conta própria: ", "toda compra passa pelo Financeiro, com "
     "registro e comprovante."),
    ("Escala do dia do espetáculo: ", "as Equipes de Arena são definidas e treinadas com "
     "antecedência, não montadas na hora."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------------ 5. tema --
doc.add_page_break()
h1(doc, "O TEMA E O ESPETÁCULO", 5)
p(doc, "O tema é a decisão mais importante do ano — é dele que saem figurino, "
       "alegoria, coreografia, trilha, arte, camisa e conteúdo. Por isso ele deixa de "
       "ser escolhido no começo da temporada e passa a ser escolhido no ano anterior.")

h2(doc, "5.1 Como o tema é escolhido")
tabela(doc, ["Etapa", "O que acontece", "Quem conduz"], [
    ["1. Propostas",
     "Qualquer membro pode propor um tema, apresentando ideia central, o que se quer "
     "contar e por que combina com a Explosão.", "Comissão de Artes"],
    ["2. Filtro de viabilidade",
     "Cada proposta é avaliada quanto a custo, complexidade de alegoria, tempo de "
     "montagem, viabilidade técnica e capacidade de virar coreografia.",
     "Tecnologia + Alegorias + Coreografia"],
    ["3. Escolha",
     "A Comissão escolhe o tema e registra em ata a justificativa da escolha.",
     "Comissão de Artes"],
    ["4. Documento do tema",
     "O tema escolhido vira documento escrito, base de todo o trabalho do ano.",
     "Comissão + Secretário"],
], larguras=[3.2, 8.8, 4.0])

h2(doc, "5.2 O documento do tema")
p(doc, "Antes de qualquer produção começar, o tema precisa estar escrito. O documento "
       "do tema contém, no mínimo:")
for txt in [
    "sinopse: a história em um parágrafo, do jeito que será contada ao público;",
    "divisão em atos: o que acontece em cada momento do espetáculo e qual emoção "
    "cada ato deve provocar;",
    "personagens e itens: papel do marcador, do casal de noivos e do casal real "
    "dentro da história;",
    "paleta de cores e referências visuais: imagens, texturas e materiais;",
    "elementos de cena: alegorias, efeitos e mecanismos previstos por ato;",
    "trilha e sonoridade: estilo musical, transições e clima entre atos;",
    "o que é surpresa: a lista do que não pode vazar antes do Festival.",
]:
    bullet(doc, txt)

h2(doc, "5.3 Do tema ao espetáculo")
tabela(doc, ["Etapa", "Produto esperado", "Responsável"], [
    ["Roteiro e atos", "Script do espetáculo com tempo previsto por ato", "Comissão de Artes"],
    ["Coreografia", "Coreografia por ato, com marcações e formações", "Música e Coreografia"],
    ["Figurino", "Desenho, ficha técnica, medidas e cronograma de confecção", "Figurino"],
    ["Alegoria e cenário", "Projeto, materiais, orçamento e plano de translado", "Alegorias e Cenário"],
    ["Arena", "Mapa de posições e cronômetro de montagem, show e desmontagem", "Planejamento de Arena"],
    ["Som e trilha", "Trilha final, transições e áudio do teatro gravado", "Música e Coreografia"],
    ["Comunicação", "Identidade do tema, calendário de conteúdo e plano de prévias", "Comunicação"],
], larguras=[4.0, 8.0, 4.0])

h2(doc, "5.4 Viabilidade antes da vontade")
p(doc, "Toda ideia criativa passa por cinco perguntas antes de ser aprovada. Se a "
       "resposta de alguma delas for “não sei”, a ideia volta para ajuste:")
for txt in [
    "Cabe na arena, no tempo de apresentação e nas regras do Festival?",
    "Dá para construir, transportar e montar com a estrutura que temos?",
    "Temos gente suficiente para operar isso no dia?",
    "Cabe no orçamento previsto para o grupo responsável?",
    "Existe plano B se o mecanismo, o efeito ou o material falhar?",
]:
    bullet(doc, txt)

h2(doc, "5.5 O tema fora da arena")
p(doc, "Hoje conta muito conseguir desenvolver o tema fora da arena. Quem só aparece "
       "no dia do Festival disputa com desvantagem: o público chega sem repertório, "
       "sem vínculo e sem entender a proposta. A Explosão vai contar o tema o ano "
       "todo — respeitando o que foi definido como surpresa.")
for rot, txt in [
    ("Prévias: ", "trechos de coreografia, ensaios abertos, apresentações em eventos e "
     "escolas, aparições dos itens caracterizados."),
    ("Bastidor: ", "a costura, a construção da alegoria, a pintura, o teste de efeito, "
     "a correria real da produção."),
    ("Narrativa: ", "conteúdo que explica a história do tema em partes, como capítulos, "
     "até a revelação completa."),
    ("Regra da surpresa: ", "o que a Comissão de Artes marcou como surpresa não aparece "
     "em nenhuma rede, em nenhuma hipótese, até o Festival."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------- 6. identidade visual
doc.add_page_break()
h1(doc, "IDENTIDADE VISUAL E MARCA", 6)
p(doc, "A Explosão precisa ser reconhecida antes de ser lida. Isso exige um sistema "
       "visual — não artes avulsas. O redesenho da identidade está previsto para "
       "janeiro e fevereiro de 2027, já em cima do tema definido no ano anterior.")

h2(doc, "6.1 Duas marcas, funções diferentes")
tabela(doc, ["Marca", "Muda?", "Para que serve"], [
    ["Marca da Explosão", "Não muda",
     "Identidade permanente da quadrilha: usada em documentos, uniformes, redes, "
     "parceiros e institucional. É o que fica de patrimônio."],
    ["Marca do tema", "Muda a cada temporada",
     "Derivada da marca principal, traduz a estética do tema do ano: camisa, artes de "
     "divulgação, cenário e material do evento de lançamento."],
], larguras=[3.5, 3.0, 9.5])

h2(doc, "6.2 O que compõe o sistema visual")
for txt in [
    "logo oficial da quadrilha, com versões (colorida, monocromática, reduzida);",
    "logo do tema da temporada, derivada da identidade principal;",
    "paleta de cores oficial, com a variação específica da temporada;",
    "tipografia padrão para todos os materiais;",
    "templates de post, story, cartaz, banner e certificado;",
    "design da camisa oficial e do uniforme de ensaio;",
    "padrão de assinatura das artes (logo, @ do perfil e crédito dos parceiros).",
]:
    bullet(doc, txt)

h2(doc, "6.3 Regras de uso")
for rot, txt in [
    ("Nada fora do padrão: ", "arte publicada nas redes oficiais passa pelo Grupo de "
     "Comunicação. Arte improvisada enfraquece a marca."),
    ("Aprovação: ", "a identidade do tema é aprovada pela Comissão de Artes antes de "
     "qualquer aplicação."),
    ("Arquivo aberto: ", "todos os arquivos editáveis ficam guardados pela Comunicação — "
     "a marca é da quadrilha, não de quem desenhou."),
    ("Parceiros: ", "logos de parceiros seguem posição e tamanho definidos por cota, "
     "conforme o Kit Parceiro."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------ 7. comunicação
doc.add_page_break()
h1(doc, "COMUNICAÇÃO E REDES SOCIAIS", 7)
p(doc, "A regra de ouro da comunicação da Explosão a partir de agora: mostrar o "
       "trabalho, não só o resultado. O público se conecta com o esforço — a "
       "madrugada de costura, o ensaio suado, o mecanismo que quase não funcionou, a "
       "correria da montagem. É isso que transforma espectador em torcedor, e "
       "torcedor em sócio.")

h2(doc, "7.1 O que publicar")
tabela(doc, ["Tipo de conteúdo", "Exemplos"], [
    ["Organização interna",
     "reunião da Diretoria, definição de grupos, planejamento, ata sendo assinada, "
     "estrutura da temporada — mostrar que existe método por trás"],
    ["A correria",
     "montagem de alegoria, teste de efeito, prova de figurino, madrugada de trabalho, "
     "carga e descarga, imprevisto resolvido"],
    ["Ensaios",
     "aquecimento, trabalho por fila, disputa mensal, evolução do grupo, o antes e "
     "depois de uma coreografia"],
    ["Desenvolvimento do tema",
     "referências, esboços, escolha de cores, construção do enredo (sem entregar o que "
     "é surpresa)"],
    ["Prévias",
     "trechos de coreografia, itens caracterizados, apresentações fora da arena, teaser "
     "de alegoria"],
    ["Gente",
     "perfis de brincantes, líderes de fila, costureiras, equipe de arena, torcedores e "
     "sócios"],
    ["Transparência e parceiros",
     "prestação de contas, balanço de eventos, agradecimento e contrapartida de "
     "patrocinadores"],
], larguras=[4.5, 11.5])

h2(doc, "7.2 Calendário editorial por fases")
tabela(doc, ["Fase", "Período previsto", "Foco"], [
    ["0 — Reestruturação", "Agosto a outubro de 2026",
     "Balanço da temporada, apresentação da nova estrutura, chamada para o Sócio "
     "Torcedor e para o time de produção"],
    ["1 — Construção do tema", "Novembro de 2026 a janeiro de 2027",
     "Bastidor da criação, enquetes, contagem regressiva, teasers sem entregar o tema"],
    ["2 — Lançamento", "Previsão: março de 2027",
     "Revelação de tema, camisa e itens no Arraial de Lançamento; prestação de contas; "
     "cobertura completa do evento"],
    ["3 — Preparação", "Março a junho de 2027",
     "Cobertura de ensaios, perfis, disputa entre filas, prévias, construção de alegoria "
     "e figurino"],
    ["4 — Festival", "Julho de 2027",
     "Cobertura ao vivo, stories em tempo real, interação com o público, registro "
     "profissional do espetáculo"],
    ["5 — Pós-Festival", "Agosto de 2027 em diante",
     "Agradecimentos, melhores momentos, balanço da temporada, Arraial da Explosão e "
     "abertura do ciclo seguinte"],
], larguras=[3.8, 4.2, 8.0])

h2(doc, "7.3 Rotina mínima")
for rot, txt in [
    ("Frequência: ", "pelo menos três publicações por semana no feed e presença diária "
     "nos stories durante a temporada."),
    ("Cobertura de ensaio: ", "todo ensaio gera registro — foto, vídeo ou story. Sem "
     "cobertura, o trabalho não existe para quem está de fora."),
    ("Responsável: ", "o Grupo de Comunicação produz; a Comissão de Artes aprova o que "
     "envolve tema e surpresa."),
    ("Banco de conteúdo: ", "todo material bruto é arquivado — vira conteúdo na "
     "entressafra e acervo histórico da quadrilha."),
    ("Imprensa: ", "releases para portais, blogs e rádios regionais nos marcos da "
     "temporada (lançamento, Festival, Arraial)."),
]:
    bullet(doc, txt, rotulo=rot)

# --------------------------------------------------- 8. gestão/transparência
doc.add_page_break()
h1(doc, "GESTÃO E TRANSPARÊNCIA", 8)

h2(doc, "8.1 Reuniões e registro")
p(doc, "A quadrilha passa a funcionar em ciclo de reuniões, com pauta e ata. O "
       "Secretário registra decisão, responsável e prazo; o registro é o que permite "
       "cobrar depois sem desgaste pessoal.")
tabela(doc, ["Reunião", "Quando", "Pauta típica"], [
    ["Diretoria", "Mensal (quinzenal na temporada)",
     "Andamento dos grupos, dinheiro, prazos, pendências e decisões"],
    ["Comissão de Artes", "Conforme o ciclo criativo",
     "Tema, roteiro, estética, aprovações e encomendas aos grupos"],
    ["Grupos de Produção", "Definida por cada grupo",
     "Execução, materiais, cronograma e dificuldades"],
    ["Geral com brincantes", "Marcos da temporada",
     "Contrato, regras, calendário, prestação de contas e avisos"],
], larguras=[4.0, 4.5, 7.5])

h2(doc, "8.2 Dinheiro: como passa a ser tratado")
for rot, txt in [
    ("Orçamento por grupo: ", "cada Grupo de Produção estima seus custos antes de "
     "produzir; o Financeiro consolida o orçamento da temporada."),
    ("Registro obrigatório: ", "sem nota, recibo ou lançamento, o gasto não existiu. "
     "Vale para compra grande e para o lanche do ensaio."),
    ("Autorização: ", "compras passam pelo Financeiro. Valores acordados por outros "
     "diretores só são pagos após formalização."),
    ("Mini-balanço por projeto: ", "todo evento ou ação de arrecadação fecha com "
     "receitas, custos e resultado — e é publicado."),
    ("Caixa separado: ", "recurso público, arrecadação própria e Sócio Torcedor são "
     "controlados separadamente, porque prestam contas de formas diferentes."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "8.3 Prestação de contas em dois níveis")
tabela(doc, ["Nível", "O que é divulgado", "Onde"], [
    ["I — Recursos públicos\n(transparência total)",
     "Verbas recebidas (Lei Paulo Gustavo, editais e fomentos municipais, estaduais e "
     "federais), detalhamento de aplicação, entregas e comprovação. É obrigação legal.",
     "Arraial de Lançamento + publicação nas redes"],
    ["II — Arrecadação própria\n(apenas total público)",
     "Valor total arrecadado com recursos próprios (parcerias, camisas, eventos, "
     "doações, Sócio Torcedor). O detalhe por fonte e por parceiro fica registrado "
     "internamente — é informação estratégica.",
     "Total nas redes; detalhe em reunião interna"],
    ["III — Patrimônio\n(opcional, recomendado)",
     "O que a quadrilha possui: figurinos, som, equipamentos, estoque de camisas e "
     "materiais construídos.",
     "Arraial de Lançamento"],
], larguras=[4.0, 8.0, 4.0])
caixa(doc, "Por que isso importa",
      "Transparência gera confiança de brincante, parceiro e comunidade — e é "
      "diferencial competitivo: nenhuma quadrilha de Beruri faz isso, e poucas no "
      "Amazonas adotam a prática. Para o Sócio Torcedor, é o principal argumento de "
      "adesão.", VERDE)

h2(doc, "8.4 Contratos")
p(doc, "A relação com o brincante passa a ser formalizada pelo Termo de Compromisso "
       "do Brincante, com assinatura prevista para fevereiro de 2027, antes do início "
       "efetivo dos ensaios. O contrato protege os dois lados:")
tabela(doc, ["A quadrilha se compromete a", "O brincante se compromete a"], [
    ["Fornecer, sem custo, o figurino completo e a blusa do tema para as apresentações "
     "oficiais",
     "Manter frequência mínima nos ensaios e avisar faltas com antecedência"],
    ["Providenciar a produção das apresentações oficiais (figurino, adereços e itens de "
     "palco)",
     "Respeitar o código de conduta, a coordenação e os colegas"],
    ["Manter o Programa de Bonificação, com regras claras e registro no sistema",
     "Participar das atividades do compromisso (arrecadação, braçal e comunitário) "
     "quando convocado"],
    ["Prestar contas dos recursos e informar o calendário com antecedência",
     "Zelar pelo figurino e devolvê-lo conforme o combinado"],
    ["Tratar imagem e dados pessoais conforme autorizado no termo",
     "Autorizar o uso de imagem para divulgação da quadrilha"],
], larguras=[8.0, 8.0])
for rot, txt in [
    ("Menor de idade: ", "assinatura acompanhada dos anexos de autorização do "
     "responsável e de viagem."),
    ("Itens: ", "marcador, casal de noivos e casal real têm termo próprio, com exigência "
     "de frequência maior."),
    ("Fornecedores e parceiros: ", "acordo simples por escrito, com contrapartidas e "
     "prazos registrados pelo Secretário."),
    ("Guia de leitura: ", "o documento “Contrato e Bonificação — Guia Explicativo” "
     "explica, em linguagem simples, por que o contrato existe, o que ele protege, "
     "qual é o valor jurídico de cada cláusula e como o Programa de Bonificação "
     "funciona dentro do sistema. É o material da reunião de assinatura."),
    ("Por que isso importa juridicamente: ", "o Termo afasta expressamente o vínculo "
     "empregatício, autoriza o uso de imagem, cobre a participação de menores de "
     "idade com os anexos do responsável e garante direito de defesa antes de "
     "qualquer sanção."),
]:
    bullet(doc, txt, rotulo=rot)

# ---------------------------------------------------------------- 9. ensaios
doc.add_page_break()
h1(doc, "ORGANIZAÇÃO DOS ENSAIOS", 9)
p(doc, "O ensaio é onde a temporada é ganha. A partir de 2027 ele tem método, "
       "liderança distribuída e avaliação registrada. Início previsto para fevereiro, "
       "junto com a assinatura dos contratos.")

h2(doc, "9.1 Liderança por filas")
p(doc, "Cada fila tem um líder designado pela coordenação, responsável por manter o "
       "alinhamento, acompanhar a evolução da sua fila e garantir que os passos "
       "estejam em dia. A liderança é rotativa: forma novos líderes e evita "
       "centralização. O líder de fila reporta ao coreógrafo e à coordenação. Essa "
       "estrutura distribui a responsabilidade que hoje recai inteiramente sobre o "
       "coreógrafo e torna viável conduzir mais de cinquenta pessoas.")

h2(doc, "9.2 Estrutura do ensaio")
tabela(doc, ["Momento", "Duração", "Atividade"], [
    ["Aquecimento", "15 min", "Alongamento e integração do grupo"],
    ["Geral", "30 min", "Passagem da coreografia completa com todos os brincantes"],
    ["Por filas", "45 min",
     "Trabalho específico por fila com o líder: correção de passos, sincronia e "
     "expressão. Enquanto uma fila trabalha, as demais observam"],
    ["Dinâmica", "20 min",
     "Ensaio combinado (2 ou 3 filas), duelo entre filas ou troca de lados"],
    ["Passagem final", "20 min", "Ensaio geral com a coreografia corrigida"],
    ["Encerramento", "10 min", "Feedback coletivo, avaliação, avisos e motivação"],
], larguras=[3.5, 2.5, 10.0])

h2(doc, "9.3 Dinâmicas de treinamento")
for rot, txt in [
    ("Ensaio combinado: ", "duas ou três filas ensaiam juntas para treinar sincronia "
     "entre grupos adjacentes, simulando a condição real de apresentação."),
    ("Duelo entre filas: ", "duas filas executam a mesma sequência e a coordenação "
     "avalia qual foi melhor. Rivalidade saudável e esforço coletivo."),
    ("Troca de lados: ", "brincantes trocam de fila temporariamente para aprender a "
     "coreografia do lado oposto."),
    ("Destaque individual: ", "brincantes executam trechos sozinhos para avaliação, "
     "revelando talentos para funções de item."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "9.4 Disputa mensal entre filas")
for txt in [
    "Um dia fixo por mês é dedicado à disputa entre filas.",
    "Cada fila apresenta a coreografia e recebe nota da coordenação (sincronia, "
    "expressão, energia e alinhamento).",
    "A fila vencedora recebe reconhecimento público: post nas redes e destaque no "
    "ensaio seguinte.",
    "Os resultados acumulados ajudam a definir a formação final para o Festival.",
    "A disputa também é momento de avaliação formal para o Programa de Bonificação.",
]:
    bullet(doc, txt)

h2(doc, "9.5 Mobilidade e treinamento cruzado")
p(doc, "A posição nas filas não é fixa. Com base nas avaliações e nas disputas "
       "mensais, a coordenação pode promover brincantes dentro da fila, reposicionar "
       "entre filas para equilibrar o nível técnico, promover uma fila inteira que "
       "evoluiu em conjunto e identificar candidatos a item. A mobilidade gera um "
       "desconforto saudável: mudar de lado ou de posição obriga o brincante a se "
       "adaptar.")
p(doc, "todo brincante deve saber dançar toda a coreografia, "
       "independentemente do lado ou da posição. Quem está do lado direito também "
       "sabe os passos do esquerdo. Assim, substituição de última hora não compromete "
       "o espetáculo, remanejamento acontece sem prejuízo e o nível técnico do cordão "
       "sobe. Ensaios de troca de lado são obrigatórios e periódicos.",
  bold_ate="O princípio é simples: ")

h2(doc, "9.6 Presença e avaliação")
p(doc, "Presença e nota (1 a 5) são registradas a cada ensaio no Sistema de "
       "Avaliação, alimentando o ranking, o perfil de cada brincante e o Programa de "
       "Bonificação. A chamada é feita no dia; a nota pode ser lançada depois. Falta "
       "avisada com antecedência é registrada como justificada. O brincante acompanha "
       "o próprio desempenho e sabe o que precisa melhorar para subir de fila ou se "
       "candidatar a item.")

# ---------------------------------------------------------------- 10. sistema
doc.add_page_break()
h1(doc, "O SISTEMA DA EXPLOSÃO", 10)
p(doc, "A tecnologia é uma das vantagens competitivas da Explosão. Três sistemas "
       "próprios sustentam a gestão da temporada, todos sob responsabilidade da "
       "Diretoria de Tecnologia.")

h2(doc, "10.1 Sistema de Avaliação")
p(doc, "É a espinha dorsal da gestão dos brincantes. Funciona no navegador, no "
       "celular ou no computador, com acesso separado para coordenação e brincante.")
tabela(doc, ["Recurso", "O que faz"], [
    ["Cadastro de brincantes",
     "Dados pessoais, fila, posição, tipo (brincante, item, coordenação), contrato, "
     "anexos de menor de idade e situação do membro. Permite cadastro em lote por "
     "planilha"],
    ["Agenda de eventos",
     "Ensaios, ensaiões, apresentações, festival, igreja e atividades do compromisso "
     "(arrecadação, braçal, comunitário), com status planejado, realizado ou cancelado"],
    ["Chamada e avaliação",
     "Presença por brincante, falta justificada, nota de 1 a 5 e observação de "
     "desempenho, salvas em tempo real"],
    ["Ranking e dashboard",
     "Frequência, média de notas e evolução do grupo e de cada fila"],
    ["Perfil do brincante",
     "O brincante vê a própria presença, notas, situação da ativação, bonificação "
     "acumulada e dicas do que melhorar"],
    ["Advertências",
     "Registro de advertência verbal, formal, desligamento e falta grave, com efeito "
     "sobre a bonificação"],
    ["Missão de captação de sócios",
     "O brincante declara quem trouxe para o Programa Sócio Torcedor e a coordenação "
     "confirma. Vale desempenho e troféu — nunca dinheiro: não entra na frequência, "
     "no ranking nem na bonificação, e por isso não toca o contrato"],
    ["Configurações e logs",
     "Valores, prazos e regras da temporada ajustáveis pela coordenação; todo registro "
     "fica logado"],
], larguras=[4.5, 11.5])
caixa(doc, "O que não está no sistema não aconteceu",
      "Cada presença, nota, advertência e alteração fica registrada com data, hora e "
      "autor. É isso que permite ao brincante contestar durante a temporada, e não "
      "depois; e é isso que sustenta qualquer decisão da coordenação sobre "
      "bonificação, promoção de fila ou desligamento.", AZUL)

h2(doc, "10.2 Programa de Bonificação")
p(doc, "O Programa de Bonificação transforma presença e desempenho em um valor "
       "acumulado ao longo da temporada, conforme o Termo de Compromisso. Não é "
       "salário: é reconhecimento pelo compromisso.")
tabela(doc, ["Regra", "Como funciona"], [
    ["Adesão", "Opcional, feita na assinatura do contrato e permitida até o prazo "
               "definido na configuração da temporada"],
    ["Ativação", "Nos primeiros meses (janela proporcional à data de adesão) o brincante "
                 "precisa atingir frequência e nota mínimas para ativar a bonificação. "
                 "Itens têm exigência de frequência maior"],
    ["Acúmulo", "Começa ao fim da ativação individual e vai até o Festival. Cada tipo de "
                "evento tem um valor; eventos podem ter valor específico"],
    ["Teto da temporada", "Novidade de 2027: o acumulado por brincante para em "
                          "R$ 80,00. Ao chegar no teto, ele mantém o que tem e deixa "
                          "de somar. O sistema mostra quanto falta para alcançá-lo"],
    ["Atividades do compromisso", "Arrecadação, braçal e comunitário registram presença, "
                                  "mas não geram valor nem entram na frequência"],
    ["Advertências", "Advertência formal reduz o total acumulado; desligamento por falta "
                     "grave zera"],
    ["Pagamento", "Feito após o Festival, na data informada pela coordenação, podendo "
                  "ser em parcelas"],
    ["Destino", "Ao fim da contagem, o brincante escolhe resgatar o valor ou doá-lo à "
                "quadrilha. A escolha é registrada no sistema"],
], larguras=[4.5, 11.5])
caixa(doc, "Por que o teto de R$ 80",
      "O programa precisa dar um retorno simbólico a quem se dedicou sem virar uma "
      "despesa que a quadrilha não sabe de antemão quanto será — o custo dependeria "
      "de quantos convites de apresentação aparecessem na temporada, e isso ninguém "
      "controla. Com os valores atuais, o máximo possível por brincante é R$ 44,00; "
      "o teto é a garantia de que, mudando os valores ou o tamanho da temporada, o "
      "compromisso máximo continua conhecido. A explicação completa está no "
      "documento “Contrato e Bonificação — Guia Explicativo”.", AMBAR)

h2(doc, "10.3 Site do Sócio Torcedor")
p(doc, "Sistema separado, dedicado ao programa de sócios, e já no ar. A coordenação "
       "cadastra sócios e confirma pagamentos com data e hora reais; o sócio entra "
       "com CPF e data de nascimento e encontra carteirinha digital, situação do mês, "
       "progresso da temporada, histórico, troféus, missões, mural, troca de nível e "
       "a prestação de contas da quadrilha.")
tabela(doc, ["Módulo", "Situação"], [
    ["Painel da coordenação (cadastro, pagamentos, fila de confirmação, lembretes, "
     "finanças, importação por planilha)", "Pronto"],
    ["Painel do sócio (carteirinha, situação, progresso, histórico, troca de nível, "
     "mural, finanças)", "Pronto"],
    ["Troféus e conquistas — as dez do catálogo", "Pronto"],
    ["Sorteios, com lista congelada e registro de entrega do prêmio", "Pronto"],
    ["Missões semanais, com pontos retidos e validação em lote", "Pronto"],
    ["Ranking da temporada e notificações", "A fazer"],
    ["Página pública e adesão online", "A fazer"],
    ["Comprovante de pagamento por imagem", "Depende de conta externa"],
], larguras=[11.5, 4.5], tam=9.5)
p(doc, "Tudo detalhado no “Programa Sócio Torcedor — Plano de Implementação”.")

h2(doc, "10.4 O que ainda vai ser construído")
for rot, txt in [
    ("Votação popular em tempo real: ", "para a competição do Arraial da Explosão, com "
     "apuração e resultado divulgados na hora — com plano B offline obrigatório."),
    ("Cadastro das bancas do Arraial: ", "formulário de inscrição do edital da feira, "
     "seleção, confirmação e mapa dos espaços demarcados."),
    ("Painel público de transparência: ", "página aberta com o balanço da temporada, "
     "alimentada pelos registros financeiros."),
    ("Venda de camisa e ingresso: ", "registro de pedidos, pagamento por Pix e controle "
     "de estoque para eventos."),
    ("Certificados e troféus: ", "geração automática de certificados de participação para "
     "as danças convidadas do Arraial."),
]:
    bullet(doc, txt, rotulo=rot)

# ------------------------------------------------------------- 11. captação --
doc.add_page_break()
h1(doc, "CAPTAÇÃO DE RECURSOS — O NOVO MODELO", 11)
p(doc, "Este é o capítulo que mais muda em relação ao que a quadrilha fazia. A "
       "Explosão hoje conta com apoio financeiro da Prefeitura, além de repasses "
       "estaduais e federais. São recursos que dão folga para planejar o espetáculo "
       "com antecedência — e que, em troca, exigem prestação de contas detalhada.")
p(doc, "Com essa base, a arrecadação deixa de ser sobrevivência e passa a ser "
       "estratégia. A quadrilha para de viver de evento em evento e passa a ter uma "
       "receita recorrente, dois eventos-âncora e um portfólio de projetos guardado "
       "para quando houver necessidade.")

banner(doc, "O NOVO MODELO EM UMA LINHA",
       "Repasses públicos = base · Sócio Torcedor = carro-chefe · Lançamento e Arraial = eventos-âncora · Demais projetos = reserva acionável",
       VERMELHO)

h2(doc, "11.1 A base: recursos públicos")
for txt in [
    "Repasses municipais, estaduais e federais custeiam a montagem do espetáculo.",
    "Com isso, o brincante não paga blusa da temporada nem as despesas do espetáculo.",
    "Exceção: em eventos grandes que exigem maquiagem e cabelo, cada brincante custeia "
    "a própria produção — e a quadrilha busca pacote com parceiros para baratear.",
    "Contrapartida obrigatória: prestação de contas detalhada e pública de cada recurso "
    "público recebido.",
]:
    bullet(doc, txt)

h2(doc, "11.2 O carro-chefe: Programa Sócio Torcedor")
p(doc, "O Sócio Torcedor é a principal frente de arrecadação da Explosão a partir de "
       "2027. Contribuição simbólica, mensal ou por temporada, de qualquer pessoa da "
       "comunidade que queira apoiar a quadrilha o ano inteiro.")
for rot, txt in [
    ("Por que é o carro-chefe: ", "é receita recorrente e previsível, entra o ano todo, "
     "não depende de evento, custa pouco para operar e cria comunidade em volta da "
     "quadrilha."),
    ("Como funciona: ", "níveis com valores simbólicos, benefícios progressivos, "
     "carteirinha, conteúdo exclusivo, sorteios com chance igual para todos, descontos e "
     "acesso à prestação de contas."),
    ("Meta da temporada: ", "100 sócios — cerca de R$ 1.500 por mês e R$ 15.000 nos "
     "dez meses de contribuição (fevereiro a novembro). Com cinquenta brincantes "
     "trazendo dois cada, a meta é atingida sem campanha externa."),
    ("O site já está no ar: ", "a coordenação cadastra e confirma pagamentos; o sócio "
     "entra com CPF e data de nascimento e acompanha tudo. Falta a página pública "
     "com adesão online."),
    ("Onde está detalhado: ", "documento “Programa Sócio Torcedor — Plano de "
     "Implementação”, com metas, operação, papéis, calendário e indicadores; e o "
     "material de divulgação, voltado ao público."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "11.3 Os dois eventos-âncora")
tabela(doc, ["Evento", "Quando (previsão)", "Função"], [
    ["Arraial de Lançamento", "Começo da temporada — pode ser em março",
     "Abre oficialmente a temporada: revela tema, itens e camisa, faz a prestação de "
     "contas do ano anterior, vende camisa, realiza sorteios e promoções e capta "
     "sócios torcedores"],
    ["Arraial da Explosão", "Depois do Festival — agosto ou mais para o fim do ano",
     "Mantém a temporada junina viva o ano todo: reúne danças de Beruri e de fora, "
     "competição com votação popular em tempo real, feira com comerciantes "
     "berurienses e premiação na hora"],
], larguras=[4.0, 4.5, 7.5])
p(doc, "Cada um desses eventos tem documento próprio, com programação, estrutura, "
       "equipes, receitas, cronograma de produção e checklist.")
caixa(doc, "O Arraial da Explosão ainda é um projeto",
      "Ele nunca aconteceu: não há edição anterior, data marcada nem orçamento "
      "aprovado. O documento dele é a proposta de criação, a ser levada à Diretoria. "
      "Dois pontos definem se ele sai do papel: a parceria com a Prefeitura — "
      "pedido formal de recursos, limpeza, segurança, estrutura e apoio às danças "
      "convidadas — e a feira, com edital de cadastro das bancas e cobrança de uma "
      "taxa de 5% a 10% sobre a venda ou de um valor fixo pelo espaço.", VERMELHO)

h2(doc, "11.4 Parcerias comerciais reposicionadas")
p(doc, "As parcerias com o comércio local continuam, mas com outra função. Em vez de "
       "serem apenas cotas de patrocínio, passam a sustentar o Programa Sócio Torcedor "
       "e a gerar ações para o público geral.")
for rot, txt in [
    ("Sustentar o sócio: ", "o parceiro oferece desconto, brinde ou prêmio ao sócio "
     "torcedor; a quadrilha divulga o parceiro e leva clientes até ele."),
    ("Prêmios de sorteio: ", "boa parte dos prêmios dos sorteios do programa vem de "
     "parceiros, com custo baixo para a quadrilha."),
    ("Ações para o público geral: ", "promoções conjuntas, combos, presença nos eventos "
     "e campanhas que beneficiam qualquer pessoa, não só os sócios."),
    ("Produção de beleza: ", "parceria com maquiadores e cabeleireiros para as grandes "
     "apresentações, em pacote de grupo com desconto."),
    ("Onde está detalhado: ", "documento “Kit Parceiro”, com cotas, contrapartidas e "
     "ações promocionais conjuntas."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "11.5 Projetos pontuais (em stand by)")
p(doc, "Rifa, bingo, venda de comidas, cinema na praça e Cine Explosão deixam de ser "
       "rotina e passam a ser reserva: ficam prontos, documentados e são acionados "
       "quando houver urgência, meta específica ou boa oportunidade. Não se faz mais "
       "arrecadação por hábito, competindo com o tempo de ensaio.")
tabela(doc, ["Quando acionar", "Exemplo"], [
    ["Urgência de caixa", "Despesa não prevista de alegoria, som ou transporte"],
    ["Meta específica", "Custear a viagem de uma apresentação fora de Beruri"],
    ["Oportunidade", "Data com público garantido na cidade"],
    ["Reforço pré-Festival", "Fechar a conta da montagem final do espetáculo"],
], larguras=[5.0, 11.0])
p(doc, "O acionamento é decidido pela Diretoria, com responsável designado, reunião "
       "de planejamento antes e balanço publicado depois. Detalhes no documento "
       "“Projetos de Arrecadação”.")

h2(doc, "11.6 Regras de ouro do dinheiro")
for txt in [
    "Todo gasto registrado. Sem nota, sem recibo, sem lançamento: não existiu.",
    "Todo projeto fecha com mini-balanço publicado.",
    "Todos participam: quem dança também vende, monta, carrega e limpa.",
    "Reunião antes, balanço depois — nenhum projeto começa ou termina sem isso.",
    "Registrar o aprendizado: o que funcionou e o que não funcionou fica documentado "
    "para os anos seguintes.",
]:
    bullet(doc, txt)

# ---------------------------------------------------------- 12. linha do tempo
doc.add_page_break()
h1(doc, "LINHA DO TEMPO DA TEMPORADA", 12)
p(doc, "O quadro abaixo é uma previsão de trabalho, não um calendário fechado. As "
       "datas exatas de cada marco são definidas pela Diretoria ao longo do caminho — "
       "o que importa aqui é a ordem e a antecedência.")
tabela(doc, ["Período previsto", "O que acontece", "Quem conduz"], [
    ["Agosto de 2026",
     "Reunião geral com a coordenação: apresentação deste plano, balanço da temporada "
     "anterior, definição da Diretoria e dos responsáveis por cada grupo do organograma.",
     "Diretoria"],
    ["Setembro de 2026",
     "Formalização do organograma; abertura do Programa Sócio Torcedor; levantamento "
     "de recursos e de calendário; primeiras propostas de tema.",
     "Diretoria + Comissão de Artes"],
    ["Outubro de 2026",
     "Escolha do tema com filtro de viabilidade; início do documento do tema (sinopse e "
     "atos); primeira previsão de orçamento da temporada.",
     "Comissão de Artes"],
    ["Novembro e dezembro de 2026",
     "Roteiro fechado; conceito de figurino e de alegoria; plano de arena; captação de "
     "parceiros; produção de conteúdo de bastidor.",
     "Comissão + Grupos de Produção"],
    ["Janeiro de 2027",
     "Redesenho da identidade visual (marca da quadrilha e marca do tema) já em cima do "
     "tema definido; arte da camisa; calendário editorial; início da confecção; "
     "convocação dos brincantes.",
     "Comunicação + Figurino"],
    ["Fevereiro de 2027",
     "Assinatura do Termo de Compromisso com os brincantes; início dos ensaios; sistema "
     "de avaliação ligado; começa o período de ativação da bonificação.",
     "Diretoria + Coreografia"],
    ["Março de 2027 (previsão)",
     "Arraial de Lançamento: revelação de tema, itens e camisa, prestação de contas do "
     "ano anterior, venda, sorteios e captação de sócios.",
     "Diretoria + Eventos"],
    ["Abril a junho de 2027",
     "Ensaios regulares, disputas mensais entre filas, apresentações e prévias, "
     "construção de alegoria e figurino, ensaiões e ensaio na arena.",
     "Grupos de Produção"],
    ["Julho de 2027",
     "Festival Folclórico de Beruri: montagem, espetáculo, desmontagem e cobertura "
     "completa.",
     "Equipes de Arena"],
    ["Agosto de 2027 em diante",
     "Balanço da temporada, pagamento da bonificação, Arraial da Explosão e abertura do "
     "planejamento de 2028.",
     "Diretoria"],
], larguras=[3.6, 8.4, 4.0])

# ------------------------------------------------------------- 13. indicadores
h1(doc, "COMO VAMOS MEDIR", 13)
p(doc, "Reestruturação sem medida vira discurso. Estes são os indicadores que a "
       "Diretoria acompanha ao longo da temporada.")
tabela(doc, ["Indicador", "Por que importa", "Onde é medido"], [
    ["Frequência média dos brincantes", "Mede compromisso e prevê o resultado na arena",
     "Sistema de Avaliação"],
    ["Nota média por fila", "Mostra a evolução técnica e onde reforçar o trabalho",
     "Sistema de Avaliação"],
    ["Brincantes ativos ao fim da temporada", "Mede retenção: quantos começaram e quantos "
     "chegaram ao Festival", "Sistema de Avaliação"],
    ["Número de sócios torcedores", "Principal receita recorrente da quadrilha",
     "Site do Sócio Torcedor"],
    ["Receita recorrente mensal", "Previsibilidade de caixa", "Site do Sócio Torcedor"],
    ["Parceiros ativos e contrapartidas cumpridas", "Sustenta o programa e a credibilidade",
     "Controle da Comunicação"],
    ["Execução do orçamento por grupo", "Mostra se o planejamento financeiro é realista",
     "Controle do Financeiro"],
    ["Alcance e engajamento nas redes", "Mede se o trabalho está sendo visto",
     "Relatório mensal da Comunicação"],
    ["Prazo do tema", "Tema fechado no ano anterior é o principal indicador de que a "
     "reestruturação pegou", "Ata da Comissão de Artes"],
], larguras=[5.0, 7.0, 4.0])

# ------------------------------------------------------------------ 14. riscos
h1(doc, "RISCOS E COMO REDUZIR", 14)
tabela(doc, ["Risco", "Como reduzir"], [
    ["Tema atrasar de novo",
     "Prazo de escolha ainda em 2026, registrado em ata, com responsável pelo documento "
     "do tema"],
    ["Sobrecarga de poucas pessoas",
     "Organograma com responsáveis por grupo, liderança rotativa de fila e delegação "
     "formal"],
    ["Dependência de recurso público",
     "Sócio Torcedor como receita própria recorrente e portfólio de projetos pronto para "
     "acionar"],
    ["Desistência de brincantes ao longo do ano",
     "Contrato, bonificação, perfil com metas claras, reconhecimento público e ambiente "
     "organizado"],
    ["Conflito interno entre grupos",
     "Fluxo de decisão definido, ata de reunião e Presidente como instância final"],
    ["Promessa não cumprida com sócio ou parceiro",
     "Lista de contrapartidas com responsável e prazo, conferida mensalmente"],
    ["Chuva, logística ou falha técnica no dia",
     "Plano B por efeito e por evento, ensaio de montagem e escala de arena treinada"],
], larguras=[6.0, 10.0])

# ------------------------------------------------------------------ 15. futuro
h1(doc, "VISÃO DE FUTURO", 15)
p(doc, "Este plano não termina em 2027. A estrutura montada agora é o que permite "
       "repetir, melhorar e crescer nos anos seguintes:")
for txt in [
    "ser a quadrilha mais organizada e transparente de Beruri — e provar isso com "
    "documento, dado e prestação de contas;",
    "consolidar uma marca reconhecida além do município, abrindo portas para festivais "
    "regionais;",
    "profissionalizar a gestão a ponto de atrair apoio institucional permanente;",
    "fazer do Arraial da Explosão uma festa tradicional do calendário de Beruri;",
    "ampliar o Programa de Bonificação à medida que a arrecadação própria crescer;",
    "criar um modelo que possa ser replicado por outros grupos culturais da cidade, "
    "fortalecendo o Festival como um todo.",
]:
    bullet(doc, txt)

citacao(doc, "Quem ganhou o primeiro tem a obrigação de ser o melhor sempre.")
p(doc, "Explosão Junina de Beruri · Temporada 2027", centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Projeto Explosao Junina Beruri.docx")
