from unittest import TestCase

from Domain.client import Client
from Domain.filme import Filme


class TestDomainClient(TestCase):
    def setUp(self):
        self.film=Filme(1, 'Titlu', 'Descriere','Gen')

    def test_idfilm(self):
        self.assertTrue(self.film.getIdFilm() == 1)

    def test_titlu(self):
        self.assertTrue(self.film.gettitlu() == 'Titlu')

    def test_descriere(self):
        self.assertTrue(self.film.getdescriere() == 'Descriere')

    def test_gen(self):
        self.assertTrue(self.film.getgen() == 'Gen')
    def test_set_idfilm(self):
        self.film.id=2
        self.assertTrue(self.film.id == 2)

    def test_set_titlufilm(self):
        self.film.nume = 'Titlu2'
        self.assertTrue(self.film.nume == 'Titlu2')

    def test_set_descriere(self):
        self.film.des ='Descriere'
        self.assertTrue(self.film.des == 'Descriere')

    def test_set_gen(self):
        self.film.gen ='Gen'
        self.assertTrue(self.film.gen == 'Gen')