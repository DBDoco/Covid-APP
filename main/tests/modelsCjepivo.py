from django.test import TestCase
from main.models import *


class Testmodels(TestCase):

    def setUp(self):
        self.cjepivo1 = Cjepivo.objects.create(
            cjepivo_naziv = 'some-cjepivo',
            broj_doza = 'TestBroj'
        )
    
    def test_cjepivo(self):
        self.assertEquals(self.cjepivo1.cjepivo_naziv, "some-cjepivo")