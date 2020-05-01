from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#Llamadas a los modelos
from .models import Admin
from chicas.models import Chica
#Fin de llamadas a los modelos 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.decorators import login_required
#Llamadas al Form
from chicas.forms import Chica_informacion

# Fin de llamadas al Form


# Create your views here.

# Función 0004 
def control_empleado(request):
    context ={
        
    }
    return render(request, 'admin/dashboard.html', context)

#Funcion 0005 Nuetras chicas
class Nuestras_chicas(generic.ListView):
    template_name = 'admin/nuestraschicas.html'
    model = Chica


#Funcion 0006 Eliminar Nuetras chicas
class Eliminar_chica(LoginRequiredMixin, generic.DeleteView):
    template_name = 'admin/eliminarchica.html'
    model = Chica
    success_url = reverse_lazy('adminmacc:Nuestras_chicas')


#Funcion 0007 Ver Nuetras chicas
class Ver_chica(LoginRequiredMixin, generic.DetailView):
    template_name = 'admin/verchica.html'
    model = Chica


#Funcion 0008 Editar Nuetras chicas
class Editar_chica(LoginRequiredMixin, generic.UpdateView):
    template_name = 'admin/editarchica.html'
    model = Chica
    form_class = Chica_informacion
    success_url = reverse_lazy('adminmacc:Nuestras_chicas')

#Clase 0009 Perfil
class Perfil_admin(LoginRequiredMixin, generic.ListView):
    template_name = 'admin/perfiladmin.html'
    model = Admin

    def get_queryset(self, *args, **kwargs):
        queryset = Admin.objects.filter(user = self.request.user )
        return queryset
