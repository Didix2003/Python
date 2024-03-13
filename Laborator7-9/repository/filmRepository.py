class FilmRepository: #acces la date, retine in memorie lista de clienti si da acces si modifica la lista
    def __init__(self):
        self.__filme={}

    def getAll(self):
        '''
        da lista de filme
        :return: o lista de obiecte de tipul Film
        '''
        return self.__filme.values()

    def getById2(self, idFilm):
        '''
        cauta un film dupa id
        :param idFilm:
        :return: un film daca exista unul cu id dat sau None in caz contrar
        '''
        if idFilm in self.__filme:
            return self.__filme[idFilm]
        return None
    def adauga(self,film):
        '''
        adauga un film
        :param film: obiect de tipul Film
        :return:
        '''
        if self.getById2(film.getIdFilm()):
            raise KeyError("Exista deja un Film cu id-ul dat")
        self.__filme[film.getIdFilm()] = film

    def modifica(self,FilmNou):
        '''
        modifica un Film dupa id
        :param FilmNou: obiect de tipul film
        :return:
        '''
        if self.getById2(FilmNou.getIdFilm()) is None:
            raise KeyError("Nu exista niciun client cu id-ul dat ")
        self.__filme[FilmNou.getIdFilm()]=FilmNou

    def sterge(self,idFilm):
        '''
        sterge un film dupa id
        :param idfilm: string
        :return:
        '''
        if self.getById2(idFilm) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat ")
        self.__filme.pop(idFilm)
