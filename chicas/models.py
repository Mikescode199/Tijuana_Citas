from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chica(models.Model):
    #foto_perfil
    # Fotos
    #El nombre solo lo veran los administradores
    imagen_profile = models.ImageField(upload_to = 'media',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apodo = models.CharField(max_length=60)
    nombre  = models.CharField(max_length=60)
    apellidos  = models.CharField(max_length=60)
    numero_telefono = models.CharField(max_length=60)
    estado_civil =  models.CharField(max_length=60)
    fecha_nacimiento = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    lugar_procedencia = models.CharField(max_length=60)
    sobre_mi = models.TextField()

    def __str__(self):
        return '{}'.format(self.user)
