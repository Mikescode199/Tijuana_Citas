from django.urls import path, include
from usuario import views


# Urls de nuestro sitio

app_name  = 'usuario'
urlpatterns = [
    path('', views.registro_user, name='registro_user'), #Registro de usuario
    path('0001/', views.datos_usuario, name='datos_usuario'), #Datos del usuario
    path('0002/', views.CrearUsuario.as_view(), name="CrearUsuario"),#CRear usuario
    path('0003/', views.Menu_chicas.as_view(), name="Menu_chicas"),
    path('3003/', views.quejas, name="quejas"),
    path('4003/<int:pk>', views.Llevar_chica.as_view(), name='Llevar_chica'),
]
