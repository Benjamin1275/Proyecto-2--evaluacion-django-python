from rest_framework import serializers
from ..API.models import *

#class GeneroSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Genero
#        fields = ('idGenero','codigo', 'nombre')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('idRegion','codigo', 'nombre')

class RegionSerializerPutDelRead(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('codigo', 'nombre')        

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ('idProvincia','codigo', 'nombre','region')

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ('idComuna','codigo', 'nombre','provincia')
        
class PerroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perro
        fields = ('idPerro','nombre', 'raza','edad','descripcion','fecha_registro','user') #id_refugio




