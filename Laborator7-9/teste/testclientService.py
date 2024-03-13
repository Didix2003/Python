import unittest
from unittest import TestCase

from Domain.client import Client
from Domain.entities import Entity
from repository.repository import Repository
from service.clientService import ClientService


class TestServiceClient(TestCase):
    def setUp(self):
        self.repository=Repository()
        self.service=ClientService(self.repository)
        self.service.adaugaClient(1,'Ronaldo',757)
    def testGetAll(self):
        listaclient=self.service.getAllClient()
        self.assertTrue(len(listaclient)==1,'lungimea listei clientului trebuie sa fie 0')
    def testgetClientbyid(self):
        client=self.service.getClientbyid(1)
        self.assertTrue(client.getIdClient()==1,'Id trebuie sa fie 1')
        self.assertTrue(client.getNume()=='Ronaldo','Id trebuie sa fie 1')
        self.assertTrue(client.getCnp()==757,'Id trebuie sa fie 1')
    def testadauga(self):
        self.service.adaugaClient(2, 'Maria', 756)
        listaclient=self.service.getAllClient()
        self.assertTrue(len(listaclient)==2,'lungimea listei clientului trebuie sa fie 1')
        with self.assertRaises(KeyError):
            self.service.adaugaClient(2, 'Maria', 756)
    def testmodifica(self):
        self.service.modificaClient(1, 'Ronald', 757)
        client=self.service.getClientbyid(1)
        self.assertTrue(client.getIdClient() == 1, 'Id trebuie sa fie 1')
        self.assertTrue(client.getNume() == 'Ronald', 'Id trebuie sa fie 1')
        self.assertTrue(client.getCnp() == 757, 'Id trebuie sa fie 1')
    def teststerge(self):
        self.service.stergeClient(1)
        listaclienti=self.service.getAllClient()
        self.assertTrue(len(listaclienti)==0)