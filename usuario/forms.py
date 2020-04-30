from django import forms 
from . import views
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class NewUser(UserCreationForm):
    correo = forms.CharField(max_length=20)

class LoginForm(forms.Form):
    #Con estas lineas de código podemos registrar a un usuario
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class Usuario_informacion(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellidos',
            'fecha_nacimiento',
            'direccion',
            'lugar_nacimiento',
            'estado_civil',
        ]
        labels = {
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'fecha_nacimiento':'Fecha nacimiento',
            'direccion':'Dirección',
            'lugar_nacimiento':'Lugar nacimiento',
            'estado_civil':'Estado civil',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={}),
            'apellidos':forms.TextInput(attrs={}),
            'fecha_nacimiento': forms.TextInput(attrs={}),
            'direccion': forms.TextInput(attrs={}),
            'lugar_nacimiento': forms.TextInput(attrs={}),
            'estado_civil' : forms.TextInput(attrs={}),
        }