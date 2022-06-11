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
    
    principais = PrinciaisDao().find_by_id(id)
    recentes = RecentesDao().find_by_id(id)
    bandeiras = BandeiraDao().find_by_id(id)
    
    index_list = [principais, recentes, bandeiras]
    
    return render_template('index.html', index_list = index_list, principais_list = principais_list, recentes_list = recentes_list, bandeiras_list = bandeiras_list)

if __name__ == '__main__':
    app.run(debug=True)