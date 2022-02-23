
from distutils.log import debug
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def static_file():
    return app.send_static_file('index.html')

@app.route('/Noticias/1')
def news1():
    return render_template('/Noticias/news-1.html')

@app.route('/Notícias/2')
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
