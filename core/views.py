from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Se guarda el usuario en la DB con contraseña hasheada
            login(request, user) # Si quieres que inicie sesión automáticamente tras registrarse
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('logged')   # Redirige a la url que desees
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Si las credenciales coinciden, iniciamos sesión
            login(request, user)
            # Redirecciona a la vista 'logged'
            return redirect('logged')
        else:
            # Credenciales inválidas
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')

    return render(request, 'registration/login.html')

def logged_view(request):
    return render(request, 'registration/logged.html')

def logout_view(request):
    logout(request) # Cierra la sesión
    return render(request, 'registration/logout.html')

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