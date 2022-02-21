from rest_framework import serializers
from main.models import *

class FakultetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fakultet
        fields = ('fakultet_naziv', 'fakultet_adresa','fakultet_kontakt_broj', 'fakultet_email_referade', 'fakultet_website')

class CjepivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cjepivo
        fields = ('cjepivo_naziv', 'broj_doza')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_ime', 'student_prezime', 'student_jmbag', 'student_adresa', 'student_email', 'student_fakultet', 'student_cijepljen', 'student_cjepivo', 'student_datum_cijepljenja', 'student_datum_isteka_potvrde', 'student_prebolio_covid')

class ZaposlenikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zaposlenik
        fields = ('zaposlenik_ime', 'zaposlenik_prezime', 'zaposlenik_oib', 'zaposlenik_adresa', 'zaposlenik_email', 'zaposlenik_fakultet', 'zaposlenik_cijepljen', 'zaposlenik_cjepivo', 'zaposlenik_datum_cijepljenja', 'zaposlenik_datum_isteka_potvrde', 'zaposlenik_prebolio_covid')