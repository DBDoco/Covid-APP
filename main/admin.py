from django.contrib import admin
from .models import *

model_list = [Cjepivo, Student, Zaposlenik, Fakultet]
admin.site.register(model_list)