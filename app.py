
from distutils.log import debug
from Pagina import Pagina
from flask import Flask, render_template, redirect

app = Flask(__name__)

listas_de_paginas = [
    Pagina(0,'Covid-19: Brasil tem a maior média móvel de mortes em seis meses','/static/img/covid-news-1.jpg','O Brasil registrou 892 mortes por covid-19 nas últimas 24 horas, segundo o levantamento do consórcio de veículos de imprensa feito junto às secretarias estaduais de Saúde do país, neste sábado (12). Com isso, o total de óbitos pelo novo coronavírus subiu para 638.124.A média móvel de mortes nos últimos sete dias é de 894 por dia – a maior registrada até hoje.')   
]
@app.route('/')
def home():
    return render_template('index.html', paginas = listas_de_paginas)

@app.route('/news-1/<id>')
def exibir_pagina(id):
    return render_template('exibir_pagina.html',pagina=listas_de_paginas[int(id)])

@app.route('/news-2')
def news2():
    return render_template('/Noticias/news-2.html')

@app.route('/Notícias/3')
def news3():
    return render_template('/Noticias/news-3.html')

@app.route('/Notícias/4')
def news4():
    return render_template('/Noticias/news-4.html')

@app.route('/Notícias/5')
def news5():
    return render_template('/Noticias/news-5.html')

@app.route('/Notícias/6')
def news6():
    return render_template('/Noticias/news-6.html')

@app.route('/Notícias/7')
def news7():
    return render_template('/Noticias/news-7.html')

@app.route('/Notícias/8')
def news8():
    return render_template('/Noticias/news-8.html')

@app.route('/Notícias/9')
def news9():
    return render_template('/Noticias/news-9.html')

if __name__ == '__main__':
    app.run(debug=True)
