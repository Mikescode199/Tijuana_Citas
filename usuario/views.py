from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#Llamadas a los modelos
from .models import Usuario, Quejas_segerencias
from adminmacc.models import Admin
from chicas.models import Chica
#Fin de llamadas a los modelos 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.decorators import login_required
#Llamadas al Form
from .forms import NewUser, LoginForm, Usuario_informacion, Quejas_usuario
from adminmacc.forms import Admin_informacion
from chicas.forms import Chica_informacion
# Fin de llamadas al Form


# Función 0000 Registro de usuarios
def registro_user(request):
    message = 'No hay inicio de sesión'
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            print(user, password)
            user = authenticate(username= user, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('usuario:Menu_chicas')
                    message = 'En curso...'
                   
                else:
                    message = 'Usuario no activo'
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

# Función 0001 Datos del usuario
@login_required(login_url='')
def datos_usuario(request):
    if request.method == 'POST':
        form = Usuario_informacion(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
            return redirect('usuario:registro_user')
    else:
            form = Usuario_informacion()
        
    return render(request, 'datos_usuario.html', {'form':form } )

# Función 0002 Crear usuario
class CrearUsuario(generic.FormView):
    template_name = 'singout.html'
    form_class = NewUser
    success_url = reverse_lazy('usuario:formulario_usuario')

    def form_valid(self, form):
        user = form.save()
        return super(CrearUsuario, self).form_valid(form)

# Función 0003 
class Menu_chicas(LoginRequiredMixin,generic.ListView):
    template_name = 'index.html'
    model = Chica

#función 3003 Quejas y sugerencias
@login_required(login_url='')
def quejas(request):
    if request.method == 'POST':
        form = Quejas_usuario(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
            return redirect('usuario:Menu_chicas')
    else:
            form = Quejas_usuario()
        
    return render(request, 'quejas.html', {'form':form } )

#Llevar chica 
class Llevar_chica(LoginRequiredMixin, generic.DetailView):
    template_name = 'llevarchica.html'
    model = Chica

