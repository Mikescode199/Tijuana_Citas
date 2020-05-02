from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.files import File 
#Llamadas a los modelos
from .models import Admin
from chicas.models import Chica
from usuario.models import Usuario
#Fin de llamadas a los modelos 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.decorators import login_required
#Llamadas al Form
from chicas.forms import Chica_informacion
from usuario.forms import NewUser, LoginForm

# Fin de llamadas al Form


# Create your views here.

# Función 0004 
@login_required(login_url='/3009') #Con este codigo limitamos a los usuarios que no tienen un perfil
def control_empleado(request):
    chicas_count = Chica.objects.count()
    usuarios_count = Usuario.objects.count()
    admins_count = Admin.objects.count()
    context = {
        'chicas_count': chicas_count,
        'usuarios_count': usuarios_count,
        'admins_count': admins_count
    }
    return render(request, 'admin/dashboard.html', context)

#Funcion 0005 Nuetras chicas
class Nuestras_chicas(LoginRequiredMixin, generic.ListView):
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

#Clase 1009 Perfil
class Crearchica(LoginRequiredMixin, generic.FormView):
    template_name = 'singout.html'
    form_class = NewUser
    success_url = reverse_lazy('adminmacc:Nuestras_chicas')

    def form_valid(self, form):
        user = form.save()
        return super(Crearchica, self).form_valid(form)


#Clase 2009 Perfil
# def datos_chica(request):
#     if request.method == 'POST':
#         form = Chica_informacion(request.POST)
#         if form.is_valid():
#             return redirect('adminmacc:Nuestras_chicas')
#     else:
#             form = Chica_informacion(request.POST)
        
#     return render(request, 'admin/datoschica.html', {'form':form } )

#Función 3009  registro_admin
def registro_admin(request): 
    message = 'Admin MACC'
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            print(user, password)
            user = authenticate(username= user, password = password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('adminmacc:control_empleado')
                    message = 'user Loged'
                   
                else:
                    message = '  Sólo para administradores '
            else:
                message = 'Usuario o contraseña incorrecta'
        context ={
        'form': form, 
        'message': message
        }
        
    context ={
        'form': form,
        'message': message

    }
    return render(request, 'login.html', context)
