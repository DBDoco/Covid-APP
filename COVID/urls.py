from django.contrib import admin
from django.urls import path, include #importamo include

urlpatterns = [
    path('', include('main.urls')), #dodajemo urls
    path('admin/', admin.site.urls),
]