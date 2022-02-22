from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('index')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, index)

    def test_student_url_is_resolved(self):
        url = reverse('studenti')

        self.assertEquals(resolve(url).func.view_class, StudentList)

    def test_zaposlenik_url_is_resolved(self):
        url = reverse('zaposlenici')

        self.assertEquals(resolve(url).func.view_class, ZaposlenikList)

    def test_fakultet_url_is_resolved(self):
        url = reverse('fakulteti')

        self.assertEquals(resolve(url).func.view_class, FakultetList)

    def test_cjepivo_url_is_resolved(self):
        url = reverse('cjepiva')

        self.assertEquals(resolve(url).func.view_class, CjepivoList)
    
