# -*- coding: utf-8 -*-
"""Gera 'Arraial da Explosao - Plano do Evento.docx'."""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["ARRAIAL", "DA EXPLOSÃO"],
    "Plano do evento · Temporada 2027",
    "A festa que mantém a temporada junina viva o ano todo em Beruri.",
    nota="Previsão: depois do Festival — agosto ou mais para o fim do ano. "
         "Sem data fechada.",
    rodape="Beruri – Amazonas",
    cor=VERMELHO,
)

# ---------------------------------------------------------------- o que é ---
h1(doc, "O QUE É E POR QUE EXISTE", 1)
p(doc, "O Arraial da Explosão é a festa própria da quadrilha, realizada depois do "
       "Festival Folclórico de Beruri. Ele nasce de uma constatação simples: a "
       "temporada junina morre cedo demais na cidade. Passado o Festival, tudo para — "
       "os grupos se dispersam, o público esquece e o assunto só volta no ano "
       "seguinte.")
p(doc, "O Arraial existe para quebrar esse ciclo. É a Explosão devolvendo à cidade um "
       "segundo momento de festa, reunindo as danças de Beruri e de municípios "
       "vizinhos, movimentando o comércio local e mantendo a quadrilha presente no "
       "calendário cultural o ano inteiro.")
caixa(doc, "A ambição",
      "O Arraial da Explosão não é um evento de arrecadação com dança. É uma festa "
      "cultural que também arrecada. A meta é que, em poucos anos, ele seja "
      "reconhecido como uma tradição de Beruri — algo que a cidade espera acontecer, "
      "como espera o Festival.", VERMELHO)

h2(doc, "1.1 Objetivos")
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

h2(doc, "1.2 Quando acontece")
p(doc, "A previsão é realizar o Arraial depois do Festival: em agosto, aproveitando "
       "o clima junino ainda recente, ou mais para o fim do ano, se isso permitir uma "
       "produção melhor e um público maior. A escolha é da Diretoria, considerando "
       "chuva, calendário da cidade, disponibilidade de espaço e caixa disponível.")

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
p(doc, "O Arraial é também uma oportunidade para o comércio de Beruri. Convidar os "
       "vendedores da cidade amplia a festa, atrai mais público e cria vínculo entre a "
       "quadrilha e o comércio — que depois vira parceria e patrocínio.")
tabela(doc, ["Espaço", "Quem ocupa", "Condição"], [
    ["Bancas de comerciantes", "Vendedores berurienses de comidas típicas, artesanato, "
     "bebidas e produtos", "Espaço demarcado, com confirmação prévia. Condição definida "
     "pela Diretoria (gratuito, taxa simbólica ou contrapartida)"],
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
    ["Venda de produtos oficiais e camisas", "Troféus e certificados"],
    ["Taxa ou contrapartida das bancas (se houver)", "Prêmios da votação popular"],
    ["Cotas de patrocínio específicas do evento", "Transporte e apoio às danças convidadas"],
    ["Novas adesões ao Sócio Torcedor", "Divulgação e material gráfico"],
    ["Rifa ou bingo dentro do evento (opcional)", "Ingredientes e insumos das bancas"],
    ["", "Limpeza, segurança e organização do espaço"],
], larguras=[8.0, 8.0])
p(doc, "Como todo projeto da quadrilha, o Arraial fecha com mini-balanço: receitas, "
       "custos e resultado, entregues ao Diretor Financeiro e publicados nas redes.")

h1(doc, "ESTRUTURA NECESSÁRIA", 6)
tabela(doc, ["Item", "Como conseguir"], [
    ["Espaço (praça, quadra ou área ampla)", "Apoio da Prefeitura ou parceria com escola / "
     "centro comunitário"],
    ["Palco ou área de apresentação demarcada", "Estrutura própria, empréstimo ou aluguel"],
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
], larguras=[6.0, 10.0])

h1(doc, "EQUIPES DO EVENTO", 7)
tabela(doc, ["Equipe", "Função no dia"], [
    ["Coordenação geral", "Comanda o evento, resolve imprevistos e mantém o horário"],
    ["Palco e apresentação", "Locução, ordem das apresentações e chamada dos grupos"],
    ["Som e técnica", "Áudio, microfones, playback e telão"],
    ["Votação", "Orienta o público, distribui QR code e acompanha a apuração"],
    ["Bancas e vendas", "Preparo, venda e controle de caixa da banca da Explosão"],
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
    ["D-60", "Definir data e local; formar a equipe de produção; abrir os convites às "
     "danças de Beruri e das cidades vizinhas"],
    ["D-45", "Confirmar espaço e estrutura; iniciar a captação de patrocínio específico "
     "do evento; convidar os comerciantes"],
    ["D-30", "Fechar a lista de grupos participantes; definir prêmios e categorias; "
     "encomendar troféus e certificados; abrir a divulgação"],
    ["D-20", "Definir a programação completa e a ordem das apresentações; preparar o "
     "sistema de votação; confirmar bancas e espaços"],
    ["D-15", "Divulgação pesada: artes com programação, grupos confirmados e vendedores; "
     "convite às autoridades e à imprensa"],
    ["D-7", "Reunião final da equipe; escala por função; compra de insumos das bancas; "
     "teste do sistema de votação"],
    ["D-2", "Montagem da estrutura; decoração; teste de som, iluminação e telão"],
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
], larguras=[4.5, 11.5])
caixa(doc, "Plano B obrigatório",
      "Internet em evento ao ar livre falha. O sistema precisa funcionar com rede "
      "local (sem depender da internet) ou ter cédula impressa como alternativa. Isso "
      "é testado no D-1, nunca no dia.", AMBAR)

# ---------------------------------------------------------------- checklist --
doc.add_page_break()
checklist(doc, [
    "Definir data e local do Arraial",
    "Formar a equipe de produção e distribuir funções",
    "Convidar as danças de Beruri e das cidades vizinhas",
    "Confirmar os grupos participantes e sortear a ordem de apresentação",
    "Definir as categorias de premiação",
    "Produzir troféus e certificados de participação",
    "Preparar e testar o sistema de votação popular",
    "Convidar e confirmar os comerciantes vendedores",
    "Demarcar os espaços de bancas e das danças",
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
], larguras=[6.0, 10.0])

citacao(doc, "O Festival é uma noite. O Arraial faz a temporada durar o ano inteiro.")
p(doc, "Explosão Junina de Beruri · Arraial da Explosão", centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Arraial da Explosao - Plano do Evento.docx")
