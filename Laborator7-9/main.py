from repository import filmRepository
from repository.ReadRepository import ClientiReadRepository, FilmeReadRepository, InchirieriReadRepository
from repository.clientrepository import ClientRepository
from repository.filmRepository import FilmRepository
from repository.inchiriereRepository import InchiriereRepository
from repository.repository import Repository
from service.clientService import ClientService
from service.filmService import FilmService
from service.inchiriereService import InchiriereService
from ui.console import Console, ConsoleFilm
import os

'''
P3. Închiriere filme
Scrieți o aplicație pentru o firmă de închiriere de filme.
Aplicația stochează:
     filme: <id>,<titlu>,<descriere>,<gen>,etc
     clienți: <id>, <nume>, <CNP>,etc
Creați o aplicație care permite:
    F1: gestiunea listei de filme și clienți.
    F2: adaugă, șterge, modifică, lista de filme, lista de clienți
    F3: căutare film, căutare clienți.
    F4: Închiriere/returnare filme
 Rapoarte:
    F5: Clienți cu filme închiriate ordonat dupa: nume, după numărul de filme închiriate
    F6: Cele mai inchiriate filme.
    F7: Primi 20% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)
 Iteratii:
    I1: F1,F2
    I2: F3,F4
    I3: F5,F6,F7
'''

def main():
        clientrepository = ClientiReadRepository("Text/clienti.txt")
        clientService = ClientService(clientrepository)
        console = Console(clientService)
        console.meniu()
        filmRepository = FilmeReadRepository("Text/filme.txt")
        filmService = FilmService(filmRepository)
        inchiriereRepository =  InchirieriReadRepository("Text/inchirieri.txt")
        inchiriereService = InchiriereService(inchiriereRepository, clientrepository,filmRepository)
        console2 = ConsoleFilm(filmService, clientService, inchiriereService)
        console2.meniu2()
main()

