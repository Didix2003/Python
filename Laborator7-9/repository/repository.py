class Repository: #acces la date, retine in memorie lista de clienti si da acces si modifica la lista
    def __init__(self):
        self.__entities={}

    def getAll(self):
        '''
        da lista de entitati
        :return: o lista de obiecte de tipul entitati
        '''
        return list(self.__entities.values()) #pune in lista valorile din dictionar
    def getById(self, idEntity):
        '''
        cauta o entitate dupa id
        :param idEntity:
        :return: o entitate daca exista unul cu id dat sau None in caz contrar
        '''
        if idEntity in self.__entities:
            return  self.__entities[idEntity]
        return None
    def adauga(self, entity):
        '''
        adauga o entitate
        :param entity: obiect de tipul Entities
        :return:
        '''
        if self.getById(entity.getIdEntity()) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat")

        self.__entities[entity.getIdEntity()]=entity
    def modifica(self, newentity):
        '''
        modifica o entitate dupa id
        :param newentity: obiect de tipul entities
        :return:
        '''
        if self.getById(newentity.getIdEntity()) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat ")
        self.__entities[newentity.getIdEntity()]=newentity

    def sterge(self, idEntity):
        '''
        sterge o entitate dupa id
        :param idEntity: string
        :return:
        '''
        if self.getById(idEntity) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat ")
        self.__entities.pop(idEntity)