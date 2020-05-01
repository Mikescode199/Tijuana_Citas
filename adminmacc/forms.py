from django import forms 
from . import views
from .models import Admin

class Admin_informacion(forms.ModelForm):
    class Meta:
        model = Admin
        fields = [
            'nombre',  
            'apellidos', 
            'numero_telefono',
            'fecha_nacimiento',
            'direccion',
            'lugar_procedencia',
        ]
        labels = {
            'nombre':'Nombre',  
            'apellidos':'Apellidos', 
            'numero_telefono':'Número de celular',
            'fecha_nacimiento':'Fecha de nacimiento',
            'direccion':'Dirección',
            'lugar_procedencia':'Lugar de procedencia',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={}),  
            'apellidos': forms.TextInput(attrs={}), 
            'numero_telefono': forms.TextInput(attrs={}),
            'fecha_nacimiento': forms.TextInput(attrs={}),
            'direccion': forms.TextInput(attrs={}),
            'lugar_procedencia': forms.TextInput(attrs={}),
        }