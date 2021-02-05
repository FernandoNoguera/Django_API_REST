from django.shortcuts import render

from rest_framework import viewsets
from personajes.models import Personajes,Chelas
from personajes.serializers import PersonajesSerializers, ChelasSerializers

class PersonajesViewSets(viewsets.ModelViewSet):
    queryset = Personajes.objects.all() #consulta todo en esa base de datos
    #queryset = Personajes.objects.all().create() #crea un objeto en la base de datos
    #queryset = Personajes.objects.all().filter() #fitra un objeto en la base de datos
    serializer_class = PersonajesSerializers

class ChelasViewSet(viewsets.ModelViewSet):
    serializer_class = ChelasSerializers
    queryset = Chelas.objects.all()
