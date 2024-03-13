from Domain.client import Client
from repository.repository import Repository


class ClientService:
    def __init__(self, clientrepository: Repository):
        self.__clientrepository=clientrepository



    def getClientbyid(self,idClient):
        return self.__clientrepository.getById(idClient)
    def getAllClient(self):
        '''
        da toata lista de clienti
        :return: o lista de obiecte de tipul client
        '''

        return self.__clientrepository.getAll()
    def adaugaClient(self,idClient,nume,CNP):
        '''
        adauga un client
        :param idClient:
        :param nume: string
        :return:
        '''
        client=Client(idClient,nume,CNP)
        self.__clientrepository.adauga(client)

    def modificaClient(self,idClient,numeNou,CNP):
        '''
        modifica un angajat dupa id
        :param idClient:
        :param numeNou:
        :return:
        '''
        client = Client(idClient, numeNou,CNP)
        self.__clientrepository.modifica(client)

    def stergeClient(self,idClient):
        '''
        sterge un angajat dupa id
        :param idClient: int
        :return:
        '''
        self.__clientrepository.sterge(idClient)
