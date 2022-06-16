class ComentarioDAO:
    def __init__(self):
        self.__lista = []
    
    def adicionarComentario(self, comentario):
        self.__lista.append(comentario)
    
    def Lista(self):
        return self.__lista