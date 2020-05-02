from django.urls import path, include
from adminmacc import views

app_name  = 'adminmacc'
urlpatterns = [
    path('0004', views.control_empleado, name='control_empleado'), #Interface del admin
    path('0005/', views.Nuestras_chicas.as_view(), name="Nuestras_chicas"),
    path('0006/<int:pk>', views.Eliminar_chica.as_view(), name='Eliminar_chica'),
    path('0007/<int:pk>', views.Ver_chica.as_view(), name='Ver_chica'),
    path('0008/<int:pk>', views.Editar_chica.as_view(), name='Editar_chica'),
    path('0009/', views.Perfil_admin.as_view(), name='Perfil_admin'),
    path('1009/', views.Crearchica.as_view(), name='Crearchica'),
    # path('2009/', views.datos_chica, name='datos_chica'),en reparación
    path('3009', views.registro_admin, name='registro_admin'),
    
]
