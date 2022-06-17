import email
from flask import redirect, render_template, request
from application import app
from application.model.dao.noticia_dao import NoticiaDao
from application.model.dao.bandeiras_dao import BandeiraDao
from application.model.dao import ComentarioDAO
from application.model.entity.comentario_entity import Comentario


@app.route('/Noticia/<int:id>', methods=['GET'])
def Noticia(id : int):
    bandeiras_list = BandeiraDao().find_all()
    noticias_list = NoticiaDao().find_all()
    lista = ComentarioDAO.lista()
    ordenar = sorted(lista, key=lambda x : x.get_data(), reverse=True)
    for noticias in noticias_list:
        if noticias.get_id() == id:
            return render_template('Noticia.html', noticias=noticias, bandeiras_list=bandeiras_list, comentario=ordenar)

@app.route('/Comentar/<int:id>', methods=['POST'])
def comentarios(id : int):
    usuario = request.form.get('nome')
    email = request.form.get('email')
    conteudo = request.form.get('conteudo')
    comentario = Comentario(usuario, email, conteudo)
    ComentarioDAO.adicionarComentario(comentario)
    if ComentarioDAO:
        return redirect("/Noticia/"+str(id))