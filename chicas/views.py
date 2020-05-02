from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Chica, Experiencias_chica
# from .forms import Experiencias_formulario
from usuario.forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views import generic
from django.contrib.auth.decorators import login_required



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
                    return redirect('chicas:perfil_chica')
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

#Funcion 0011 Perfil
@login_required(login_url='/0010') #Con este codigo limitamos a los usuarios que no tienen un perfil
def perfil_chica(request):
    model = Chica.objects.filter(user = request.user)
    context ={

            'model':model
        }
    return render(request, 'chicas/miperfil.html', context)

#Función 0012
@login_required(login_url='/0010') #Con este codigo limitamos a los usuarios que no tienen un perfil
def historial_chica(request):
    context ={

        }
    return render(request, 'chicas/historial.html', context)



#funcion 0013 TRABAJANDO
# def bitacora_chica(request):
#     if request.method == 'POST':
#         form = Experiencias_formulario(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             form.save()
#             return redirect('chicas:perfil_chica')
#     else:
#             form = Experiencias_formulario()
        
#     return render(request, 'chica/experiencias.html', {'form':form } )



