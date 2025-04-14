from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm, EditProfileForm

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

        # Validación de campos vacíos
        if not username:
            messages.error(request, "El campo 'Nombre de Usuario' es obligatorio.")
            return
        if not password:
            messages.error(request, "El campo 'Contraseña' es obligatorio.")
            return

        # Autenticación del usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Si las credenciales coinciden, iniciamos sesión
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('logged')
        else:
            # Credenciales inválidas
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')

    return render(request, 'registration/login.html')

@login_required
def mi_cuenta_view(request):
    return render(request, 'registration/micuenta.html')

@login_required
def mi_cuenta_editar_view(request):
    user = request.user # El usuario logueado actual
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil se ha actualizado correctamente!')
            return redirect('micuenta') # O la ruta que definas
        else:
            messages.error(request, 'Por favor corrige los errores señalados.')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'registration/micuenta_editar.html', {'form': form})

@login_required
def cambiar_contraseña_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Actualiza la contraseña
            # Mantener la sesión iniciada después del cambio de contraseña:
            update_session_auth_hash(request, user)
            messages.success(request, '¡Tu contraseña se ha cambiado exitosamente!')
            return redirect('micuenta')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'registration/cambiar_contraseña.html', {'form': form})

def logout_view(request):
    logout(request) # Cierra la sesión
    return redirect('core/home')

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