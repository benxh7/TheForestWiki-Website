from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .forms import RegisterForm


def registrarse(request):
    if request.method == 'POST':
        print("Se recibió una petición POST")
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo registro
            print("Registro guardado correctamente")
            return redirect('home')  # Redirige a la página de inicio
        else:
            # Imprime los errores del formulario para depuración
            print("Errores en el formulario:", form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})


def login_view(request):
    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'core/home.html')

def error_404(request):
    return render(request, 'core/error_404.html')

def animales(request):
    return render(request, 'core/animales.html')

def enemigos(request):
    return render(request, 'core/enemigos.html')

def mapa(request):
    return render(request, 'core/mapa.html')

def construcciones(request):
    return render(request, 'core/construcciones.html')

def plantas(request):
    return render(request, 'core/plantas.html')

def armas(request):
    return render(request, 'core/armas.html')

def consumibles(request):
    return render(request, 'core/consumibles.html')

def historia(request):
    return render(request, 'core/historia.html')

def foro(request):
    return render(request, 'core/foro.html')

def micuenta(request):
    return render(request, 'core/micuenta.html')