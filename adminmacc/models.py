from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    #foto_perfil
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre  = models.CharField(max_length=60)
    apellidos  = models.CharField(max_length=60)
    numero_telefono = models.CharField(max_length=60, blank=True)
    fecha_nacimiento = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    lugar_procedencia = models.CharField(max_length=60)

    def __str__(self):
        return '{}'.format(self.user)