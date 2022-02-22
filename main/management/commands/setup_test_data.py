import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_FAKULTET = 10
NUM_CJEPIVO = 10
NUM_STUDENT = 10
NUM_ZAPOSLENIK= 10


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Fakultet, Cjepivo, Student, Zaposlenik]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_FAKULTET):
            fakultet = FakultetFactory()

        for _ in range(NUM_CJEPIVO):
            cjepivo = CjepivoFactory()

        for _ in range(NUM_STUDENT):
            student = StudentFactory()
        
        for _ in range(NUM_ZAPOSLENIK):
            zaposlenik = ZaposlenikFactory()