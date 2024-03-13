class InchiriereRepository:
    def __init__(self):
        self.__inchiriere={}
    def getAll(self):
        '''
        da lista de inchirieri
        :return: o lista de obiecte de tipul Inchirieri
        '''
        return self.__inchiriere.values()

    def getbyid3(self, idInchiriere):
        '''
        cauta o inchiriere dupa id
        :param idInchiriere: int
        :return: o inchiriere daca exista unul cu id dat sau None in caz contrar
        '''
        if idInchiriere in self.__inchiriere:
            return self.__inchiriere[idInchiriere]
        return None
    def adauga(self,inchiriere):
        '''
        adauga o inchiriere
        :param inchiriere: obiect de tipul Inchiriere
        :return:
        '''
        if self.getbyid3(inchiriere.getIdInchiriere()):
            raise KeyError("Exista deja acest id")
        self.__inchiriere[inchiriere.getIdInchiriere()] = inchiriere

    def retur(self,idInchiriere):
        '''
        sterge o inchiriere expirata
        :param idInchiriere: int
        :return:
        '''
        if self.getbyid3(idInchiriere) is None:
            raise KeyError("Nu exista id-ul dat ")
        self.__inchiriere.pop(idInchiriere)
