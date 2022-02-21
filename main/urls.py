from django.urls import path
from . import views
from .views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('studenti', views.StudentList, name ="studenti"),
     path('zaposlenici', views.ZaposlenikList, name ="zaposlenici"),
    path('fakulteti', FakultetList.as_view()),
    path('cjepiva', CjepivoList.as_view()),
]