from dataclasses import dataclass

from Domain.client import Client
from Domain.filme import Filme
from repository.repository import Repository


class AssemblerDTO:
    @staticmethod
    def movie_dto(rent_list, movie_repository: Repository):
        movie_list = {}
        for rent in rent_list:
            if rent.getIdFilm() in movie_list:
                movie_list[rent.getIdFilm()].frequency = movie_list[rent.getIdFilm()].frequency + 1
            else:
                movie_list[rent.getIdFilm()] = MovieDTO(movie_repository.getById(rent.getIdFilm()), 1)
        return movie_list

    @staticmethod
    def client_dto(rent_list, client_repository: Repository):
        client_list = {}
        for rent in rent_list:
            if rent.getIdClient() in client_list:
                client_list[rent.getIdClient()].frequency = client_list[rent.getIdClient()].frequency + 1
            else:
                client_list[rent.getIdClient()] = ClientDTO(client_repository.getById(rent.getIdClient()), 1)
        return client_list


@dataclass
class MovieDTO:
    __movie: Filme
    __frequency: int

    @property
    def frequency(self) -> int:
        return self.__frequency

    @frequency.setter
    def frequency(self, value: int) -> None:
        self.__frequency = value

    @property
    def movie(self):
        return self.__movie

    def __str__(self):
        return f'Id Film: {self.movie.getIdFilm()}\n' \
               f'Titlu: {self.movie.gettitlu()}\n' \
               f'Descriere: {self.movie.getdescriere()}\n' \
               f'Gen: {self.movie.getgen()}\n' \
               f'Acest film a fost inchiriat de {self.frequency} ori\n'


@dataclass
class ClientDTO:
    __client: Client
    __frequency: int

    @property
    def frequency(self) -> int:
        return self.__frequency

    @frequency.setter
    def frequency(self, value: int) -> None:
        self.__frequency = value

    @property
    def client(self):
        return self.__client

    def __str__(self):
        return f'Id Client: {self.client.getIdClient()}\n' \
               f'Nume Client: {self.client.getNume()}\n' \
               f'Cnp Client: {self.client.getCnp()}\n' \
               f'Numarul de filme inchiriate: {self.frequency}\n'