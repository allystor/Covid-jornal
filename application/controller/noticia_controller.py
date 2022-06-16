from flask import redirect, render_template, request, url_for
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.bandeiras_dao import BandeiraDao
from application.model.dao import ComentarioDAO
from application.model.entity.comentario_entity import Comentario


@app.route('/Noticia/<int:id>', methods=['GET'])
def Noticia(id : int):
    bandeiras_list = BandeiraDao().find_all()
    noticias_list = NoticiaDao().find_all()
    lista = ComentarioDAO.Lista()
    ordenar = sorted(lista, key=lambda x: x.__data(), reverse=True)
    for noticias in noticias_list:
        if noticias.get_id() == id:
            return render_template('Noticia.html', noticias=noticias, bandeiras_list=bandeiras_list, lista=ordenar)

@app.route('/Comentar/', methods=['GET', 'POST'])
def comentarios():
    usuario = request.form.get('nome', 'none')
    conteudo = request.form.get('conteudo', 'none')
    comentario = Comentario(usuario, conteudo)
    ComentarioDAO.adicionarComentario(comentario)
    if ComentarioDAO:
        return render_template('Noticia.html', comentario=ComentarioDAO.Lista())