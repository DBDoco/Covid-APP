from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers


app_name = 'main'  

router = routers.DefaultRouter()
router.register(r'fakulteti', views.FakultetViewSet)
router.register(r'studenti', views.StudentViewSet)
router.register(r'zaposlenici', views.ZaposlenikViewSet)
router.register(r'cjepiva', views.CjepivoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('studenti', views.StudentList, name ="studenti"),
    path('zaposlenici', views.ZaposlenikList, name ="zaposlenici"),
    path('fakulteti', FakultetList.as_view()),
    path('cjepiva', CjepivoList.as_view()),
    path('<fakultet>', FakultetStudentList.as_view())
]