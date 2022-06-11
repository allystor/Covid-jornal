class Bandeira:
    
    def __init__(self,id, titulo, bandeira):
        self.__id = id
        self.__titulo = titulo
        self.__bandeira = bandeira

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_bandeira(self):
        return self.__bandeira