from flask import render_template, request, redirect
from application import app
from application.model.dao.bandeiras_dao import BandeiraDao
from application.model.dao.pagina_dao import PrinciaisDao
from application.model.dao.pagina_dao import RecentesDao
from application.model.entity.comentario_entity import Comentario
from application.model.dao import ComentarioDAO

@app.route('/')
def index():
    principais_list = PrinciaisDao().find_all()
    recentes_list = RecentesDao().find_all()
    bandeiras_list = BandeiraDao().find_all()
    lista = ComentarioDAO.lista()
    ordenar = sorted(lista, key=lambda x : x.get_data(), reverse=True)
    return render_template('index.html', recentes_list = recentes_list, bandeiras_list = bandeiras_list, comentario=ordenar, principais_list = principais_list)

@app.route('/Principais/<int:id>',  methods=['GET'])
def Principais(id : int):
    principais_list = PrinciaisDao().find_all()
    bandeiras_list = BandeiraDao().find_all()
    lista = ComentarioDAO.lista()
    ordenar = sorted(lista, key=lambda x : x.get_data(), reverse=True)
    for principal in principais_list:
        if principal.get_id() == id:
            return render_template('Principais.html', principais=principal, bandeiras_list = bandeiras_list, comentario=ordenar)
    
@app.route('/Recentes/<int:id>', methods=['GET'])
def Recentes(id : int):
    recentes_list = RecentesDao().find_all()
    bandeiras_list = BandeiraDao().find_all()
    lista = ComentarioDAO.lista()
    ordenar = sorted(lista, key=lambda x : x.get_data(), reverse=True)
    for recente in recentes_list:
        if recente.get_id() == id:
            return render_template('Recentes.html', recentes=recente, bandeiras_list = bandeiras_list, comentario=ordenar)

@app.route('/Comentar/<int:id>', methods=['GET','POST'])
def comentar(id : int):
    usuario = request.form.get('nome','none')
    email = request.form.get('email','none')
    conteudo = request.form.get('conteudo','none')
    comentario = Comentario(usuario, email, conteudo)
    ComentarioDAO.adicionarComentario(comentario)
    if ComentarioDAO:
        return redirect("/Principais/"+str(id)), redirect("/Recentes/"+str(id))