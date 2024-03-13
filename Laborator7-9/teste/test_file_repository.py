import os
import shutil
from unittest import TestCase

from Domain.client import Client
from repository.ReadRepository import ClientiReadRepository
from repository.repository import Repository


class TestFileRepository(TestCase):
    def setUp(self):
        self.file_repository = ClientiReadRepository('clienti.txt')
    def test_add_entity(self):
        self.file_repository.adauga(Client(1, 'Dada', 120))
        self.assertTrue(len(self.file_repository.getAll()) == 1)

    def test_update_entity(self):
        self.file_repository.adauga(Client(1, 'Dada', 120))
        self.file_repository.modifica(Client(1, 'Dad', 120))
        self.assertTrue(Repository.getById(self.file_repository, 1).getIdClient() == 1)
        self.assertTrue(Repository.getById(self.file_repository, 1).getNume() == 'Dad')
        self.assertTrue(Repository.getById(self.file_repository, 1).getCnp() == 120)

    def test_delete_entity(self):
        self.file_repository.adauga(Client(1, 'Dada', 120))
        self.file_repository.sterge(1)
        self.assertTrue(len(self.file_repository.getAll()) == 1)
