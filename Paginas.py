class Paginas:

    def __init__(self,id,titulo,conteudo,img):
        self.__id = id
        self.__titulo = titulo
        self.__img = img
        self.__conteudo = conteudo

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_img(self):
        return self.__img

