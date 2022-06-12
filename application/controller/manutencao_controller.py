from application import app
from flask import render_template

@app.route('/manutencao/')
def manutencao():
    return render_template('manutencao.html')