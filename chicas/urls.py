from django.urls import path, include
from chicas import views


# Urls de nuestro sitio

app_name  = 'chicas'
urlpatterns = [
    path('0010/', views.registro_chicas, name='registro_chicas'),

]