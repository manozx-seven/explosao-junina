# -*- coding: utf-8 -*-
"""Gera 'Programa Socio Torcedor Explosao Junina.docx' — material de DIVULGACAO.

Peca voltada ao publico. O documento interno equivalente e o
'Programa Socio Torcedor - Plano de Implementacao.docx' (gen_socio.py): tudo o
que estiver aqui precisa estar de acordo com ele e com o `server/niveis.js` do
site do Socio Torcedor. Foi assim que a receita da temporada ja divergiu uma vez
— documento calculando 12 meses e sistema usando 10.

Ate 29/07/2026 este arquivo nao tinha gerador (era editado avulso). Passou a ter
quando o site entrou no ar e o material precisou descrever o painel do socio.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *  # noqa

doc = novo_documento()

capa(
    doc,
    ["PROGRAMA", "SÓCIO TORCEDOR"],
    "Temporada 2027",
    "Faça parte da torcida oficial da quadrilha campeã.",
    nota="Proposta inicial — valores e benefícios ajustáveis pela coordenação.",
    rodape="Beruri – Amazonas",
    cor=VERMELHO,
)

# ---------------------------------------------------------------- o que é ----
h1(doc, "O QUE É")
p(doc, "O Sócio Torcedor é o jeito de qualquer pessoa da comunidade apoiar a "
       "Explosão o ano inteiro, com uma contribuição simbólica. Não é patrocínio de "
       "empresa (isso está no Kit Parceiro): é a torcida oficial da quadrilha, gente "
       "que gosta da Explosão e quer ajudar a manter viva a cultura de Beruri.")
p(doc, "O objetivo é criar uma base de apoio recorrente e previsível, que ajude a "
       "sustentar os projetos e as apresentações durante toda a temporada — e não só "
       "nos meses do Festival. E, mais que ajudar, o sócio entra para dentro da "
       "quadrilha: recebe carinho, reconhecimento e vantagens de verdade o ano todo.")

h1(doc, "COMO FUNCIONA")
for rot, txt in [
    ("Contribuição simbólica: ", "mensal ou por temporada, à sua escolha. A "
     "temporada tem dez meses, de fevereiro a novembro — dezembro e janeiro são "
     "livres, sem cobrança."),
    ("Vencimento no dia 5: ", "de cada mês, por Pix ou em dinheiro com a "
     "coordenação."),
    ("Adesão simples: ", "você escolhe o nível, fala com a coordenação e entra na "
     "lista oficial de sócios."),
    ("Carteirinha de Sócio Torcedor: ", "digital na hora, no seu painel. Quem aderir "
     "até fevereiro de 2027 recebe também a carteirinha física exclusiva da primeira "
     "temporada, entregue na reunião da torcida."),
    ("Seu painel no site: ", "você entra com CPF e data de nascimento e vê tudo — "
     "contribuições, troféus, missões, mural e as contas da quadrilha."),
    ("Troca de nível quando quiser: ", "dá para subir ou descer pelo próprio painel, "
     "sem pedir autorização a ninguém."),
    ("Transparência: ", "o sócio acompanha as contas da quadrilha, liberadas "
     "temporada por temporada."),
]:
    bullet(doc, txt, rotulo=rot)

# ----------------------------------------------------------------- níveis ----
h1(doc, "NÍVEIS E VALORES (proposta)")
tabela(doc, ["Nível", "Por mês", "Por temporada", "Além de todos os benefícios base"], [
    ["🔥 Fogueira", "R$ 10", "R$ 100",
     "Todos os benefícios do programa (carteirinha, Close Friends, sorteios, "
     "descontos e transparência)."],
    ["🎏 Bandeirinha", "R$ 20", "R$ 200", "Tudo do Fogueira + brinde da temporada."],
    ["⭐ Estrela do Arraial", "R$ 30", "R$ 300",
     "Tudo do Bandeirinha + blusa “Sócio Torcedor” (com o nome nas costas) + "
     "bastidores e encontro com a quadrilha."],
], larguras=[3.8, 2.2, 2.8, 7.2])
p(doc, "Os valores acima são uma sugestão de partida, propositalmente simbólicos. "
       "Podem ser ajustados pela coordenação a cada temporada.")
caixa(doc, "O nível é a faixa que você escolhe — não um cargo que se conquista",
      "Quer contribuir mais? Sobe de nível. Precisou apertar? Desce, sem "
      "constrangimento e sem perder o que já conquistou. A troca vale a partir do "
      "primeiro mês ainda não pago; mês já quitado não muda de valor.", VERDE)

# ------------------------------------------------------------- benefícios ----
h1(doc, "O QUE A QUADRILHA FAZ POR VOCÊ")

h2(doc, "Carteirinha de sócio (digital e física)")
p(doc, "Todo sócio recebe a carteirinha digital na adesão, direto no painel — e o "
       "site gera um modelo para impressão a qualquer momento. Quem aderir até "
       "fevereiro de 2027 recebe ainda a carteirinha física exclusiva da primeira "
       "temporada: design próprio, entregue pessoalmente numa reunião da torcida, "
       "item de colecionador que só esse grupo terá. Quem entrar depois recebe a "
       "carteirinha comum.")

h2(doc, "Close Friends e destaque no Instagram")
bullet(doc, "Todos os sócios entram no Close Friends do Instagram da Explosão, com "
            "bastidores, prévias e conteúdos exclusivos.")
bullet(doc, "Destaque fixo “Sócios Torcedores” no perfil, com a lista dos sócios e "
            "as publicações dedicadas à torcida.")

h2(doc, "Sorteios o ano todo")
p(doc, "Ao longo do ano, sorteios exclusivos entre os sócios, com prêmios como "
       "dinheiro, kits de mercado e descontos com os nossos parceiros. Participa "
       "quem está com a contribuição em dia — e, entre os elegíveis, todos concorrem "
       "com a mesma chance, independentemente do nível: todo apoio vale igual na "
       "hora do sorteio.")
p(doc, "A lista de participantes é publicada antes de cada sorteio, o resultado sai "
       "na hora e a entrega do prêmio fica registrada. Quem atrasa não paga multa "
       "nem juros; só fica de fora dos sorteios até regularizar.")

h2(doc, "Descontos")
bullet(doc, "Desconto na blusa da temporada, para todos os níveis.")
bullet(doc, "Descontos nos eventos da Explosão, incluindo o Arraial da Explosão.")
bullet(doc, "O nível Estrela do Arraial ganha, além do desconto, a blusa “Sócio "
            "Torcedor” com o nome nas costas.")

h2(doc, "Transparência para o torcedor")
p(doc, "O sócio tem acesso ao painel de finanças da quadrilha — receitas, despesas e "
       "destino de cada recurso —, liberado temporada por temporada pela "
       "coordenação. Você apoia sabendo para onde vai o dinheiro.")

# ------------------------------------------------------------------ painel ---
doc.add_page_break()
h1(doc, "SEU PAINEL DE SÓCIO")
p(doc, "O Programa tem site próprio, e ele já está no ar. Você entra com o seu CPF e "
       "a sua data de nascimento — sem senha para decorar — e encontra:")
tabela(doc, ["No painel", "O que você vê"], [
    ["Carteirinha digital", "Seu número de sócio, seu nível e desde quando você é da "
     "torcida"],
    ["Situação do mês", "Se está tudo em dia, o que falta e até quando"],
    ["Avisar pagamento", "Você informa que pagou e a coordenação confirma. A chave "
     "Pix fica ali, com o nome do titular e botão de copiar"],
    ["Progresso da temporada", "Quanto você já contribuiu no ano"],
    ["Histórico", "Todas as suas contribuições, com data e forma de pagamento"],
    ["Troféus", "Suas conquistas, com barra de progresso das que ainda faltam"],
    ["Missões", "As missões abertas da torcida e os seus pontos"],
    ["Mural", "Recados e novidades da quadrilha para os sócios"],
    ["Finanças", "A prestação de contas, temporada por temporada"],
    ["Meus dados", "Você corrige nome, apelido, contato e e-mail quando precisar"],
], larguras=[4.0, 12.0])
caixa(doc, "Seus dados estão seguros",
      "Seu CPF e sua data de nascimento são a sua chave de entrada — e por isso o "
      "site nunca mostra os dois em tela nenhuma, nem para você (o CPF aparece "
      "mascarado). Ninguém consegue ver a sua contribuição a não ser você e a "
      "coordenação.", AZUL)

h1(doc, "TROFÉUS: SEU APOIO VIRA CONQUISTA")
p(doc, "Cada contribuição confirmada desbloqueia conquistas no seu painel. Elas são "
       "suas, ficam registradas e contam desde o dia em que você entrou.")
tabela(doc, ["Conquista", "Como você desbloqueia"], [
    ["Primeira Fagulha", "Sua primeira contribuição confirmada"],
    ["Pontual", "Contribuir dentro do prazo"],
    ["Trio de Fogo", "Três meses seguidos em dia"],
    ["Sócio Fiel", "Três meses seguidos em dia — este é entregue na sua mão pela "
     "coordenação"],
    ["Temporada Completa", "Contribuir em todos os meses da sua temporada"],
    ["Chamador de Gente", "Indicar alguém que virou sócio de verdade"],
    ["Veterano", "Apoiar a quadrilha em mais de uma temporada"],
    ["Torcedor de Arquibancada", "Presença registrada nos eventos da quadrilha"],
    ["Missão Cumprida", "Sua primeira missão aprovada"],
    ["Puxador de Fila", "Cinco missões aprovadas na temporada"],
], larguras=[5.0, 11.0])

h1(doc, "MISSÕES DA TORCIDA")
p(doc, "Ser sócio não é só pagar. Toda semana a quadrilha publica uma missão — uma "
       "enquete sobre a Explosão, um post para compartilhar, presença num ensaio "
       "aberto, uma indicação de novo sócio. Cada missão vale pontos, e os pontos "
       "valem troféus e posição no ranking da torcida.")
bullet(doc, "São rápidas: a maioria se resolve em um minuto, no próprio site.")
bullet(doc, "Não é obrigatório: quem só quer contribuir e torcer segue com todos os "
            "benefícios.")
bullet(doc, "Quem está com o mês em aberto continua jogando; os pontos ficam "
            "guardados e são liberados quando o mês é pago.")

# ------------------------------------------------------------------ atraso ---
h1(doc, "E SE EU ATRASAR?")
p(doc, "Nada de multa, juros ou cobrança retroativa. Nunca. O que acontece é só "
       "isto:")
tabela(doc, ["Situação", "O que muda"], [
    ["Pagou depois do dia 5", "Vale como pago. Você só não ganha o troféu daquele mês "
     "e a sua sequência recomeça"],
    ["Mês em aberto", "Você fica de fora dos sorteios até regularizar. Painel, mural, "
     "missões e finanças continuam abertos"],
    ["Um mês fechado sem pagar", "Sai dos sorteios e do mural; o painel continua seu"],
    ["Dois meses seguidos sem pagar", "Sai do quadro ativo e o progresso da temporada "
     "zera"],
    ["Voltando depois", "Você mantém para sempre o número da carteirinha, a "
     "antiguidade e o histórico. Volta pagando só o mês corrente, e pode até trocar "
     "de nível na volta"],
], larguras=[5.0, 11.0])

# ------------------------------------------------------------------ destino --
h1(doc, "PARA ONDE VAI O DINHEIRO")
p(doc, "A contribuição dos sócios ajuda a manter o que faz a Explosão acontecer o "
       "ano todo:")
bullet(doc, "Figurino, blusa do tema e produção das apresentações.")
bullet(doc, "Estrutura de ensaios e dos arraiais da quadrilha.")
bullet(doc, "Transporte e logística para apresentações fora de Beruri.")
bullet(doc, "Manutenção dos projetos e das contrapartidas dos patrocinadores.")

h1(doc, "METAS (ilustrativo)")
p(doc, "Meta inicial: 100 sócios torcedores na temporada 2027. Um cenário simples de "
       "exemplo:")
bullet(doc, "60 no nível Fogueira (R$ 10) = R$ 600/mês")
bullet(doc, "30 no nível Bandeirinha (R$ 20) = R$ 600/mês")
bullet(doc, "10 no nível Estrela do Arraial (R$ 30) = R$ 300/mês")
p(doc, "Total do exemplo: cerca de R$ 1.500 por mês — aproximadamente R$ 15.000 na "
       "temporada de dez meses, só com a torcida. Números meramente ilustrativos, "
       "para dimensionar o potencial do programa.")

# ------------------------------------------------------------------ adesão ---
doc.add_page_break()
h1(doc, "COMO SE TORNAR SÓCIO TORCEDOR")
numero(doc, "Escolha o seu nível: Fogueira, Bandeirinha ou Estrela do Arraial.")
numero(doc, "Fale com a coordenação pelo WhatsApp oficial e informe nome completo, "
            "CPF, data de nascimento e contato — o CPF e a data de nascimento são o "
            "que vai te dar acesso ao painel.")
numero(doc, "Faça a contribuição pelo Pix da quadrilha (ou em dinheiro, com a "
            "coordenação).")
numero(doc, "Receba sua carteirinha digital, entre no Close Friends e acesse o seu "
            "painel de sócio no site.")
p(doc, "Em breve: a página pública do programa, com adesão e pagamento pela própria "
       "plataforma. Enquanto ela não chega, a adesão é pelo WhatsApp e a coordenação "
       "faz o cadastro — depois é você quem entra no painel.", bold_ate="Em breve: ")
p(doc, "Empresa ou negócio que quer apoiar? Fale com a coordenação sobre o Kit "
       "Parceiro, com cotas e ações promocionais próprias para parceiros.")

h1(doc, "PERGUNTAS FREQUENTES")
tabela(doc, ["Pergunta", "Resposta"], [
    ["Preciso ser de Beruri?", "Não. Qualquer pessoa que goste da Explosão pode ser "
     "sócio torcedor, de onde estiver"],
    ["Posso pagar a temporada inteira de uma vez?", "Pode. É só combinar com a "
     "coordenação na adesão"],
    ["Posso mudar de nível no meio do ano?", "Pode, quando quiser, pelo próprio "
     "painel. Vale a partir do primeiro mês ainda não pago"],
    ["Preciso participar das missões?", "Não. Elas são para quem quiser jogar junto; "
     "os benefícios do seu nível continuam iguais"],
    ["Ser Estrela aumenta minha chance no sorteio?", "Não. Todo apoio vale igual na "
     "hora do sorteio — o que muda entre os níveis são os benefícios"],
    ["Como sei que o sorteio é honesto?", "A lista de participantes é publicada "
     "antes, o resultado sai na hora e a entrega do prêmio é registrada"],
    ["Posso cancelar quando quiser?", "Pode, sem multa e sem burocracia. Sua "
     "carteirinha e o seu histórico continuam guardados se você voltar"],
    ["E se eu esquecer de pagar um mês?", "Nada acontece além de ficar fora dos "
     "sorteios até regularizar. Sem multa, sem juros, sem cobrança retroativa"],
], larguras=[5.5, 10.5])

h1(doc, "NOSSO COMPROMISSO: TRANSPARÊNCIA TOTAL")
p(doc, "Assim como com os parceiros, cada real do Sócio Torcedor entra na prestação "
       "de contas aberta da quadrilha. O painel de finanças fica disponível aos "
       "sócios, liberado temporada por temporada, com o mesmo padrão de seriedade do "
       "Kit Parceiro.")

citacao(doc, "A Explosão é de Beruri. E Beruri é de quem faz junto.")
p(doc, "FALE CONOSCO — [Nome do responsável] · [Telefone/WhatsApp] · [@explosaoberuri]",
  centro=True, tam=11, cor=GRAFITE)

salvar(doc, "Programa Socio Torcedor Explosao Junina.docx")
