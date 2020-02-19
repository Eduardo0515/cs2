from rest_framework import viewsets

from Profile.models import ModelCiudad
from Profile.serializer import CiudadSerializers

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = ModelCiudad.objects.all()
    serializer_class = CiudadSerializers