class Pagina:

    def __init__(self,id,titulo,imagem,conteudo):
        self.__id = id
        self.__titulo = titulo
        self.__imagem = imagem
        self.__conteudo = conteudo

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_imagem(self):
        return self.__imagem

    def get_conteudo(self):
        return self.__conteudo


