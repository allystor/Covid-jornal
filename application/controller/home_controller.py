from flask import render_template
from application import app
from application.model.entity.bandeiras_entity import Bandeira
from application.model.dao.bandeiras_dao import BandeiraDao
from application.model.entity.noticia_entity import Noticia
from application.model.dao.noticia_dao import NoticiaDao
from application.model.entity.pagina_entity import Pagina
from application.model.dao.pagina_dao import PrinciaisDao
from application.model.dao.pagina_dao import RecentesDao

@app.route('/')
def index():
    principais_list = PrinciaisDao().find_all()
    recentes_list = RecentesDao().find_all()
    bandeiras_list = BandeiraDao().find_all()
    return render_template('index.html', principais_list = principais_list, recentes_list = recentes_list, bandeiras_list = bandeiras_list)

@app.route('/Principais/<int:id>')
def Principais(id : int):
    principais_list = PrinciaisDao().find_all()
    for principal in principais_list:
        if principal.get_id() == id:
            return render_template('Principais.html', principais=principal)
    
@app.route('/Recentes/<int:id>')
def Recentes(id : int):
    recentes_list = RecentesDao().find_all()
    for recente in recentes_list:
        if recente.get_id() == id:
            return render_template('Recentes.html', recentes=recente)

if __name__ == '__main__':
    app.run(debug=True)