from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.bandeiras_dao import BandeiraDao

@app.route('/Noticia/<int:id>')
def Noticia(id : int):
    bandeiras_list = BandeiraDao().find_all()
    noticias_list = NoticiaDao().find_all()
    for noticias in noticias_list:
        if noticias.get_id() == id:
            return render_template('Noticia.html', noticias=noticias, bandeiras_list=bandeiras_list)