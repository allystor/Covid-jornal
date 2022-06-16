from application.model.dao import ComentarioDAO
from datetime import datetime

class Comentario:
    def __init__(self, usuário,conteudo):
        self.__usuario = usuário
        self.__conteudo = conteudo
        self.__id = len(ComentarioDAO.Lista()) + 1
        self.__data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    def get_usuario(self):
        return self.__usuario

    def get_conteudo(self):
        return self.__conteudo
