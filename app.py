
from distutils.log import debug
from bandeiras import Estado
from pagina import Pagina
from noticia import Noticia
from flask import Flask, render_template, redirect

app = Flask(__name__)

listas_de_paginas_principais = [
    Pagina(0,'Covid-19: Brasil tem a maior média móvel de mortes em seis meses','/static/img/covid-news-1.jpg','O Brasil registrou 892 mortes por covid-19 nas últimas 24 horas, segundo o levantamento do consórcio de veículos de imprensa feito junto às secretarias estaduais de Saúde do país, neste sábado (12). Com isso, o total de óbitos pelo novo coronavírus subiu para 638.124.A média móvel de mortes nos últimos sete dias é de 894 por dia – a maior registrada até hoje. De acordo com o balanço deste sábado, o número de novos casos conhecidos de covid-19 de ontem pra hoje foi de 132.935, elevando o total de infectados para 27.424.975. A média móvel de casos do novo coronavírus nos últimos sete dias foi de 136.138 por dia, um recuo de 27% em relação aos casos registrados em 14 dias, apontando tendência de queda nos diagnósticos da doença. Os dados divulgados pelo consórcio de imprensa foram obtidos após uma parceria inédita entre “g1”, “O Globo”, “Extra”, “O Estado de S.Paulo”, “Folha de S.Paulo” e “UOL”, que passaram a trabalhar de forma colaborativa desde o dia 8 de junho de 2020 para reunir as informações necessárias nos 26 Estados e no Distrito Federal.'),
    Pagina(1,'Como estão as vacinas da Covid-19 específicas para a variante Ômicron','/static/img/covid-news-2jpg.jpg','Os vírus são microrganismos com estruturas relativamente simples, compostos basicamente de proteínas e de informações genéticas. Essa característica faz com que eles tenham uma alta capacidade de mutação. É o que acontece com o SARS-CoV-2, que já se desdobrou em centenas de linhagens diferentes. Uma delas é a variante Ômicron, identificada em novembro de 2021, e que se espalhou rapidamente pelo mundo. Desde então, laboratórios e farmacêuticas se mobilizaram para avaliar como desenvolver vacinas capazes de reduzir o alto contágio da variante. Nenhuma das atualizações dos imunizantes ainda está pronta, mas a cada dia parecemos estar mais pertos delas. A média móvel de casos do novo coronavírus nos últimos sete dias foi de 136.138 por dia, um recuo de 27% em relação aos casos registrados em 14 dias, apontando tendência de queda nos diagnósticos da doença.'), 
    Pagina(2,'Araraquara tem 2 mortes por Covid-19 e soma 655 óbitos; mais 365 casos são registrados','/static/img/covid-news-3.jpg','Araraquara (SP) registrou, neste domingo (13), mais duas mortes por Covid-19 e chega aos 655 óbitos em decorrência da doença desde o início da pandemia. As vítimas mais recentes são:idoso de 91 anos, com comorbidades, internado em hospital da rede particular desde o dia 4 de fevereiro.idoso de 69 anos, com comorbidades, internado em hospital da rede pública desde o dia 30 de janeiro. A cidade também registrou 365 novos casos da doença e soma 59.130 infectados desde o início da pandemia. Segundo o boletim do Comitê de Contingência do Coronavírus, o município tem taxa de ocupação de 56% de leitos de enfermaria e 69% de UTI.'),  
]

