from Domain.filme import Filme
from repository.filmRepository import FilmRepository
from repository.repository import Repository


class FilmService:
    def __init__(self,filmRepository:Repository):
        self.__filmRepository = filmRepository


    def getAllFilme(self):
        '''
        da toata lista de filme
        :return: o lista de obiecte de tipul film
        '''
        return self.__filmRepository.getAll()

    def getFilmbyid(self,idFilm):
        return self.__filmRepository.getById(idFilm)
    def adaugaFilm(self,idFilm,titlu,descriere,gen):
        '''
        adauga un film
        :param idFilm:
        :param titlu:
        :param descriere:
        :param gen:
        :return:
        '''
        film=Filme(idFilm,titlu,descriere,gen)
        self.__filmRepository.adauga(film)

    def modificaFilm(self,idFilm,titluNou,descriereNoua,genNou):
        '''
        modifica un film dupa id
        :param idFilm:
        :param titluNou:
        :param descriereNoua:
        :param genNou:
        :return:
        '''
        film = Filme(idFilm,titluNou,descriereNoua,genNou)
        self.__filmRepository.modifica(film)

    def stergeFilm(self,idFilm):
        '''
        sterge un film
        :param idFilm:
        :return:
        '''
        self.__filmRepository.sterge(idFilm)