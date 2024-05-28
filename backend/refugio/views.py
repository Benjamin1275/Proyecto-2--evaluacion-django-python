from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import RefugioForm
from .models import Refugio
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('refugio')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def listar_refugios(request):
    refugios = refugio.objects.all()
    return render(request, 'refugio.html', {'refugios': refugios})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('refugio')

def agregarRefugio(request):
    if request.method == 'GET':
        return render(request, 'agregarRefugio.html', {
            'form': RefugioForm})
    else:
        try:
            form = RefugioForm(request.POST)
            newRefugio = form.save(commit=False)
            newRefugio.user = request.user
            newRefugio.save()
            return redirect('refugio')
        except ValueError:
            return render(request, 'agregarRefugio.html', {
                'form': RefugioForm,
                'error': 'Error al guardar el refugio'
            })
def refugio(request):
    return render(request, 'refugio.html')

def info_refugio(request, id_refugio):
    if request.method == 'GET':
        perro = get_object_or_404(Refugio, pk=id_refugio)
        form = RefugioForm(instance=refugio)
        return render(request, 'info_refugio.html', {'refugi': refugio, 'form': form})
    else:
        try:
            perro = get_object_or_404(Refugio, pk=id_refugio)
            form = RefugioForm(request.POST, instance=refugio)
            form.save()
            return redirect('refugio')
        except ValueError:
            return render(request, 'info_refugio.html', {
                'refugio': refugio,
                'form': form,
                'error': 'Error al guardar el refugio'
            })

    
def refugio_delete(request, id_refugio):
    refugio = get_object_or_404(Refugio, pk=id_refugio, user=request.user)
    #if request.method == 'POST':
    refugio.delete()
    return redirect('refugio')