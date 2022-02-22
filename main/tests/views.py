from django.test import TestCase, Client
from django.urls import reverse
from main.models import *
from main.views import FakultetList, ZaposlenikList


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('/index')
        self.fakultet_q_url = reverse('fakultet_q', args=['some-fakultet'])

        self.fakultet1 = FakultetList.objects.create(
            fakultet_naziv = 'some-fakultet',
            fakultet_adresa = 'TestAdress',
            fakultet_kontakt_broj = 'TestNumber',
            fakultet_email_referade = 'TestEmail',
            fakultet_website = 'TestWebsite'
        )
            
            
    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_zaposlenik_GET(self):
        client = Client()

        response = client.get(self.zaposlenik_q_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/main/fakultet_list.html') 
