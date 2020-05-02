from django import forms 
from . import views
from .models import Chica, Experiencias_chica

#Formulario para laws chicas 
class Chica_informacion(forms.ModelForm):
    class Meta:
        model = Chica
        fields = [
            'user',
            'imagen_profile',
            'imagen_segunda',
            'imagen_tercera',
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
            'user':'Asignar Chica que acabas de crear',
            'imagen_profile':'Imagen de perfil',
            'imagen_segunda':'Segunda imagen',
            'imagen_tercera':'Tercer imagen',
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
            'imagen_profile':forms.TextInput(attrs={'type':'file', 'accept':'image/*', 'class':'informacion_chica'}),
            'imagen_segunda':forms.TextInput(attrs={'type':'file', 'accept':'image/*', 'class':'informacion_chica'}),
            'imagen_tercera':forms.TextInput(attrs={'type':'file', 'accept':'image/*', 'class':'informacion_chica'}),
            'apodo':forms.TextInput(attrs={'class':'informacion_chica'}),
            'nombre':forms.TextInput(attrs={'class':'informacion_chica'}), 
            'apellidos':forms.TextInput(attrs={'class':'informacion_chica'}),  
            'numero_telefono':forms.TextInput(attrs={'class':'informacion_chica'}), 
            'estado_civil': forms.TextInput(attrs={'class':'informacion_chica'}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'informacion_chica'}), 
            'direccion':forms.TextInput(attrs={'class':'informacion_chica'}), 
            'lugar_procedencia':forms.TextInput(attrs={'class':'informacion_chica'}), 
            'sobre_mi':forms.TextInput(attrs={'class':'informacion_chica'}), 
        }

class Experiencias_formulario(forms.ModelForm):
    class Meta:
            model = Experiencias_chica
            fields = [
                'nombre_cliente',
                'direccion_servicio',
                'tarifa',
                'bitacora_servicio',
            ]

            labels = {
                'nombre_cliente':'Nombre del cliente',
                'direccion_servicio':'Dirección de servicio',
                'tarifa':'Tarifa',
                'bitacora_servicio':'Bitacora',
            }
            widgets = {
                'nombre_cliente':forms.TextInput(attrs={'class':'informacion_chica'}),
                'direccion_servicio':forms.TextInput(attrs={'class':'informacion_chica'}),
                'tarifa':forms.TextInput(attrs={'class':'informacion_chica'}),
                'bitacora_servicio':forms.TextInput(attrs={'class':'informacion_chica'}),
            }