from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    # Foto de perfil
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    fecha_nacimiento = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    lugar_nacimiento = models.CharField(max_length=60)
    estado_civil = models.CharField(max_length=60)
    
    def __str__(self):
        return '{}'.format(self.user)


