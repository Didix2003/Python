from unittest import TestCase

from Domain.client import Client


class TestDomainClient(TestCase):
    def setUp(self):
        self.client=Client(1,'Name',1234)

    def test_idclient(self):
        self.assertTrue(self.client.getIdClient()==1)

    def test_name(self):
        self.assertTrue(self.client.getNume()=='Name')

    def test_cnp(self):
        self.assertTrue(self.client.getCnp()==1234)

    def test_set_idclient(self):
        self.client.id=2
        self.assertTrue(self.client.id==2)

    def test_set_numeclient(self):
        self.client.nume = 'Nume2'
        self.assertTrue(self.client.nume == 'Nume2')

    def test_set_cnpclient(self):
        self.client.cnp =11
        self.assertTrue(self.client.cnp == 11)