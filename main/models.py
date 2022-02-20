from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, URLField
from django.db.models.fields.related import OneToOneField
from django.utils import timezone

# Create your models here.

class Fakultet (models.Model):
    fakultet_naziv=models.CharField(max_length=30)
    fakultet_adresa=models.CharField(max_length=30)
    fakultet_kontakt_broj=models.CharField(max_length=20)
    fakultet_email_referade=models.EmailField(default='')
    fakultet_website=models.URLField()

    def __str__(self):
        return self.fakultet_naziv


class Cjepivo (models.Model):
    cjepivo_naziv=models.CharField(max_length=30)
    broj_doza=models.CharField(max_length=1)

    def __str__(self):
        return self.cjepivo_naziv


class Student (models.Model):
    student_ime=models.CharField(max_length=30)
    student_prezime=models.CharField(max_length=30)
    student_jmbag=models.CharField(max_length=10, primary_key=True)
    student_adresa=models.CharField(max_length=30, default='')
    student_email=models.EmailField(default='')
    student_fakultet=models.ForeignKey(Fakultet, on_delete=models.CASCADE, default='')
    student_cijepljen=models.BooleanField(default=True)
    student_cjepivo=models.ForeignKey(Cjepivo, on_delete=models.CASCADE, default='')
    student_datum_cijepljenja=models.DateTimeField(default=timezone.now)
    student_datum_isteka_potvrde=models.DateTimeField(default=timezone.now)
    student_prebolio_covid=models.BooleanField(default=False)

    def __str__(self):
        return self.student_jmbag


class Zaposlenik (models.Model):
    zaposlenik_ime=models.CharField(max_length=30)
    zaposlenik_prezime=models.CharField(max_length=30)
    zaposlenik_oib=models.CharField(max_length=11, primary_key=True)
    zaposlenik_adresa=models.CharField(max_length=30, default='')
    zaposlenik_email=models.EmailField(default='')
    zaposlenik_fakultet=models.ForeignKey(Fakultet, on_delete=models.CASCADE, default='')
    zaposlenik_cijepljen=models.BooleanField(default=True)
    zaposlenik_cjepivo=models.ForeignKey(Cjepivo, on_delete=models.CASCADE, default='')
    zaposlenik_datum_cijepljenja=models.DateTimeField(default=timezone.now)
    zaposlenik_datum_isteka_potvrde=models.DateTimeField(default=timezone.now)
    zaposlenik_prebolio_covid=models.BooleanField(default=False)

    def __str__(self):
        return self.zaposlenik_oib