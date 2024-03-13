class ClientRepository: #acces la date, retine in memorie lista de clienti si da acces si modifica la lista
    def __init__(self):
        self.__clienti={}

    def getAll(self):
        '''
        da lista de clienti
        :return: o lista de obiecte de tipul client
        '''
        return self.__clienti.values() #pune in lista valorile din dictionar

    def getById(self,idClient):
        '''
        cauta un client dupa id
        :param idClient:
        :return: un client daca exista unul cu id dat sau None in caz contrar
        '''
        if idClient in self.__clienti:
            return  self.__clienti[idClient]
        return None
    def getbynumber(self,CNP):
        var=CNP
        nr=0
        while var:
            nr=nr+1
            var=var//10
        return nr

    def getbycnp(self,CNP):
        nr=self.getbynumber(CNP)
        if  nr!=12:
            raise KeyError("Exista un client cu CNP dat sau ati introdus gresit CNP-ul")
        return None
    def getbycnp2(self,CNP):
        if CNP in self.__clienti:
            return self.__clienti[CNP]
        return None
    def adauga(self,client):
        '''
        adauga un client
        :param client: obiect de tipul Client
        :return:
        '''
        if self.getById(client.getIdClient()):
            raise KeyError("Exista deja un client cu id-ul dat")
        self.getbycnp(client.getCnp())
        if  self.getbycnp2(client.getCnp()):
            raise KeyError("Exista un client cu CNP dat sau ati introdus gresit CNP-ul")

        self.__clienti[client.getIdClient()]=client
    def modifica(self,clientNou):
        '''
        modifica un client dupa id
        :param clientNou: obiect de tipul client
        :return:
        '''
        if self.getById(clientNou.getIdClient()) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat ")
        self.__clienti[clientNou.getIdClient()]=clientNou

    def sterge(self,idClient):
        '''
        sterge un angajat dupa id
        :param idClient: string
        :return:
        '''
        if self.getById(idClient) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat ")
        self.__clienti.pop(idClient)


