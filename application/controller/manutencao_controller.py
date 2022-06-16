from application import app
from flask import render_template
from application.model.dao.bandeiras_dao import BandeiraDao

@app.route('/manutencao/')
def manutencao():
    bandeiras_list = BandeiraDao().find_all()
    return render_template('manutencao.html', bandeiras_list = bandeiras_list)