class ComentarioDAO:
    def __init__(self):
        self.__lista = []
    
    def adicionarComentario(self, comentario):
        self.__lista.append(comentario)
    
    def lista(self):
        return self.__lista