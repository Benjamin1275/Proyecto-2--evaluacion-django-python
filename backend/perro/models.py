from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


# Create your models here.
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')
    
    def __str__(self):
        return self.nombre + ', Region ' + self.id_region.nombre

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, db_column='id_provincia')
    
    def __str__(self):
        return self.nombre
    

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    # id_refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE) Agregar despues de crear el refugio


