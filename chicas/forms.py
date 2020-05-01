from django import forms 
from . import views
from .models import Chica

#Formulario para laws chicas 
class Chica_informacion(forms.ModelForm):
    class Meta:
        model = Chica
        fields = [
            'imagen_profile',
            'apodo',
            'nombre', 
            'apellidos',  
            'numero_telefono', 
            'estado_civil',
            'fecha_nacimiento', 
            'direccion', 
            'lugar_procedencia', 
            'sobre_mi',
        ]
        labels = {
            'imagen_profile':'Imagen de perfil',
            'apodo':'Apodo',
            'nombre':'Nombre', 
            'apellidos':'Apellidos',  
            'numero_telefono':'Número de celular', 
            'estado_civil':'Estado cívil',
            'fecha_nacimiento':'Fecha de nacimiento', 
            'direccion':'Dirección', 
            'lugar_procedencia':'Lugar de procedencia', 
            'sobre_mi':'Acerca de mí', 
        }
        widgets = {
            'imagen_profile':forms.TextInput(attrs={'type':'file', 'accept':"image/*"}),
            'apodo':forms.TextInput(attrs={}),
            'nombre':forms.TextInput(attrs={}), 
            'apellidos':forms.TextInput(attrs={}),  
            'numero_telefono':forms.TextInput(attrs={}), 
            'estado_civil': forms.TextInput(attrs={}),
            'fecha_nacimiento':forms.TextInput(attrs={}), 
            'direccion':forms.TextInput(attrs={}), 
            'lugar_procedencia':forms.TextInput(attrs={}), 
            'sobre_mi':forms.TextInput(attrs={}), 
        }

        