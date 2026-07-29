# -*- coding: utf-8 -*-
"""Gera 'Contrato e Bonificacao - Guia Explicativo.docx'.

O contrato em si ('Contratos Explosao Junina Final.docx') e o instrumento que se
assina — juridico, seco, sem explicacao. Este guia e o documento que faltava: por
que o contrato existe, para que serve, o que ele protege, como funciona o
Programa de Bonificacao (agora com teto) e como cada regra dele vive dentro do
Sistema de Avaliacao. E o material de leitura da coordenacao e da reuniao de
assinatura — nao substitui o contrato.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

TETO = "R$ 80,00"

doc = novo_documento()

capa(
    doc,
    ["CONTRATO E", "BONIFICAÇÃO"],
    "Guia explicativo · Temporada 2027",
    "Por que a Explosão Junina assina contrato com seus brincantes, e como "
    "funciona o Programa de Bonificação.",
    nota="Documento de apoio. Quem manda é o Termo de Compromisso assinado "
         "(“Contratos Explosao Junina Final”); este guia existe para explicá-lo "
         "em linguagem de gente.",
    rodape="Beruri – Amazonas",
    cor=VERMELHO,
)

# ------------------------------------------------------------- por que existe -
h1(doc, "POR QUE EXISTE UM CONTRATO", 1)
p(doc, "Durante anos a Explosão funcionou no combinado de boca. Deu certo enquanto "
       "o grupo era pequeno e todo mundo se conhecia. Não dá mais: a quadrilha "
       "passou de meia centena de brincantes, recebe e movimenta dinheiro, tem "
       "figurino caro sob responsabilidade de cada um, viaja com menores de idade, "
       "publica imagem em rede social e agora sustenta um programa de bonificação "
       "e um programa de sócios torcedores.")
p(doc, "Quando um grupo chega nesse tamanho, o que não está escrito vira discussão. "
       "E discussão dentro de quadrilha não acaba em processo: acaba em gente "
       "saindo, em fila desfalcada e em coordenação desmoralizada. O contrato existe "
       "para que ninguém precise lembrar do que foi combinado — está escrito, e é o "
       "mesmo para todos.")

caixa(doc, "O que este contrato é — e o que ele não é",
      "É um TERMO DE COMPROMISSO entre a quadrilha e o brincante: um acordo de "
      "participação cultural, voluntária e sem remuneração. NÃO é contrato de "
      "trabalho, não cria vínculo empregatício, não gera salário, férias, 13º ou "
      "carteira assinada — e a própria Cláusula Sexta, IX, diz isso com todas as "
      "letras. A bonificação é incentivo simbólico, não pagamento por serviço "
      "prestado.", VERMELHO)

h2(doc, "1.1 Os cinco problemas que ele resolve")
tabela(doc, ["Situação real", "O que acontece sem contrato", "O que o contrato faz"], [
    ["Brincante some no meio da temporada",
     "A fila fica desfalcada às vésperas do Festival e não há nada a dizer",
     "Prazo de aviso, regra de desligamento e consequência conhecida desde o "
     "primeiro dia"],
    ["Figurino caro se perde ou volta destruído",
     "O prejuízo fica com a quadrilha, sem conversa possível",
     "Zelo e devolução são compromisso assinado (Cláusula Segunda, “h”)"],
    ["Brincante vai dançar em quadrilha rival",
     "Vira fofoca, briga e mágoa dentro do grupo",
     "Regra escrita e igual para todos, com consequência definida"],
    ["Foto e vídeo do brincante nas redes",
     "A quadrilha publica sem autorização formal — risco desnecessário",
     "Cessão de uso de imagem assinada (Cláusula Quarta)"],
    ["Menor de idade viajando para outro município",
     "A quadrilha assume uma responsabilidade que não é dela por escrito",
     "Anexos I e II: autorização do responsável e designação de quem responde "
     "por ele na viagem"],
], larguras=[4.5, 5.5, 6.0])

h2(doc, "1.2 O contrato protege os dois lados")
p(doc, "É um erro comum ler o contrato como uma lista de obrigações do brincante. "
       "Metade dele é obrigação da quadrilha — e essa metade é a que o brincante "
       "pode cobrar.")
tabela(doc, ["A quadrilha se compromete a", "Onde está"], [
    ["Fornecer figurino completo e camisa do tema, sem custo", "Cláusula Terceira, “a”"],
    ["Produzir as apresentações (adereços, montagem, palco)", "Cláusula Terceira, “b”"],
    ["Providenciar alimentação nos ensaios, conforme disponibilidade", "Cláusula Terceira, “c”"],
    ["Organizar transporte para eventos externos", "Cláusula Terceira, “d”"],
    ["Manter ambiente respeitoso e seguro", "Cláusula Terceira, “e”"],
    ["Comunicar datas, horários e locais com antecedência", "Cláusula Terceira, “f”"],
    ["Publicar prestação de contas periódica", "Cláusula Terceira, “g”"],
    ["Tratar todos os brincantes com igualdade", "Cláusula Terceira, “h”"],
    ["Avaliar de forma justa, transparente e formativa", "Cláusulas Terceira “i” e Quinta"],
    ["Ouvir o brincante antes de qualquer desligamento", "Cláusulas Sétima, Oitava e Décima"],
], larguras=[10.5, 5.5])
caixa(doc, "A avaliação não é para punir",
      "A Cláusula Quinta, IV é explícita: a avaliação tem caráter formativo, nunca "
      "punitivo. Nota baixa não exclui ninguém — ela direciona apoio. Quem tem mais "
      "dificuldade recebe acompanhamento mais próximo. Isso está no contrato porque "
      "é promessa, e promessa escrita se cobra.", VERDE)

# ------------------------------------------------------------ valor juridico --
doc.add_page_break()
h1(doc, "A IMPORTÂNCIA JURÍDICA", 2)
p(doc, "O contrato não existe para ir a juízo — existe para que nunca seja preciso. "
       "Mas, se um dia for, é ele que responde por escrito o que aconteceu, o que "
       "cada um aceitou e o que foi cumprido.")

h2(doc, "2.1 Ele afasta o vínculo empregatício")
p(doc, "Esse é o ponto mais sensível de qualquer grupo que paga algum valor a quem "
       "participa. A lei trabalhista reconhece vínculo quando existem, ao mesmo "
       "tempo, pessoalidade, habitualidade, subordinação e salário. O Termo trata "
       "disso de frente:")
for rot, txt in [
    ("Adesão voluntária: ", "participar da quadrilha não depende de aderir ao "
     "programa, e a Cláusula Sexta abre dizendo isso."),
    ("Valor simbólico: ", "centavos por ensaio, com teto de " + TETO + " na "
     "temporada inteira. Nenhuma leitura razoável transforma isso em salário."),
    ("Sem contraprestação de serviço: ", "a bonificação reconhece comprometimento e "
     "presença, não trabalho executado."),
    ("Declaração expressa: ", "as Cláusulas Sexta, IX e Décima, 10.1 afirmam que não "
     "há vínculo empregatício."),
    ("A coordenação não recebe: ", "quem organiza está fora do programa — o que "
     "reforça o caráter de incentivo, e não de folha de pagamento."),
]:
    bullet(doc, txt, rotulo=rot)

h2(doc, "2.2 Ele autoriza o uso de imagem")
p(doc, "Imagem é direito da pessoa. Publicar foto, vídeo, story ou transmissão sem "
       "autorização é risco real — inclusive de indenização — e cresce quando há "
       "menores envolvidos. A Cláusula Quarta resolve isso: cessão gratuita, para "
       "fins de divulgação da quadrilha e acervo histórico, válida na temporada, sem "
       "uso comercial por terceiros e com autorização do responsável quando o "
       "brincante for menor de 18 anos.")

h2(doc, "2.3 Ele protege o menor de idade e a família")
p(doc, "Os Anexos I e II são a parte mais importante do contrato do ponto de vista "
       "legal. O Anexo I é a autorização do responsável para a participação. O Anexo "
       "II é a autorização de viagem, assinada caso a caso, designando por nome e "
       "CPF os coordenadores adultos que respondem pelo menor durante o "
       "deslocamento.")
caixa(doc, "Regra que não se flexibiliza",
      "O Anexo I não autoriza viagem automaticamente. Cada viagem é comunicada e "
      "consultada individualmente, com destino, datas, transporte e responsáveis "
      "informados antes. O responsável legal sempre pode acompanhar, e a quadrilha "
      "o inclui no planejamento. Sem Anexo II assinado, o menor não viaja.", VERMELHO)

h2(doc, "2.4 Ele garante defesa antes de punição")
p(doc, "As sanções são progressivas (advertência verbal, advertência formal, "
       "desligamento) e o desligamento por iniciativa da quadrilha só ocorre depois "
       "de esgotada essa escala — exceto em agressão física. Em todos os casos, o "
       "brincante é comunicado e tem direito de se manifestar. Isso protege o "
       "brincante da arbitrariedade e protege a coordenação da acusação de "
       "perseguição.")

h2(doc, "2.5 Formalidades que valem a pena")
tabela(doc, ["Item", "Por que importa"], [
    ["Duas vias de igual teor", "Cada lado fica com a sua. Contrato que só uma parte "
     "tem vale menos"],
    ["Duas testemunhas", "Reforçam a validade do que foi assinado"],
    ["Foro da Comarca de Beruri/AM", "Define onde qualquer discussão seria tratada"],
    ["Reconhecimento de firma (opcional)", "Não é obrigatório hoje; pode ser adotado "
     "em temporadas futuras conforme o grupo cresce"],
    ["Assinatura antes do início dos ensaios", "Contrato assinado depois do problema "
     "não resolve o problema"],
], larguras=[5.5, 10.5])

caixa(doc, "Aviso honesto",
      "Este guia e o Termo foram escritos pela própria coordenação, com cuidado, mas "
      "sem parecer de advogado. Antes da assinatura da temporada 2027, vale a leitura "
      "de um profissional — sobretudo das cláusulas de imagem, dos anexos de menor de "
      "idade e da natureza não empregatícia da bonificação.", AMBAR)

# ------------------------------------------------------------- bonificacao ----
doc.add_page_break()
h1(doc, "O PROGRAMA DE BONIFICAÇÃO", 3)
p(doc, "O Programa de Bonificação é o reconhecimento em dinheiro — simbólico — de "
       "quem esteve presente e se dedicou durante a temporada. Ele não paga o "
       "trabalho do brincante: nenhum valor pagaria. Ele devolve um gesto concreto a "
       "quem sustentou o grupo indo a ensaio, apresentação e Festival.")

h2(doc, "3.1 Como funciona, do começo ao fim")
tabela(doc, ["Etapa", "O que acontece"], [
    ["1. Adesão", "O brincante marca SIM ao assinar o Termo. Quem marcar NÃO pode "
     "aderir até 30 de abril; depois disso, só na próxima temporada"],
    ["2. Ativação (3 meses)", "Contados da adesão de cada um. Nesse período ele "
     "ensaia e é avaliado normalmente, mas ainda não acumula. Para ativar: presença "
     "≥ 75% (Item: 85%) e nota ≥ 4 em pelo menos 75% dos ensaios"],
    ["3. Acumulação", "Terminada a ativação, cada presença passa a valer dinheiro, "
     "até o Festival Folclórico de Beruri"],
    ["4. Teto", "Ao alcançar " + TETO + " acumulados, o brincante para de acumular e "
     "mantém o que tem"],
    ["5. Fechamento", "A contagem encerra na data do Festival. Ensaios posteriores "
     "não geram bonificação, embora o contrato siga vigente"],
    ["6. Destino", "Com o valor fechado, o brincante escolhe resgatar ou doar à "
     "quadrilha, no todo ou em parte"],
    ["7. Pagamento", "Após o Festival, cumpridos os requisitos de resgate"],
], larguras=[3.5, 12.5])

h2(doc, "3.2 Quanto vale cada coisa")
tabela(doc, ["Evento", "Valor", "Observação"], [
    ["Ensaio (regular ou ensaião)", "R$ 0,50", "Precisa estar presente e avaliado"],
    ["Apresentação oficial externa", "R$ 1,00", "Festivais, arraiais de escolas e "
     "agremiações, empresas, outros municípios"],
    ["Festival Folclórico de Beruri", "R$ 5,00", "Bônus do evento principal da temporada"],
    ["Apresentação para a Igreja Católica", "R$ 0,00", "Retribuição à parceria histórica "
     "que cedeu espaço e apoio à quadrilha desde o começo"],
    ["Atividades (arrecadação, braçal, comunitária)", "R$ 0,00", "São obrigação da "
     "Cláusula Segunda, “l”: têm presença registrada, mas não geram bonificação nem "
     "entram na frequência"],
], larguras=[5.5, 2.5, 8.0])

h2(doc, "3.3 O teto de " + TETO)
caixa(doc, "A regra em uma frase",
      "Nenhum brincante acumula mais de " + TETO + " na temporada. Ao chegar no teto, "
      "ele mantém tudo o que acumulou e para de somar.", VERMELHO)
p(doc, "O teto entrou na temporada 2027 por um motivo de orçamento, e é honesto "
       "dizer isso com clareza: o programa precisa dar um retorno simbólico a quem "
       "se dedicou, sem virar uma despesa que a quadrilha não sabe de antemão quanto "
       "vai ser. Sem teto, o custo do programa depende de quantos convites de "
       "apresentação aparecerem — e isso ninguém controla.")
tabela(doc, ["Pergunta", "Resposta"], [
    ["Isso reduz o que eu ia receber?",
     "Não, nas contas de hoje. Com 100% de presença, o máximo possível na temporada "
     "2027 é R$ 44,00 — bem abaixo do teto. O teto só passa a limitar se os valores "
     "por evento subirem ou se a temporada tiver muito mais apresentações que o "
     "previsto"],
    ["Chegando no teto, posso faltar?",
     "Não. Presença, nota, conduta e participação nas atividades continuam sendo "
     "requisitos para RECEBER (Cláusula Sexta, VII). Atingir o teto não dispensa "
     "ninguém de nada"],
    ["O teto vale para o Item Destaque também?",
     "Sim. É o mesmo para todos — muda a frequência exigida (85%), não o teto"],
    ["E com o Programa de Fidelidade, em 2028?",
     "O teto continua valendo. Mesmo no Nível 3, com o dobro por ensaio, o acumulado "
     "para em " + TETO],
    ["Quem decide o valor do teto?",
     "A Diretoria, a cada temporada, junto com os valores por evento. No sistema é um "
     "único campo na tela de Configurações"],
], larguras=[5.0, 11.0])

h2(doc, "3.4 Quando se perde a bonificação")
tabela(doc, ["Situação", "Perda"], [
    ["Advertência formal (2ª ocorrência)", "50% do acumulado"],
    ["3ª ocorrência / desligamento por falta grave", "100%"],
    ["Agressão física (gravidade extrema)", "100%, com desligamento imediato"],
    ["Abandono sem aviso (10 faltas seguidas ou 20 alternadas injustificadas)",
     "100%, com direito de defesa antes do desligamento"],
    ["Ingresso em quadrilha rival", "100%"],
    ["Saída nos 15 dias anteriores ao Festival, sem força maior", "100%"],
    ["Saída voluntária avisada, fora dessa janela", "Mantém o proporcional acumulado"],
], larguras=[9.5, 6.5])
p(doc, "O desconto por sanção incide sobre o total acumulado — e depois do teto. Um "
       "brincante que acumulou R$ 120 com teto de R$ 80 e recebeu advertência formal "
       "fica com R$ 40, não com R$ 60. A ordem é essa no contrato e é essa no "
       "sistema.", bold_ate="Ordem das contas: ")

h2(doc, "3.5 O que a quadrilha se compromete a gastar")
tabela(doc, ["Cenário (57 brincantes, ~38 ativados)", "Custo estimado"], [
    ["Máximo teórico com os valores atuais (100% de presença)", "38 × R$ 44 = R$ 1.672,00"],
    ["Cenário realista (80% de presença no período remunerado)", "≈ R$ 1.330,00"],
    ["Cenário conservador (75% + perdas por sanção)", "≈ R$ 1.088,00"],
    ["Compromisso máximo com o teto (pior caso possível)", "38 × R$ 80 = R$ 3.040,00"],
], larguras=[10.0, 6.0])
p(doc, "A última linha é a que interessa ao Diretor Financeiro: é o número que o "
       "teto garante que nunca será ultrapassado, aconteça o que acontecer na "
       "temporada. Sem ele, essa linha não existiria.")

# ---------------------------------------------------------------- sistema -----
doc.add_page_break()
h1(doc, "COMO O SISTEMA DE AVALIAÇÃO ENTRA NISSO", 4)
p(doc, "O contrato é a regra; o Sistema de Avaliação é onde a regra acontece. Quase "
       "toda cláusula com número dentro tem um espelho no sistema — e é isso que "
       "impede o contrato de virar papel de gaveta.")

h2(doc, "4.1 Cláusula por cláusula, dentro do sistema")
tabela(doc, ["No contrato", "No sistema"], [
    ["Cláusula Segunda — frequência mínima e aviso de falta",
     "Chamada por evento, com falta justificada marcada quando avisada com 24h de "
     "antecedência. O percentual de presença é calculado sozinho"],
    ["Cláusula Segunda, “l” — atividades obrigatórias",
     "Tipos de atividade (arrecadação, braçal, comunitária) com presença registrada, "
     "sem gerar bonificação nem entrar na frequência de ensaios"],
    ["Cláusula Quinta — avaliação de 1 a 5",
     "Nota e observação por brincante em cada ensaio, com histórico que ele mesmo "
     "consulta"],
    ["Cláusula Quinta, IV — caráter formativo",
     "O perfil mostra dicas conforme o desempenho, apontando o que melhorar em vez "
     "de só exibir a nota"],
    ["Cláusula Sexta, I — adesão até 30 de abril",
     "O sistema recusa adesão depois da data de corte configurada"],
    ["Cláusula Sexta, II — ativação de 3 meses proporcional",
     "Calculada automaticamente a partir da data de adesão; o perfil mostra se "
     "frequência e nota foram atingidas"],
    ["Cláusula Sexta, III — valores por tipo de evento",
     "Configuráveis pela coordenação, com valor específico por evento quando preciso"],
    ["Cláusula Sexta, III, “e” — teto de " + TETO,
     "Campo único na tela de Configurações. O acumulado trava no teto e o perfil "
     "avisa quanto falta para chegar nele"],
    ["Cláusula Sexta, V — Igreja não gera bonificação",
     "Tipo de evento “igreja”, que soma presença e não soma valor"],
    ["Cláusula Sexta, VI — contagem termina no Festival",
     "Datas de início e fim da contagem na configuração da temporada"],
    ["Cláusula Sexta, VII, “d” — resgatar ou doar",
     "Escolha do brincante no próprio perfil, liberada pela coordenação quando o "
     "valor está fechado"],
    ["Cláusula Sétima — sanções progressivas",
     "Advertências registradas por nível, com o desconto aplicado sozinho sobre o "
     "acumulado"],
    ["Cláusula Oitava — desligamento",
     "Situação do membro (ativo, afastado, desligado) com o motivo definindo se a "
     "bonificação é mantida proporcional ou perdida"],
], larguras=[6.5, 9.5])

h2(doc, "4.2 O que cada um vê")
tabela(doc, ["Quem", "O que enxerga"], [
    ["Brincante", "Apenas o próprio desempenho: presença, notas, histórico de "
     "eventos, situação da ativação, quanto acumulou, quanto falta para o teto, "
     "advertências registradas, dicas do que melhorar, quando e como será pago, e a "
     "escolha entre resgatar e doar"],
    ["Coordenação", "Tudo: cadastro, eventos, chamada e nota, ranking, painel de "
     "bonificação com o total da temporada e o compromisso máximo do teto, "
     "advertências, missão de captação de sócios e registro de todas as ações"],
], larguras=[3.5, 12.5])

h2(doc, "4.3 Por que o registro é o que protege todo mundo")
p(doc, "A frase que resume: o que não está no sistema não aconteceu. Cada presença, "
       "nota, advertência e alteração fica registrada com data, hora e autor. Isso "
       "sustenta o contrato dos dois lados.")
for rot, txt in [
    ("Para o brincante: ", "ele acompanha em tempo real e pode contestar antes do "
     "fim da temporada, não depois. Nada é decidido de surpresa."),
    ("Para a coordenação: ", "a decisão sobre bonificação, promoção de fila ou "
     "desligamento se apoia em histórico, não em memória."),
    ("Para a Diretoria: ", "o custo do programa é conhecido a qualquer momento, e o "
     "teto define o compromisso máximo antes de a temporada começar."),
    ("Para a prestação de contas: ", "o valor pago em bonificação entra no balanço "
     "público da temporada com número, não com estimativa."),
]:
    bullet(doc, txt, rotulo=rot)

caixa(doc, "O que o sistema NÃO faz",
      "A missão de captação de sócios torcedores vale reconhecimento e troféu — "
      "nunca dinheiro. Ela não entra na frequência, no ranking de desempenho nem na "
      "bonificação, e por isso não toca o contrato. Foi desenhada assim de "
      "propósito: misturar as duas coisas transformaria o contrato num acordo de "
      "vendas.", AZUL)

# ------------------------------------------------------------------ perguntas -
doc.add_page_break()
h1(doc, "PERGUNTAS QUE O BRINCANTE FAZ", 5)
tabela(doc, ["Pergunta", "Resposta"], [
    ["Sou obrigado a assinar?",
     "Sim, para participar da temporada — é o que define os deveres dos dois lados. "
     "Mas aderir ao Programa de Bonificação é opcional e não muda em nada a sua "
     "participação na quadrilha"],
    ["Se eu não aderir à bonificação, danço menos?",
     "Não. Fila, posição, figurino e presença nas apresentações não têm relação com "
     "o programa"],
    ["Isso é emprego? Vou ter carteira assinada?",
     "Não. É participação cultural voluntária. A bonificação é incentivo simbólico e "
     "o contrato declara isso expressamente"],
    ["Quanto vou receber, na prática?",
     "Com presença integral, algo em torno de R$ 44,00 na temporada, limitado ao "
     "teto de " + TETO],
    ["Quando recebo?",
     "Depois do Festival, com data divulgada pela coordenação e informada no seu "
     "perfil no sistema"],
    ["Posso doar minha bonificação para a quadrilha?",
     "Pode, no todo ou em parte. A escolha é sua e fica registrada no sistema"],
    ["Faltei por doença. Perco tudo?",
     "Não. Falta avisada com 24h é registrada como justificada. O que pesa é a "
     "ausência reiterada e sem justificativa"],
    ["Recebi advertência. Perco tudo?",
     "Depende do nível: verbal só registra; formal desconta 50%; a terceira "
     "ocorrência leva a desligamento e perda integral. Você é comunicado e tem "
     "direito de se manifestar"],
    ["Sou menor de idade. O que muda?",
     "Seu responsável assina o Anexo I, e cada viagem exige o Anexo II específico, "
     "com os coordenadores responsáveis nomeados"],
    ["Onde vejo tudo isso?",
     "No sistema, com seu ID e CPF: presença, notas, acumulado, quanto falta para o "
     "teto e o histórico completo"],
], larguras=[5.5, 10.5])

h1(doc, "PARA A COORDENAÇÃO: O DIA DA ASSINATURA", 6)
checklist(doc, [
    "Revisar o Termo com as datas da temporada 2027 antes de imprimir",
    "Conferir se os valores e o teto do contrato batem com a tela de Configurações",
    "Imprimir duas vias por brincante (uma fica com ele)",
    "Preencher os contatos oficiais da coordenação no quadro da primeira página",
    "Explicar em voz alta, antes de assinar: bonificação é opcional, tem teto e não é salário",
    "Conferir a marcação SIM/NÃO do Programa de Bonificação em cada termo",
    "Separar quem é menor de idade e recolher o Anexo I assinado pelo responsável",
    "Colher as assinaturas das duas testemunhas",
    "Cadastrar cada brincante no sistema com a data de adesão real",
    "Marcar no sistema quem aderiu ao programa (a ativação passa a contar dali)",
    "Arquivar as vias da quadrilha em ordem, com os anexos junto",
    "Guardar o Anexo II de cada viagem junto ao termo do brincante",
], titulo="CHECKLIST DA REUNIÃO DE ASSINATURA")

citacao(doc, "O contrato não existe porque desconfiamos uns dos outros. "
             "Existe para que ninguém precise desconfiar.")
p(doc, "Explosão Junina de Beruri · Guia do Contrato e da Bonificação",
  centro=True, tam=10, cor=CINZA_TEXTO)

salvar(doc, "Contrato e Bonificacao - Guia Explicativo.docx")
