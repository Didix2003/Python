from Domain.entities import Entity


class Filme(Entity):
    def __init__(self,idFilm,titlu,descriere, gen):
        Entity.__init__(self, idFilm)
        self.__idFilm=idFilm
        self.__titlu=titlu
        self.__descriere=descriere
        self.__gen=gen
    def getIdFilm(self):
        return self.__idFilm
    def gettitlu(self):
        return self.__titlu
    def getdescriere(self):
        return self.__descriere
    def getgen(self):
        return self.__gen
    def setIdFilm(self,idFilm):
         self.__idFilm=idFilm
    def settitlu(self,titlu):
        self.__titlu=titlu
    def setdescriere(self,descriere):
        self.__descriere=descriere
    def setgen(self,gen):
        self.__gen=gen

    def __str__(self):
        return f"id: {self.__idFilm}, titlu: {self.__titlu}, descriere: {self.__descriere}, gen:{self.__gen}"