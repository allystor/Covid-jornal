from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Noticias/1')
def news1():
    return render_template('/Noticias/news-1.html')

@app.route('/Notícias/news-2.html')
def news2():
    return render_template('news-2.html')

@app.route('/Notícias/news-3.html')
def news3():
    return render_template('nes-3.html')

@app.route('/Notícias/news-4.html')
def news4():
    return render_template('news-4.html')

@app.route('/Notícias/news-5.html')
def news5():
    return render_template('news-5.html')

@app.route('/Notícias/news-6.html')
def news6():
    return render_template('news-6.html')

@app.route('/Notícias/news-7.html')
def news7():
    return render_template('news-7.html')

@app.route('/Notícias/news-8.html')
def news8():
    return render_template('news-8.html')

@app.route('/Notícias/news-9.html')
def news9():
    return render_template('news-9.html')
