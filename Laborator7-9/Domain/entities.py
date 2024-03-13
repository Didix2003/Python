class Entity:
    def __init__(self,idEntity):
        self.__idEntity=idEntity

    def getIdEntity(self):
        return self.__idEntity

    def setIdEntity(self,val):
        self.__idEntity=val