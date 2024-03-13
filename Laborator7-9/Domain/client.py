from Domain.entities import Entity


class Client(Entity):
    #metode
    def __init__(self,idClient,nume,CNP):
        Entity.__init__(self,idClient)
        self.__idClient=idClient
        self.__nume=nume
        self.__CNP=CNP
    def getIdClient(self):
        return self.__idClient

    def getNume(self):
        return self.__nume

    def getCnp(self):
        return self.__CNP

    def setIdClient(self,idClient):
        self.__idClient=idClient

    def setnume(self,nume):
        self.__nume=nume

    def setCnp(self,CNP):
        self.__CNP=CNP

    def __str__(self):
        return f"id: {self.__idClient}, nume: {self.__nume}, CNP: {self.__CNP}"

#constructor
#campuri/atribute
#camp privat(__)


