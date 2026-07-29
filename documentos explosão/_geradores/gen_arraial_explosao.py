# -*- coding: utf-8 -*-
"""Gera 'Arraial da Explosao - Plano do Evento.docx'."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["ARRAIAL", "DA EXPLOSÃO"],
    "Projeto do evento · Temporada 2027",
    "A festa que mantém a temporada junina viva o ano todo em Beruri.",
    nota="PROJETO — o Arraial da Explosão ainda não existe. Este documento é a "
         "proposta de criação: por que fazer, como fazer e o que é preciso para "
         "que a primeira edição aconteça. Previsão: depois do Festival — agosto "
         "ou mais para o fim do ano. Sem data fechada.",
    rodape="Beruri – Amazonas",
    cor=VERMELHO,
)

# ------------------------------------------------------------ por que fazer --
h1(doc, "POR QUE VAMOS FAZER", 1)
caixa(doc, "Leia antes de tudo: isto é um projeto, não um relatório",
      "O Arraial da Explosão nunca aconteceu. Não existe edição anterior, não há "
      "data marcada e não há orçamento aprovado. O que existe é a decisão de "
      "criá-lo. Tudo o que vem a seguir — programação, competição, feira, "
      "estrutura, cronograma — é proposta a ser levada à Diretoria, discutida e "
      "ajustada. O documento serve exatamente para isso: transformar a ideia em "
      "algo que dá para aprovar, orçar e executar.", VERMELHO)

p(doc, "A pergunta que este projeto responde não é “como organizar mais uma festa”. "
       "É por que a Explosão Junina precisa ter uma festa própria — e por que "
       "precisa ter agora, junto com a reestruturação da quadrilha para 2027.")

h2(doc, "1.1 O problema: a temporada junina morre cedo em Beruri")
p(doc, "A temporada junina da cidade cabe em poucas semanas. Passado o Festival "
       "Folclórico, tudo para: os grupos se dispersam, o público esquece, os ensaios "
       "acabam, as redes silenciam e o assunto só volta no ano seguinte. Para quem "
       "vê de fora, a quadrilha existe um mês por ano.")
p(doc, "Isso tem um custo real, e não é só simbólico. Quadrilha que só aparece em "
       "julho não consegue patrocínio (o comércio não vê retorno), não consegue "
       "sócio torcedor (ninguém apoia o ano inteiro algo que só existe uma noite), "
       "não segura brincante (sete meses sem nada acontecendo é tempo de sobra para "
       "perder gente) e não constrói memória na cidade.")

h2(doc, "1.2 A ideia central: estar sempre em movimento")
citacao(doc, "A Explosão não é uma noite de julho. É um grupo que trabalha o ano inteiro.")
p(doc, "O Arraial da Explosão é a peça mais visível de uma virada maior: a Explosão "
       "passa a ocupar o calendário da cidade o ano todo. Junto com o Arraial de "
       "Lançamento, o Programa Sócio Torcedor, os projetos de arrecadação e a nova "
       "estrutura de diretoria e grupos de produção, ele existe para passar uma "
       "mensagem que hoje a cidade não recebe:")
for rot, txt in [
    ("Estamos sempre ativos: ", "sempre há algo acontecendo — ensaio, evento, ação, "
     "notícia. A quadrilha não hiberna entre um Festival e outro."),
    ("Estamos sempre inovando: ", "votação popular pelo celular, sistema próprio de "
     "avaliação, sócio torcedor com painel e troféus, prestação de contas pública. "
     "Nada disso existe na região."),
    ("Estamos movimentando a quadrilha em Beruri: ", "a Explosão não puxa só para si. "
     "Ela dá palco, troféu e certificado às outras danças, aproxima municípios "
     "vizinhos e faz o cenário junino da cidade crescer junto."),
    ("Estamos construindo tradição: ", "um evento que se repete todo ano vira parte do "
     "calendário. É assim que o Festival virou o que é — e é isso que o Arraial "
     "persegue."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "1.3 O que a Explosão ganha com isso")
tabela(doc, ["Frente", "O que o Arraial destrava"], [
    ["Patrocínio e parceria",
     "Comerciante patrocina quem aparece. Com dois eventos próprios por ano, a "
     "quadrilha passa a ter contrapartida real para oferecer — e não só um pedido"],
    ["Sócio Torcedor",
     "O programa cobra o ano inteiro; precisa de entrega o ano inteiro. O Arraial é "
     "um dos momentos em que o sócio vê para onde foi o apoio dele — e um posto de "
     "adesão com público na frente"],
    ["Poder público",
     "Evento cultural aberto, com danças convidadas e comércio local, é pauta que a "
     "Prefeitura tem interesse em apoiar. Isso abre a porta do custeio público"],
    ["Brincantes",
     "Mais um palco na temporada, mais um motivo para continuar, e uma atividade "
     "coletiva que não é ensaio"],
    ["Imagem da quadrilha",
     "A Explosão deixa de ser “a quadrilha que ganhou em 2025” e passa a ser “a "
     "quadrilha que organiza as coisas na cidade”"],
    ["Caixa",
     "Receita própria fora da temporada, quando o dinheiro costuma faltar"],
], larguras=[4.0, 12.0])

caixa(doc, "A ambição",
      "O Arraial da Explosão não é um evento de arrecadação com dança. É uma festa "
      "cultural que também arrecada. A meta é que, em poucos anos, ele seja "
      "reconhecido como uma tradição de Beruri — algo que a cidade espera acontecer, "
      "como espera o Festival.", VERMELHO)

h2(doc, "1.4 Objetivos")
for rot, txt in [
    ("Manter a temporada viva: ", "dar à cidade um segundo grande momento junino, depois "
     "do Festival."),
    ("Firmar tradição: ", "construir um evento anual associado ao nome da Explosão."),
    ("Valorizar as danças locais: ", "dar palco, troféu e certificado a todos os grupos "
     "culturais do município."),
    ("Aproximar municípios vizinhos: ", "criar intercâmbio com danças de fora e ampliar "
     "a rede da Explosão."),
    ("Movimentar o comércio: ", "convidar comerciantes berurienses a vender no espaço do "
     "evento."),
    ("Arrecadar: ", "gerar receita própria para a quadrilha, sem que esse seja o único "
     "propósito."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "1.5 Quando acontece")
p(doc, "A previsão é realizar o Arraial depois do Festival: em agosto, aproveitando "
       "o clima junino ainda recente, ou mais para o fim do ano, se isso permitir uma "
       "produção melhor e um público maior. A escolha é da Diretoria, considerando "
       "chuva, calendário da cidade, disponibilidade de espaço e caixa disponível.")

h2(doc, "1.6 O que precisa ser decidido para o projeto sair do papel")
tabela(doc, ["Decisão", "Quem decide", "Sem isso"], [
    ["Data e local da primeira edição", "Diretoria",
     "Nada mais pode ser planejado — todo o cronograma conta a partir da data"],
    ["Parceria com a Prefeitura e o que ela cobre", "Presidência + Diretoria de Eventos",
     "O orçamento fica todo no caixa da quadrilha"],
    ["Condição das bancas (taxa de 5% a 10% ou valor fixo)", "Diretoria + Financeiro",
     "Não dá para abrir o edital de cadastro dos comerciantes"],
    ["Se as danças de fora competem, competem à parte ou vêm fora de competição",
     "Diretoria", "Não dá para fechar as categorias nem os troféus"],
    ["Orçamento aprovado", "Diretor Financeiro",
     "A quadrilha entra no evento sem saber quanto pode gastar"],
], larguras=[6.0, 4.5, 5.5])

# ------------------------------------------------------------- programação --
doc.add_page_break()
h1(doc, "FORMATO E PROGRAMAÇÃO", 2)
tabela(doc, ["Momento", "O que acontece"], [
    ["Abertura da feira",
     "Espaços de venda abertos ao público: comerciantes locais, bancas das danças "
     "convidadas e banca da Explosão"],
    ["Abertura oficial",
     "Boas-vindas da Presidência, apresentação dos grupos participantes, explicação das "
     "regras da votação popular e agradecimento aos parceiros"],
    ["Apresentações das danças",
     "Cada grupo convidado se apresenta na ordem sorteada. Entre uma apresentação e "
     "outra, a votação daquele grupo é aberta ao público"],
    ["Votação popular",
     "O público vota em tempo real pelo celular. O painel de votos pode ser exibido "
     "durante a festa"],
    ["Intervalo animado",
     "Atração musical, sorteios entre o público e sorteio exclusivo dos sócios torcedores"],
    ["Apuração e premiação",
     "Resultado divulgado na hora, com os grupos chamados ao palco para receber troféu, "
     "certificado e prêmios"],
    ["Encerramento com a Explosão",
     "A quadrilha anfitriã se apresenta por último, fechando a noite como atração "
     "principal"],
], larguras=[4.5, 11.5])

h1(doc, "COMPETIÇÃO E VOTAÇÃO POPULAR", 3)
p(doc, "A competição é o coração do Arraial. Ela não é uma disputa técnica com "
       "jurados — é festa: quem decide é o público, na hora, pelo celular.")

h2(doc, "3.1 Quem compete")
tabela(doc, ["Categoria", "Quem participa", "Observação"], [
    ["Danças de Beruri", "Grupos culturais e danças do município",
     "Concorrem ao prêmio principal por votação popular"],
    ["Danças convidadas de fora", "Grupos de municípios vizinhos",
     "Participam em categoria própria ou fora de competição, conforme decisão da "
     "Diretoria a cada edição"],
    ["Explosão Junina", "A quadrilha anfitriã",
     "Se apresenta no encerramento, fora de competição"],
], larguras=[4.0, 5.0, 7.0])

h2(doc, "3.2 Como funciona a votação")
for rot, txt in [
    ("Pelo celular: ", "o público acessa a votação por QR code espalhado no espaço do "
     "evento — sem instalar aplicativo."),
    ("Por apresentação: ", "a votação de cada grupo abre logo depois da apresentação dele "
     "e fecha em um tempo definido."),
    ("Um voto por pessoa: ", "controle simples por dispositivo, com registro de horário, "
     "suficiente para uma festa de cidade pequena."),
    ("Resultado ao vivo: ", "a apuração é automática. O painel pode ser projetado no "
     "telão durante a festa, criando expectativa."),
    ("Divulgação na hora: ", "o resultado é anunciado no mesmo dia, com os vencedores "
     "chamados ao palco imediatamente."),
    ("Registro público: ", "os números finais são publicados nas redes depois do evento — "
     "transparência também vale para a votação."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "3.3 Prêmios")
tabela(doc, ["Prêmio", "Quem recebe", "Como é definido"], [
    ["Certificado de participação", "Todos os grupos que se apresentarem", "Automático"],
    ["Troféu de participação", "Todos os grupos que se apresentarem", "Automático"],
    ["Prêmio principal do Arraial", "Melhor apresentação da noite", "Votação popular"],
    ["Melhor marcador(a)", "Destaque individual", "Votação popular"],
    ["Melhor casal de noivos", "Destaque individual", "Votação popular"],
    ["Grupo mais animado", "Destaque coletivo", "Votação popular"],
    ["Melhor figurino", "Destaque coletivo", "Votação popular"],
    ["Torcida mais animada", "Público do grupo", "Aclamação / votação"],
], larguras=[5.0, 5.5, 5.5])
caixa(doc, "Ninguém sai de mãos vazias",
      "Todo grupo que se apresentar recebe troféu e certificado. Os prêmios da votação "
      "são simbólicos e servem para animar a noite, não para criar rivalidade. O "
      "Arraial precisa ser lembrado como a festa em que todo mundo foi valorizado.",
      VERDE)

# ---------------------------------------------------------------- feira -----
doc.add_page_break()
h1(doc, "FEIRA E COMÉRCIO LOCAL", 4)
p(doc, "A feira é a segunda perna do Arraial. Ela transforma um evento de dança numa "
       "noite de movimento para a cidade: o comerciante vende, o público fica mais "
       "tempo, a quadrilha arrecada e o vínculo criado ali vira patrocínio na "
       "temporada seguinte. É também o argumento mais forte na conversa com o poder "
       "público — não é um pedido para uma festa, é um espaço de renda para "
       "comerciantes berurienses.")

h2(doc, "4.1 Parceria com a Prefeitura")
p(doc, "O ideal é que o Arraial seja realizado em parceria com a Prefeitura de "
       "Beruri, com solicitação formal de recursos e apoio. A quadrilha entra com a "
       "produção, o público e o conteúdo cultural; o poder público entra com o que "
       "encarece um evento aberto e que a quadrilha não tem como bancar sozinha.")
tabela(doc, ["O que se pede à Prefeitura", "Por que faz diferença"], [
    ["Limpeza do espaço (antes, durante e depois)",
     "É a maior despesa invisível de qualquer evento aberto, e a que mais gera "
     "reclamação se falhar"],
    ["Segurança e apoio da guarda / polícia",
     "Festa noturna com bebida e público grande exige presença oficial. Sem isso, a "
     "quadrilha assume um risco que não deve assumir"],
    ["Organização e cessão do espaço",
     "Praça, quadra ou área pública liberada, com autorização formal e demarcação"],
    ["Estrutura: palco, tendas, som, iluminação e energia",
     "É o maior item de custo do evento. Estrutura cedida muda o orçamento inteiro"],
    ["Transporte das danças convidadas",
     "Sem transporte, grupo de município vizinho não vem — e a competição perde sentido"],
    ["Hospedagem e alimentação das danças de fora",
     "Um grupo que viaja precisa de onde ficar e o que comer. É o que viabiliza o "
     "intercâmbio entre municípios"],
    ["Divulgação nos canais oficiais do município",
     "Amplia o alcance muito além das redes da quadrilha"],
], larguras=[6.5, 9.5])
caixa(doc, "Como pedir",
      "O pedido é feito por ofício, assinado pela Presidência e registrado pelo "
      "Diretor Secretário, acompanhado deste projeto. Deve deixar claro o que a "
      "cidade ganha: evento cultural gratuito, palco para as danças do município, "
      "espaço de renda para o comércio local e prestação de contas pública ao final. "
      "Quanto antes for protocolado, maior a chance de entrar no planejamento e no "
      "orçamento da Prefeitura.", AZUL)

h2(doc, "4.2 Condição das bancas: taxa de 5% a 10% ou valor fixo")
p(doc, "Num primeiro momento, a proposta é cobrar do comerciante uma taxa de 5% a "
       "10% sobre a venda, ou um valor fixo pelo espaço — o que for mais simples de "
       "controlar. A cobrança vale tanto para quem monta a própria barraca quanto "
       "para quem ocupa espaço dentro da tenda da quadrilha.")
tabela(doc, ["Modelo", "Como funciona", "Quando usar"], [
    ["Taxa de 5% a 10%", "Percentual sobre o que a banca vendeu na noite, acertado ao "
     "final do evento", "Quando o comerciante não quer arriscar valor fixo — o custo "
     "dele acompanha a venda"],
    ["Valor fixo pelo espaço", "Valor único pago na confirmação da vaga, definido por "
     "tamanho e localização da banca", "Quando se quer previsibilidade de caixa e "
     "menos controle no dia"],
], larguras=[4.0, 6.0, 6.0])
for rot, txt in [
    ("A escolha do modelo é da Diretoria: ", "o percentual exato e o valor fixo saem "
     "da reunião, junto com o orçamento do evento."),
    ("O valor precisa caber no comerciante: ", "a taxa existe para custear o evento, "
     "não para tirar o lucro de quem vende. Cobrança alta demais esvazia a feira e "
     "acaba com a parceria antes de ela existir."),
    ("Transparência dos dois lados: ", "a condição é a mesma para todo mundo, "
     "divulgada no edital, e o total arrecadado com as bancas entra no balanço "
     "público do evento."),
    ("Danças convidadas não pagam: ", "o espaço de venda dos grupos convidados "
     "continua gratuito — é parte do convite."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "4.3 Edital e formulário de cadastro das bancas")
p(doc, "As vagas não são distribuídas no boca a boca. A quadrilha divulga um edital "
       "com formulário de cadastro, aberto a qualquer comerciante de Beruri que "
       "queira vender no Arraial. Isso resolve três problemas de uma vez: dá "
       "igualdade de acesso, permite planejar o espaço com antecedência e produz a "
       "lista do que vai ter na festa — que vira material de divulgação.")
tabela(doc, ["Etapa", "O que acontece"], [
    ["Publicação do edital",
     "Regras divulgadas nas redes, na rádio e no comércio: quem pode participar, o "
     "que pode vender, a condição de pagamento, o prazo de inscrição e o dia da "
     "confirmação"],
    ["Formulário de cadastro",
     "O comerciante se inscreve informando nome e contato, o que vai vender, tamanho "
     "aproximado da banca, se traz estrutura própria ou precisa de espaço na tenda, e "
     "necessidade de energia elétrica"],
    ["Análise e seleção",
     "A coordenação confere as inscrições, evita repetição excessiva do mesmo produto "
     "e distribui as vagas conforme o espaço disponível"],
    ["Confirmação e pagamento",
     "A vaga é confirmada e a condição é acertada por escrito (taxa percentual ou "
     "valor fixo). Sem confirmação, não há espaço reservado"],
    ["Mapa e demarcação",
     "Cada banca recebe um lugar marcado no mapa do evento, com numeração. A "
     "demarcação física é feita antes do dia, para ninguém disputar espaço na hora"],
    ["Banner de divulgação",
     "Com a lista fechada, a quadrilha produz o banner e as artes anunciando o que vai "
     "ter na feira — comidas, bebidas, artesanato e serviços, com o nome de cada "
     "banca. É divulgação para o evento e para o comerciante ao mesmo tempo"],
    ["Acerto no fim da noite",
     "No modelo de percentual, a banca acerta com o Financeiro ao encerrar; no valor "
     "fixo, já está pago. Tudo registrado para o balanço"],
], larguras=[4.0, 12.0])
caixa(doc, "O banner é o que faz a feira valer a pena para o comerciante",
      "Divulgar o nome de cada banca antes do evento é o que transforma a taxa em "
      "investimento: o comerciante paga pelo espaço e recebe divulgação para a cidade "
      "inteira. É esse detalhe que faz o mesmo comerciante voltar na próxima edição — "
      "e, com o tempo, virar patrocinador do Kit Parceiro.", VERDE)

h2(doc, "4.4 Mapa dos espaços")
tabela(doc, ["Espaço", "Quem ocupa", "Condição"], [
    ["Bancas de comerciantes", "Vendedores berurienses de comidas típicas, artesanato, "
     "bebidas e produtos", "Inscrição pelo edital, vaga confirmada e lugar demarcado. "
     "Taxa de 5% a 10% sobre a venda ou valor fixo pelo espaço"],
    ["Espaço na tenda da quadrilha", "Comerciante sem estrutura própria",
     "Mesma condição das bancas — o que se cobra aqui é o espaço coberto e a "
     "estrutura cedida"],
    ["Bancas das danças convidadas", "Cada grupo pode vender seus produtos (camisas, "
     "comidas, bebidas)", "Gratuito — é incentivo para participar"],
    ["Banca da Explosão", "A própria quadrilha", "Comidas, doces, bebidas e produtos "
     "oficiais; principal fonte de receita direta"],
    ["Espaço de parceiros", "Patrocinadores do Kit Parceiro", "Conforme a cota "
     "contratada"],
    ["Posto do Sócio Torcedor", "Coordenação do programa", "Adesão na hora, com QR code "
     "e meta do dia"],
], larguras=[4.0, 5.5, 6.5])

h1(doc, "RECEITAS E DESPESAS", 5)
tabela(doc, ["Receitas previstas", "Despesas previstas"], [
    ["Banca da Explosão (comidas, doces e bebidas)", "Estrutura: som, iluminação e palco"],
    ["Taxa das bancas (5% a 10% da venda ou valor fixo)", "Troféus e certificados"],
    ["Venda de produtos oficiais e camisas", "Prêmios da votação popular"],
    ["Cotas de patrocínio específicas do evento", "Transporte e apoio às danças convidadas"],
    ["Recursos da parceria com a Prefeitura", "Hospedagem e alimentação das danças de fora"],
    ["Novas adesões ao Sócio Torcedor", "Divulgação, banner e material gráfico"],
    ["Rifa ou bingo dentro do evento (opcional)", "Ingredientes e insumos das bancas"],
    ["", "Limpeza, segurança e organização do espaço"],
], larguras=[8.0, 8.0])
p(doc, "Boa parte das despesas da coluna da direita é exatamente o que se pede à "
       "Prefeitura na parceria (§4.1). Quanto mais dela for coberta, mais o resultado "
       "do evento fica com a quadrilha — e menor o risco de prejuízo na primeira "
       "edição, que é a mais incerta de todas.")
p(doc, "Como todo projeto da quadrilha, o Arraial fecha com mini-balanço: receitas, "
       "custos e resultado, entregues ao Diretor Financeiro e publicados nas redes.")

h1(doc, "ESTRUTURA NECESSÁRIA", 6)
tabela(doc, ["Item", "Como conseguir"], [
    ["Espaço (praça, quadra ou área ampla)", "Parceria com a Prefeitura (cessão formal) "
     "ou parceria com escola / centro comunitário"],
    ["Palco ou área de apresentação demarcada", "Parceria com a Prefeitura, estrutura "
     "própria, empréstimo ou aluguel"],
    ["Tendas e cobertura para a feira", "Parceria com a Prefeitura ou aluguel; parte "
     "das bancas traz estrutura própria"],
    ["Som e microfone", "Equipamento da quadrilha, empréstimo ou aluguel"],
    ["Iluminação e energia", "Apoio da Prefeitura ou gerador / parceiro"],
    ["Decoração junina", "Produção interna: bandeirinhas, fogueira cenográfica, "
     "totens do tema"],
    ["Mesas, cadeiras e barracas", "Empréstimo, aluguel ou responsabilidade dos "
     "próprios vendedores"],
    ["Telão ou TV para o painel de votação", "Empréstimo de parceiro ou escola"],
    ["Internet para a votação", "Roteador com chip de dados ou apoio de parceiro; "
     "prever plano B offline"],
    ["Troféus e certificados", "Produção com fornecedor local; certificados impressos "
     "pela própria quadrilha"],
    ["Limpeza, segurança e organização", "Parceria com a Prefeitura; equipe própria "
     "como retaguarda"],
], larguras=[6.0, 10.0])

h1(doc, "EQUIPES DO EVENTO", 7)
tabela(doc, ["Equipe", "Função no dia"], [
    ["Coordenação geral", "Comanda o evento, resolve imprevistos e mantém o horário"],
    ["Palco e apresentação", "Locução, ordem das apresentações e chamada dos grupos"],
    ["Som e técnica", "Áudio, microfones, playback e telão"],
    ["Votação", "Orienta o público, distribui QR code e acompanha a apuração"],
    ["Bancas e vendas", "Preparo, venda e controle de caixa da banca da Explosão"],
    ["Feira", "Recebe os comerciantes, confere o mapa das bancas, orienta a montagem e "
     "faz o acerto da taxa ao final"],
    ["Recepção das danças", "Recebe, acomoda e orienta os grupos convidados"],
    ["Comunicação", "Fotos, vídeos, stories ao vivo e cobertura completa"],
    ["Sócio Torcedor", "Posto de adesão, sorteio dos sócios e atendimento"],
    ["Limpeza e organização", "Antes, durante e depois — o espaço é devolvido em ordem"],
], larguras=[4.5, 11.5])

# --------------------------------------------------------------- cronograma --
doc.add_page_break()
h1(doc, "CRONOGRAMA DE PRODUÇÃO", 8)
p(doc, "Contagem regressiva a partir da data escolhida. Os prazos são referências de "
       "produção, não datas de calendário.")
tabela(doc, ["Prazo", "O que fazer"], [
    ["D-90", "Protocolar o ofício de parceria na Prefeitura, com este projeto anexado, "
     "pedindo recursos, estrutura, limpeza, segurança e apoio às danças convidadas"],
    ["D-60", "Definir data e local; formar a equipe de produção; abrir os convites às "
     "danças de Beruri e das cidades vizinhas; definir a condição das bancas (taxa "
     "percentual ou valor fixo)"],
    ["D-45", "Confirmar espaço e estrutura; publicar o edital da feira e abrir o "
     "formulário de cadastro das bancas; iniciar a captação de patrocínio específico "
     "do evento"],
    ["D-30", "Fechar a lista de grupos participantes; encerrar as inscrições da feira e "
     "selecionar as bancas; definir prêmios e categorias; encomendar troféus e "
     "certificados; abrir a divulgação"],
    ["D-20", "Definir a programação completa e a ordem das apresentações; preparar o "
     "sistema de votação; confirmar as bancas, acertar a condição por escrito e montar "
     "o mapa dos espaços"],
    ["D-15", "Divulgação pesada: artes com a programação, os grupos confirmados e o "
     "banner da feira com o nome de cada banca; convite às autoridades e à imprensa"],
    ["D-7", "Reunião final da equipe; escala por função; compra de insumos das bancas; "
     "teste do sistema de votação; envio do mapa e das orientações aos comerciantes"],
    ["D-2", "Montagem da estrutura; demarcação física dos espaços das bancas; "
     "decoração; teste de som, iluminação e telão"],
    ["D-1", "Ensaio de operação: passagem de som, simulação da votação e conferência do "
     "material de premiação"],
    ["Dia", "Realizar o evento conforme a programação; registrar tudo"],
    ["D+2", "Agradecimentos públicos, divulgação dos resultados e das fotos"],
    ["D+7", "Mini-balanço financeiro publicado e reunião de aprendizados"],
], larguras=[2.5, 13.5])

h1(doc, "O QUE O SISTEMA VAI FAZER", 9)
p(doc, "A votação popular em tempo real é uma construção da Diretoria de Tecnologia. "
       "É o que diferencia o Arraial de qualquer outra festa da região: resultado na "
       "hora, sem urna, sem contagem manual e sem discussão.")
tabela(doc, ["Recurso", "Como funciona"], [
    ["Cadastro dos grupos", "A coordenação cadastra as danças participantes, a ordem de "
     "apresentação e as categorias de prêmio"],
    ["Votação por QR code", "O público lê o código, escolhe o grupo e vota pelo próprio "
     "celular, sem instalar nada"],
    ["Janela de votação", "A coordenação abre e fecha a votação de cada grupo ou de cada "
     "categoria pelo painel"],
    ["Controle de voto", "Um voto por dispositivo em cada categoria, com registro de "
     "horário"],
    ["Painel ao vivo", "Tela de apuração para projetar no telão, com os números "
     "atualizando durante a festa"],
    ["Resultado na hora", "Ao fechar a votação, o sistema aponta os vencedores de cada "
     "categoria para o anúncio imediato"],
    ["Registro final", "Relatório com todos os votos por categoria, para publicação"],
    ["Certificados", "Geração dos certificados de participação de cada grupo"],
    ["Cadastro das bancas", "Formulário de inscrição do edital da feira: o comerciante "
     "se inscreve pelo celular e a coordenação acompanha a lista, seleciona, confirma e "
     "monta o mapa dos espaços"],
    ["Acerto da feira", "Registro da condição de cada banca (percentual ou valor fixo) e "
     "do que foi acertado no fim da noite, alimentando o balanço do evento"],
], larguras=[4.5, 11.5])
caixa(doc, "Plano B obrigatório",
      "Internet em evento ao ar livre falha. O sistema precisa funcionar com rede "
      "local (sem depender da internet) ou ter cédula impressa como alternativa. Isso "
      "é testado no D-1, nunca no dia.", AMBAR)

# ---------------------------------------------------------------- checklist --
doc.add_page_break()
checklist(doc, [
    "Definir data e local do Arraial",
    "Protocolar o ofício de parceria e pedido de recursos na Prefeitura",
    "Formar a equipe de produção e distribuir funções",
    "Convidar as danças de Beruri e das cidades vizinhas",
    "Confirmar os grupos participantes e sortear a ordem de apresentação",
    "Definir as categorias de premiação",
    "Produzir troféus e certificados de participação",
    "Preparar e testar o sistema de votação popular",
    "Definir a condição das bancas (taxa de 5% a 10% ou valor fixo)",
    "Publicar o edital da feira e abrir o formulário de cadastro das bancas",
    "Selecionar e confirmar as bancas inscritas",
    "Montar o mapa dos espaços e demarcar o lugar de cada banca",
    "Produzir o banner de divulgação com o que vai ter na feira",
    "Montar a banca de comidas e bebidas da Explosão",
    "Captar patrocínio específico do evento",
    "Definir estrutura: som, iluminação, palco, telão e energia",
    "Criar artes de divulgação com a programação completa",
    "Divulgar nas redes, na rádio e boca a boca",
    "Montar o posto de adesão do Sócio Torcedor",
    "Organizar sorteios (público geral e sócios)",
    "Realizar o evento",
    "Apurar a votação e premiar na hora",
    "Publicar resultados, fotos e balanço",
    "Reunião de aprendizados para a próxima edição",
], titulo="CHECKLIST DE EXECUÇÃO")

h1(doc, "RISCOS E COMO REDUZIR", 10)
tabela(doc, ["Risco", "Como reduzir"], [
    ["Chuva", "Definir local coberto ou plano alternativo desde o início da produção"],
    ["Internet cair durante a votação", "Rede local, teste no D-1 e cédula impressa como "
     "alternativa"],
    ["Poucos grupos confirmarem", "Convite com antecedência, troféu e certificado "
     "garantidos e espaço de venda gratuito para cada grupo"],
    ["Público baixo", "Divulgação começando cedo, atração musical e apresentação da "
     "Explosão no encerramento"],
    ["Evento atrasar e perder o público", "Coordenação geral com relógio na mão e ordem "
     "de apresentação definida antes"],
    ["Prejuízo financeiro", "Orçamento aprovado antes, patrocínio captado e custos "
     "compartilhados com vendedores e parceiros"],
    ["Reclamação sobre o resultado", "Regras explicadas na abertura, votação transparente "
     "e números publicados depois"],
    ["A parceria com a Prefeitura não sair", "Protocolar cedo (D-90) e ter um plano de "
     "evento reduzido, que caiba no caixa da quadrilha, como alternativa"],
    ["Poucas bancas se inscreverem", "Edital divulgado com antecedência, taxa baixa na "
     "primeira edição e a divulgação do nome de cada banca como contrapartida"],
    ["Discussão por espaço no dia do evento", "Mapa fechado antes, espaços demarcados "
     "fisicamente no D-2 e equipe da feira orientando a montagem"],
    ["Comerciante não acertar a taxa no fim da noite", "Condição por escrito na "
     "confirmação da vaga, e preferência pelo valor fixo pago na inscrição quando "
     "houver dúvida"],
], larguras=[6.0, 10.0])

citacao(doc, "O Festival é uma noite. O Arraial faz a temporada durar o ano inteiro.")
p(doc, "Explosão Junina de Beruri · Arraial da Explosão", centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Arraial da Explosao - Plano do Evento.docx")
