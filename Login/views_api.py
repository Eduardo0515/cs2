from rest_framework import viewsets

from Login.models import Example2
from Login.serializer import Example2Serializers

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Example2.objects.all()
    serializer_class = Example2Serializers