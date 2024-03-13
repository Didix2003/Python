import datetime

from Domain.dto import AssemblerDTO
from Domain.inchiriere import Inchiriere

from repository.inchiriereRepository import InchiriereRepository
from repository.repository import Repository


class InchiriereService:
    def __init__(self,inchiriereRepository:Repository,clientRepository: Repository,filmRepository:Repository):
        self.__clientRepository = clientRepository
        self.__inchiriereRepository=inchiriereRepository
        self.__filmRepository=filmRepository


    def adauga(self,idInchiriere,idClient,idFilm,data_inc,data_retur):
        '''
        adauga o inchiriere
        :param idInchiriere: int
        :param idClient: int
        :param idFilm: int
        :param data_inc: datetime
        :param data_retur: datetime
        :return:
        '''
        inc=Inchiriere(idInchiriere,idClient,idFilm,data_inc,data_retur)
        self.__inchiriereRepository.adauga(inc)

    def getInchirierebyid(self,idInchiriere):
        return self.__inchiriereRepository.getById(idInchiriere)
    def getAllInchiriere(self):
        '''
        da lista de inchirieri
        :return: o lista de obiecte de tipul inchirieri
        '''
        return self.__inchiriereRepository.getAll()

    def sterge(self,idInchiriere):
        '''
        sterge din lista dupa id
        :param idInchiriere:int
        :return:
        '''
        self.__inchiriereRepository.sterge(idInchiriere)

    # def getFilmeFrecventa(self):
    #     freq_dict = {}
    #     for e in list(self.getAllInchiriere()):
    #         id = e.getIdFilm()
    #         if id in freq_dict:
    #             freq_dict[id] += 1
    #         else:
    #             freq_dict[id] = 1
    #
    #     return freq_dict

    def maxInchiriereFilmId(self):
        movie_list = []
        max_frequency = 0
        movie_dto = AssemblerDTO.movie_dto(self.getAllInchiriere(),self.__filmRepository)
        for movie in movie_dto.values():
            if movie.frequency > max_frequency:
                movie_list.clear()
                movie_list.append(movie)
                max_frequency = movie.frequency
            elif movie.frequency == max_frequency:
                movie_list.append(movie)
        return movie_list
    @staticmethod
    def listLen(len, firstXPercent):
        if firstXPercent // 100 == 0:
            return (firstXPercent // 100) * len + 1
        else:
            return (firstXPercent // 100) * len

    # def getClientiNrFilmeSiId(self):
    #     freq_dict = {}
    #     for e in list(self.getAllInchiriere()):
    #         id = e.getIdClient()
    #         if id in freq_dict:
    #             freq_dict[id] += 1
    #         else:
    #             freq_dict[id] = 1
    #     return freq_dict

    # def getClientiSiNume(self):
    #     new_list = []
    #     for e in self.__clientRepository.getAll():
    #         new_list.append({'idClient': e.getIdClient(), 'name': e.getNume()})
    #     return new_list

    def sortClientsByName(self):

       client_list=AssemblerDTO.client_dto(self.getAllInchiriere(),self.__clientRepository)
       return sorted(client_list.items(),key=lambda d:d[1].client.getNume())

    # def getClientsAndFilme(self, freq_dict):
    #     new_list = []
    #     for e in freq_dict:
    #         new_list.append({'idClient': e, 'nrFilme': freq_dict[e]})
    #     return new_list

    def sortClientsDupaNRFilme(self):
        client_list = AssemblerDTO.client_dto(self.getAllInchiriere(), self.__clientRepository)
        return sorted(client_list.items(), key=lambda d: d[0])

    def mostActiveClient(self):
       client_list=self.sortClientsDupaNRFilme()
       return client_list[:InchiriereService.listLen(len(client_list),20)]

    # def clientsOrderedByNrOfMovie(self):
    #     new_list = self.sortClientsDupaNRFilme(self.getClientsAndFilme(self.getClientiNrFilmeSiId()))
    #     new_list = new_list[:self.listLen(len(new_list), 100)]
    #     return new_list
    #
    # def clientsOrderedByName(self):
    #     return self.sortClientsByName(self.getClientiSiNume())
    #
    # def mostRentedBook(self):
    #
    #     maxRentBookIds, frequency = self.maxInchiriereFilmId()
    #     return maxRentBookIds, frequency