from flask import render_template
from application import app
from application.model.entity.noticia_entity import Noticia
from application.model.dao.noticia_dao import NoticiaDao
from application.model.entity.bandeiras_entity import Bandeira
from application.model.dao.bandeiras_dao import BandeiraDao

@app.route('/Estado/<int:id>')
def Estado(id : int):
    bandeiras_list = BandeiraDao().find_all()
    noticias_list = NoticiaDao().find_all()
    for noticia in noticias_list:
        if noticia.get_id() == id:
            return render_template('Noticia.html', noticia=noticia, bandeiras_list=bandeiras_list)
    return render_template('Estado.html', bandeiras_list=bandeiras_list, noticias_list=noticias_list)