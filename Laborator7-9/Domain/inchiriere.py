from Domain.entities import Entity


class Inchiriere(Entity):
    def __init__(self,idInchiriere,idClient,idFilm,data_inc,data_retur):
        Entity.__init__(self, idInchiriere)
        self.__idInchiriere=idInchiriere
        self.__idClient=idClient
        self.__idFilm=idFilm
        self.__data_inc=data_inc
        self.__data_retur=data_retur

    def getIdInchiriere(self):
        return self.__idInchiriere
    def setIdInchiriere(self,inchiriere):
        self.__idInchiriere=inchiriere


    def getIdClient(self):
        return self.__idClient

    def setIdClient(self,idClient):
        self.__idClient=idClient

    def getIdFilm(self):
        return self.__idFilm
    def setIdFilm(self,IdFilm):
        self.__idFilm=IdFilm
    def getdatainc(self):
        return self.__data_inc
    def setdatainc(self,data_inc):
        self.__data_inc=data_inc
    def getdataret(self):
        return self.__data_retur

    def setdataret(self,data_retur):
        self.__data_retur=data_retur

    def __str__(self):
        return f"idInchiriere: {self.__idInchiriere}, idClient: {self.__idClient}, idFilm: {self.__idFilm}, data_inchiriere: {self.__data_inc}, data_retur: {self.__data_retur}"