listas_de_paginas_recentes = [
    Pagina(3,'Covid-19: A maioria dos estados não apresentam média de crescimento na média de casos','/static/img/covid-news-4.jpg','Dados divulgados pelo Ministério da Saúde neste sábado (12) apontaram que o número de novos casos voltou a diminuir na maioria dos estados do país. Dentre os 26 estados mais o Distrito Federal, 14 apresentaram queda nas suas médias móveis de infecções e oito se mantiveram estáveis. Rio de Janeiro, Minas Gerais, Espírito Santo, Mato Grosso, Rio Grande do Sul, Santa Catarina, Paraná, Amapá, Roraima, Tocantins, Amazonas, Ceará, Rio Grande do Norte e o Distrito Federal registraram índices pelo menos 15% menores em relação há duas semanas. Ao mesmo tempo, o número médio de infecções em São Paulo, Goiás, Mato Grosso do Sul, Rondônia, Acre, Bahia, Maranhão e Pernambuco permaneceram estáveis em relação ao mesmo período. Desse modo, o panorama do Brasil se mantém em queda pelo segundo dia consecutivo após 44 dias com recordes de infecções. Com 140.234 novos casos, o número médio de brasileiros infectados chegou a 136.067, uma diminuição de 27% em relação há 14 dias. A análise da situação pandêmica é feita a partir da variação de 15% fixada por infectologistas como ponto de inflexão. Dessa maneira, se um índice registrar um aumento superior a 15% em relação há duas semanas, ele está em alta; se o índice cair mais de 15% em relação ao mesmo período, ele está em queda. Médias que permanecem entre -15% e 15% são definidas como estáveis.'),
    Pagina(4,'Covid-19: De onde poderá vir a próxima variante? Estudo aponta países prováveis','/static/img/covid-news-5.jpg','O vírus que causa a Covid-19 foi sequenciado pela primeira vez no início de 2020 e desde então já foram identificadas pela Organização Mundial de Saúde cinco "variantes preocupantes". A mais recente, a Ômicron, foi descoberta em novembro e é agora dominante em quase todos os países do mundo – a nova variante pode evitar a imunidade induzida pela vacina e se espalha mais rapidamente do que a Delta. No entanto, uma subvariante, a BA.2, parece ser ainda mais transmissível. Esta é a história que já vivemos, agora vamos à história que nos reserva – é improvável que estas variantes sejam as últimas. É impossível ter a certeza de como o vírus vai evoluir mas pesquisadores da Airfinity, na Inglaterra, empresa de dados de ciências da vida, tentaram mapear o local mais provável de aparecimento da próxima variante. A mutação de um vírus é um processo aleatório e é por isso que novas variantes bem-sucedidas são mais propensas a vir de lugares onde muitas mutações estão ocorrendo. A hipótese da Airfinity é de que vai ocorrer num local onde poucas pessoas estarão vacinadas e onde muitos sofrem com sistemas imunológicos enfraquecidos. As pessoas imunocomprometidas tendem a abrigar o vírus por mais tempo porque os respetivos corpos lutam mais para o combater, dando mais tempo para que as mutações bem-sucedidas possam se acumular e são menos propensos a produzir anticorpos após serem vacinados, o que significa que têm menos proteção contra a reinfecção.'), 
    Pagina(5,'Ministério da Saúde decide não recomendar 4ª dose de vacina contra a Covid-19','/static/img/covid-news-6.jpg','Após reunião da Câmara Técnica de Assessoramento em Imunização da Covid-19 (CTAI), nesta sexta-feira (11), o Ministério da Saúde decidiu que não vai recomendar a quarta dose de vacina no Brasil. As informações foram antecipadas pela CNN ontem. Segundo fontes da câmara técnica, o entendimento é de que não há pesquisas científicas com dados suficientes que embasam um novo reforço de imunização para pessoas que não sejam imunossuprimidas. O comitê também analisou o cenário epidemiológico atual do país antes de chegar a esta conclusão. Ainda de acordo com técnicos que compõem o comitê técnico, neste momento não deve ser aplicada a quarta dose porque as pessoas que tomaram duas doses e o reforço, ou seja, estão com o esquema vacinal completo, continuam muito bem protegidas contra a Covid- 19 e o agravamento da doença. A pasta definiu o posicionamento depois que o estado de São Paulo ampliou a vacinação ao público em geral com idade acima de 60 anos, com previsão para começar a aplicar a quarta dose a partir do dia 4 de abril. Em entrevista à CNN, o coordenador-executivo do Comitê Científico do estado de São Paulo, João Gabbardo, analisou que há evidências e experiências de outros países que mostram um benefício da dose extra de vacina para os idosos.')  
]

