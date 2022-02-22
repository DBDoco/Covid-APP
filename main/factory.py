## factory.py
import random
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class FakultetFactory(DjangoModelFactory):
    class Meta:
        model = Fakultet

    fakultet_naziv = factory.Faker("first_name")
    fakultet_adresa = factory.Faker("address")
    fakultet_kontakt_broj = factory.Faker("phone_number")
    fakultet_email_referade = factory.Faker("email")
    fakultet_website = factory.Faker("url")
    

class CjepivoFactory(DjangoModelFactory):
    class Meta:
        model = Cjepivo

    cjepivo_naziv = factory.Faker("first_name")
    broj_doza = factory.Faker('pyint', min_value=1, max_value=3)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    student_ime = factory.Faker("first_name")
    student_prezime = factory.Faker("last_name")
    student_jmbag = factory.Faker('pyint', min_value=1000000000, max_value=9999999999)
    student_adresa = factory.Faker("address")
    student_email = factory.Faker("email")
    student_fakultet = factory.SubFactory(FakultetFactory)
    student_cijepljen = factory.Faker("pybool")
    student_cjepivo = factory.SubFactory(CjepivoFactory)
    student_datum_cijepljenja = factory.Faker("date_time")
    student_datum_isteka_potvrde = factory.Faker("date_time")
    student_prebolio_covid = factory.Faker("pybool")


class ZaposlenikFactory(DjangoModelFactory):
    class Meta:
        model = Zaposlenik

    zaposlenik_ime = factory.Faker("first_name")
    zaposlenik_prezime = factory.Faker("last_name")
    zaposlenik_oib = factory.Faker('pyint', min_value=10000000000, max_value=99999999999)
    zaposlenik_adresa = factory.Faker("address")
    zaposlenik_email = factory.Faker("email")
    zaposlenik_fakultet = factory.SubFactory(FakultetFactory)
    zaposlenik_cijepljen = factory.Faker("pybool")
    zaposlenik_cjepivo = factory.SubFactory(CjepivoFactory)
    zaposlenik_datum_cijepljenja = factory.Faker("date_time")
    zaposlenik_datum_isteka_potvrde = factory.Faker("date_time")
    zaposlenik_prebolio_covid = factory.Faker("pybool")    
