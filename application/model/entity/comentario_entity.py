from application.model.dao import ComentarioDAO
from datetime import datetime

class Comentario:
    def __init__(self, usuário, email, conteudo):
        self.__usuario = usuário
        self.__email = email
        self.__conteudo = conteudo
        self.__id = len(ComentarioDAO.lista()) + 1
        self.__data = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
    def get_usuario(self):
        return self.__usuario
    
    def get_email(self):
        return self.__email

    def get_conteudo(self):
        return self.__conteudo
    
    def get_data(self):
        return self.__data
