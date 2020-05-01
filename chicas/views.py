from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#Llamadas a los modelos
from .models import Chica
#Fin de llamadas a los modelos 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.decorators import login_required
#Llamadas al Form
from usuario.forms import LoginForm



#Funcion 0010 Inicio de sesión chica
def registro_chicas(request):
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
    return render(request, 'chicas/registrochicas.html', context)