listas_de_paginas_estado =[
    Estado(0,'Acre','/static/img/bandeiras/Acre.png'),
    Estado(1,'Alagoas','/static/img/bandeiras/Alagoas.png'),
    Estado(2,'Amapá','/static/img/bandeiras/Amapá.png'),
    Estado(3,'Amazonas','/static/img/bandeiras/Amazonas.png'),
    Estado(4,'Bahia','/static/img/bandeiras/Bahia.png'),
    Estado(5,'Ceará','/static/img/bandeiras/Ceará.png'),
    Estado(6,'Distrito Federal','/static/img/bandeiras/distrito_federal.png'),
    Estado(7,'Espírito Santo','/static/img/bandeiras/Espirito_santo.png'),
    Estado(8,'Goiás','/static/img/bandeiras/Goias.png'),
    Estado(9,'Maranhão','/static/img/bandeiras/Maranhão.png'),
    Estado(10,'Mato Grosso','/static/img/bandeiras/Mato_grosso.png'),
    Estado(11,'Mato Grosso do Sul','/static/img/bandeiras/Mato_grosso_do_sul.png'),
    Estado(12,'Minas Gerais','/static/img/bandeiras/Minas_gerais.png'),
    Estado(13,'Pará','/static/img/bandeiras/Pará.png'),
    Estado(14,'Paraíba','/static/img/bandeiras/Paraiba.png'),
    Estado(15,'Paraná','/static/img/bandeiras/Paraná.png'),
    Estado(16,'Pernambuco','/static/img/bandeiras/Pernambuco.png'),
    Estado(17,'Piauí','/static/img/bandeiras/Piaui.png'),
    Estado(18,'Rio de Janeiro','/static/img/bandeiras/Rio_de_janeiro.png'),
    Estado(19,'Rio Grande do Norte','/static/img/bandeiras/Rio_grande_do_norte.png'),
    Estado(20,'Rio Grande do Sul','/static/img/bandeiras/Rio_grande_do_sul.png'),
    Estado(21,'Rondônia','/static/img/bandeiras/Rondonia.png'),
    Estado(22,'Roraima','/static/img/bandeiras/Roraima.png'),
    Estado(23,'Santa Catarina','/static/img/bandeiras/Santa_catarina.png'),
    Estado(24,'São Paulo','/static/img/bandeiras/Sao_paulo.png'),
    Estado(25,'Sergipe','/static/img/bandeiras/Sergipe.png'),
    Estado(26,'Tocantins','/static/img/bandeiras/Tocantins.png')
]
lista_de_noticia = [
    Noticia(6,'Rio Branco e outras cidades do Baixo, Alto Acre e Purus avançam para bandeira verde em avaliação do Comitê Covid','https://s2.glbimg.com/Nb5ECEQh2dJEujNB0A8rpjPZMLg=/0x0:540x405/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/u/6/km22dOTRqekbmjdKBptA/capturar.jpg','As regionais do Baixo Acre, Alto Acre e Purus avançaram para a bandeira verde, que representa cuidado, na avaliação do Comitê de Acompanhamento Especial da Covid-19. Já as regionais Juruá e Tarauacá/Envira permaneceram em bandeira amarela, que é de atenção. Os dados foram divulgados nesta sexta-feira (1º) pelo governo do Acre e representa o período de avaliação do dia 13 a 26 de março. Na última avaliação, divulgada no dia 7 de março, o governador Gladson Cameli manteve todas as cidades do Acre em nível de atenção (bandeira amarela) na classificação de risco da pandemia até o dia 31 de março, após aumento de casos no mês de fevereiro.')
]
@app.route('/')
def home():
    return render_template('index.html',paginas=listas_de_paginas_principais,paginas_2=listas_de_paginas_recentes,paginas_3=listas_de_paginas_estado, pagina_4=lista_de_noticia)

@app.route('/manutencao/')
def manutencao():
    return render_template('manutencao.html')

@app.route('/news-1/<id>')
def Principais(id):
    return render_template('Principais.html',principais=listas_de_paginas_principais[int(id)])
    
@app.route('/news-2/<id>')
def Recentes(id):
    return render_template('Recentes.html',recentes=listas_de_paginas_recentes[int(id)])

@app.route('/estado/<id>')
def Estados(id):
    return render_template('Estado.html',noticia=lista_de_noticia[int(id)], paginas_3=listas_de_paginas_estado)

@app.route('/noticia/<id>')
def noticia(id):
    return render_template('Noticia.html',noticia=listas_de_paginas_principais[int(id)])

if __name__ == '__main__':
    app.run(debug=True)
