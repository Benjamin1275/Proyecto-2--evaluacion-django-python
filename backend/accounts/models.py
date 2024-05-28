from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    rut = models.CharField(max_length=20, unique=True, help_text="Ingrese el RUT sin puntos ni guión")

    def validate_unique(self, exclude=None):
        exclude = ('rut',) if exclude is None else tuple(exclude) + ('rut',)
        super().validate_unique(exclude=exclude)
        
    def __str__(self):
        if self.username == 'admin':
            return 'Super usuario admin'
        return f'Usuario: {self.username} - Rut: {str(self.rut)}'