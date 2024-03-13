from unittest import TestCase

from Domain.entities import Entity


class TestDomainEntity(TestCase):
    def setUp(self):
        self.entity=Entity(1)
    def test_get_id(self):
        self.assertTrue(self.entity.getIdEntity()==1)
    def test_set_id(self):
        self.entity.id=1
        self.assertTrue(self.entity.id==1)