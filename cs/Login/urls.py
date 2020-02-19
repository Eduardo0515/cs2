from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Login.views import CustonAuthToken
from Login import views
from Login.views_api import LoginViewSet

router = routers.DefaultRouter()
router.register('', LoginViewSet)


urlpatterns = [
    re_path(r'Login/$', CustonAuthToken.as_view()),
    #Hola soy Hugo
    re_path(r'example_Lista2/$',views.ExampleList2.as_view()),    
]
