from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
#from Profile.views import CustonAuthToken
from Profile import views
from Login.views import CustonAuthToken


#from rest_framework_swagger.views import get_swagger_view

from Profile.views_api import ProfileViewSet


urlpatterns = [
    re_path(r'Profile/$', CustonAuthToken.as_view()),
    #Hola soy Hugo
    re_path(r'ciudad_Lista/$',views.CiudadList.as_view()),
    re_path(r'genero_Lista/$',views.GeneroList.as_view()),
    re_path(r'ocupacion_Lista/$',views.OcupacionList.as_view()),
    re_path(r'estado_Lista/$',views.EstadoList.as_view()),
    re_path(r'estadoCivil_Lista/$',views.EstadoCivilList.as_view()),
    re_path(r'profile_Lista/$',views.ProfileList.as_view()),    
    #re_path(r'api_profile/$',schema_view),     
]
