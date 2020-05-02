from django.urls import path, include
from chicas import views


# Urls de nuestro sitio

app_name  = 'chicas'
urlpatterns = [
    path('0010/', views.registro_chicas, name='registro_chicas'),
    path('0011/', views.perfil_chica, name='perfil_chica'),
    path('0012/', views.historial_chica, name='historial_chica'),
    # path('0013/', views.bitacora_chica, name='bitacora_chica'),

]