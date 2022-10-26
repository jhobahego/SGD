from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegistrarForm

def Index(request):
    return render(request, "index.html")


def Login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html', {
            "form": LoginForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'login.html', {
                "form": LoginForm,
                "error": "Usuario o contraseña incorrectos",
            })
        else:
            login(request, usuario)
            return redirect("index")


def Registrar(request):
    if (request.method == 'GET'):
        return render(request, 'registrar.html', {
            "form": RegistrarForm
        })
    else:
        if(request.POST['password1'] != request.POST['password2']):
            return render(request, 'registrar.html', {
                "form": RegistrarForm,
                "error": "las contraseñas no coinciden"
            })

        try:
            usuario = User.objects.create_user(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                username = request.POST['username'],
                password = request.POST['password1']
            )
            usuario.save()
            login(request, usuario)
            return redirect("index")
        except:
            return render(request, 'registrar.html', {
                "form": RegistrarForm,
                "error": "el usuario ya existe"
            })

def Cerrar_sesion(request):
    logout(request)
    return redirect('login')
