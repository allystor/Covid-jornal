from application.model.entity.bandeiras_entity import Bandeira

class BandeiraDao:
    def __init__(self):
        b1 = Bandeira(0,'Acre','/static/img/bandeiras/Acre.png')
        b2 = Bandeira(1,'Alagoas','/static/img/bandeiras/Alagoas.png')
        b3 = Bandeira(2,'Amapá','/static/img/bandeiras/Amapá.png')
        b4 = Bandeira(3,'Amazonas','/static/img/bandeiras/Amazonas.png')
        b5 = Bandeira(4,'Bahia','/static/img/bandeiras/Bahia.png')
        b6 = Bandeira(5,'Ceará','/static/img/bandeiras/Ceará.png')
        b7 = Bandeira(6,'Distrito Federal','/static/img/bandeiras/Distrito_federal.png')
        b8 = Bandeira(7,'Espírito Santo','/static/img/bandeiras/Espirito_santos.png')
        b9 = Bandeira(8,'Goiás','/static/img/bandeiras/Goias.png')
        b10 = Bandeira(9,'Maranhão','/static/img/bandeiras/Maranhão.png')
        b11 = Bandeira(10,'Mato Grosso','/static/img/bandeiras/Mato_grosso.png')
        b12 = Bandeira(11,'Mato Grosso do Sul','/static/img/bandeiras/Mato_grosso_do_sul.png')
        b13 = Bandeira(11,'Mato Grosso do Sul','/static/img/bandeiras/Mato_grosso_do_sul.png')
        b14 = Bandeira(13,'Pará','/static/img/bandeiras/Pará.png')
        b15 = Bandeira(14,'Paraíba','/static/img/bandeiras/Paraiba.png')
        b16 = Bandeira(15,'Paraná','/static/img/bandeiras/Paraná.png')
        b17 = Bandeira(16,'Pernambuco','/static/img/bandeiras/Pernambuco.png')
        b18 = Bandeira(17,'Piauí','/static/img/bandeiras/Piaui.png')
        b19 = Bandeira(18,'Rio de Janeiro','/static/img/bandeiras/Rio_de_janeiro.png')
        b20 = Bandeira(19,'Rio Grande do Norte','/static/img/bandeiras/Rio_grande_do_norte.png')
        b21 = Bandeira(20,'Rio Grande do Sul','/static/img/bandeiras/Rio_grande_do_sul.png')
        b22 = Bandeira(21,'Rondônia','/static/img/bandeiras/Rondonia.png')
        b23 = Bandeira(22,'Roraima','/static/img/bandeiras/Roraima.png')
        b24 = Bandeira(23,'Santa Catarina','/static/img/bandeiras/Santa_catarina.png')
        b25 =Bandeira(24,'São Paulo','/static/img/bandeiras/São_paulo.png')
        b26 = Bandeira(25,'Sergipe','/static/img/bandeiras/Sergipe.png')
        b27 = Bandeira(26,'Tocantins','/static/img/bandeiras/Tocantins.png')
        self.__db = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27]
        
    def find_all(self):
        return self.__db
    
    def find_by_id(self, id):
        for bandeira in self.__db:
            if bandeira.get_id() == id:
                return bandeira
        return None
