from django.test import TestCase
from main.models import *


class Testmodels(TestCase):

    def setUp(self):
        self.fakultet1 = Fakultet.objects.create(
            fakultet_naziv = 'some-fakultet',
            fakultet_adresa = 'TestAdress',
            fakultet_kontakt_broj = 'TestNumber',
            fakultet_email_referade = 'TestEmail',
            fakultet_website = 'TestWebsite'
        )

    def test_fakultet(self):
        self.assertEquals(self.fakultet1.fakultet_naziv, "some-fakultet")