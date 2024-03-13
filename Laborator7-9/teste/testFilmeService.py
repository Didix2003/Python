from unittest import TestCase

from repository.repository import Repository
from service.filmService import FilmService


class TestServicFilm(TestCase):
    def setUp(self):
        self.repository=Repository()
        self.service=FilmService(self.repository)
        self.service.adaugaFilm(1,'Marianne','o fata','horror')
    def testGetAll(self):
        listafilm=self.service.getAllFilme()
        self.assertTrue(len(listafilm)==1,'lungimea listei clientului trebuie sa fie 1')
    def testgetFilmebyid(self):
        film=self.service.getFilmbyid(1)
        self.assertTrue(film.getIdFilm() == 1, 'Id trebuie sa fie 1')
        self.assertTrue(film.gettitlu() == 'Marianne', 'Id trebuie sa fie 1')
        self.assertTrue(film.getdescriere() == 'o fata', 'Id trebuie sa fie 1')
        self.assertTrue(film.getgen() == 'horror', 'Id trebuie sa fie 1')
    def testadauga(self):
        self.service.adaugaFilm(2, 'Ciocolata','cu lapte', 'satisfacere')
        listafilm=self.service.getAllFilme()
        self.assertTrue(len(listafilm)==2,'lungimea listei clientului trebuie sa fie 1')
        with self.assertRaises(KeyError):
            self.service.adaugaFilm(2, 'Ciocolata','cu lapte', 'satisfacere')
    def testmodifica(self):
        self.service.modificaFilm(1,'Marianne','o fata frumoasa','horror')
        film=self.service.getFilmbyid(1)
        self.assertTrue(film.getIdFilm() == 1, 'Id trebuie sa fie 1')
        self.assertTrue(film.gettitlu() == 'Marianne', 'Id trebuie sa fie 1')
        self.assertTrue(film.getdescriere() == 'o fata frumoasa', 'Id trebuie sa fie 1')
        self.assertTrue(film.getgen() == 'horror', 'Id trebuie sa fie 1')
    def teststerge(self):
        self.service.stergeFilm(1)
        listafilme=self.service.getAllFilme()
        self.assertTrue(len(listafilme)==0)