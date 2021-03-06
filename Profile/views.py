from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#Importar modelo
from Profile.models import ModelCiudad
from Profile.models import ModelGenero
from Profile.models import ModelOcupacion
from Profile.models import ModelEstado
from Profile.models import ModelEstadoCivil
from Profile.models import ModelProfile

#Importar Serializer
from Profile.serializer import CiudadSerializers
from Profile.serializer import GeneroSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import EstadoCivilSerializers
from Profile.serializer import ProfileSerializers

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CiudadList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelCiudad.objects.filter(delete = False)
        #queryset
        #many = True Si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelGenero.objects.filter(delete = False)
        #queryset
        #many = True Si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelOcupacion.objects.filter(delete = False)
        #queryset
        #many = True Si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelEstado.objects.filter(delete = False)
        #queryset
        #many = True Si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelEstadoCivil.objects.filter(delete = False)
        #queryset
        #many = True Si aplica si retorno multiples objetos
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ModelProfile.objects.filter(delete = False)
        #queryset
        #many = True Si aplica si retorno multiples objetos
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)