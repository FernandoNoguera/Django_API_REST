from rest_framework import serializers
from personajes.models import Personajes,Chelas

class PersonajesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personajes  
        fields = '__all__'

class ChelasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chelas
        fiels = '__all__'
        exclude = ['artesanal']