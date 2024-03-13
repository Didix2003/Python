import unittest
from unittest import TestCase

from Domain.client import Client
from Domain.entities import Entity
from repository.repository import Repository


class TestRepository(TestCase):
    def setUp(self):
        self.repository=Repository()
        self.repository.adauga(Client(1,'Ronaldo',757))
    def testGetAll(self):
        listaclient=self.repository.getAll()
        self.assertTrue(len(listaclient)==1,'lungimea listei clientului trebuie sa fie 0')
    def testgetbyid(self):
        client=self.repository.getById(1)
        self.assertTrue(client.getIdClient()==1,'Id trebuie sa fie 1')
        self.assertTrue(client.getNume()=='Ronaldo','Id trebuie sa fie 1')
        self.assertTrue(client.getCnp()==757,'Id trebuie sa fie 1')
    def testadauga(self):
        self.repository.adauga(Client(2, 'Maria', 756))
        listaclient=self.repository.getAll()
        self.assertTrue(len(listaclient)==2,'lungimea listei clientului trebuie sa fie 1')
        with self.assertRaises(KeyError):
            self.repository.adauga(Client(2, 'Maria', 756))
    def testmodifica(self):
        self.repository.modifica(Client(1,'Ronald',757))
        client=self.repository.getById(1)
        self.assertTrue(client.getIdClient() == 1, 'Id trebuie sa fie 1')
        self.assertTrue(client.getNume() == 'Ronald', 'Id trebuie sa fie 1')
        self.assertTrue(client.getCnp() == 757, 'Id trebuie sa fie 1')
    def teststerge(self):
        self.repository.sterge(1)
        listaclienti=self.repository.getAll()
        self.assertTrue(len(listaclienti)==0)