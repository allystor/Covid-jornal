from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.bandeiras_dao import BandeiraDao

@app.route('/Estado/<int:id>')
def Estado(id : int):
    bandeiras_list = BandeiraDao().find_all()
    noticias_list = NoticiaDao().find_all()
    noticias_estado = []
    for noticia in noticias_list:
        if noticia.get_id() == id:
            noticias_estado.append(noticia)
    return render_template('Estado.html', bandeiras_list = bandeiras_list, noticias_estado = noticias_estado)
        
