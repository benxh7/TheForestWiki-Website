from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm, EditProfileForm, AvatarForm, ComentarioForm
from .models import Comentario
import requests

def ver_cuentas_api(request):
    try:
        response = requests.get("http://127.0.0.1:8000/cuenta")
        response.raise_for_status()
        cuentas = response.json()

    except request.RequestException as e:
        cuentas = []
        print(f'Error al obtener las cuentas: {e}')
    return render(request, 'core/ver_cuentas_api.html', {'cuentas': cuentas})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Se guarda el usuario en la DB con contraseña hasheada
            login(request, user) # Si quieres que inicie sesión automáticamente tras registrarse
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('home')   # Redirige a la url que desees
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
            return redirect('home')
        else:
            # Credenciales inválidas
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')

    return render(request, 'registration/login.html')

@login_required
def mi_cuenta_view(request):
    # Formulario para cambiar imagen de perfil
    form = AvatarForm(request.POST or None, request.FILES or None, instance=request.user)

    if request.method == 'POST' and form.is_valid():
        form.save() # Guarda la nueva imagen en el campo 'imagen'
        messages.success(request, "Avatar actualizado correctamente.")
        return redirect('micuenta') # Refresca la misma página

    return render(request, 'registration/micuenta.html',{'form': form,})

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

@login_required
def foro_view(request):
    comentarios = Comentario.objects.filter(parent__isnull=True).select_related('usuario').prefetch_related('replies__usuario')

    form = ComentarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        nuevo = form.save(commit=False)
        nuevo.usuario = request.user
        nuevo.save()
        return redirect('foro')

    return render(request, 'core/foro.html', {
        'comentarios': comentarios,
        'form': form,
    })

@login_required
def comment_edit(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    # Permiso para editar
    if comentario.usuario != request.user and not request.user.is_superuser:
        messages.error(request, "No tienes permiso para editar este comentario.")
    else:
        if request.method == 'POST':
            form = ComentarioForm(request.POST, instance=comentario)
            if form.is_valid():
                form.save()
                messages.success(request, "Comentario editado correctamente.")
            else:
                messages.error(request, "Hubo un error al editar el comentario.")
    return redirect('foro')

@login_required
def comment_delete(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if comentario.usuario != request.user and not request.user.is_superuser:
        messages.error(request, "No tienes permiso para borrar este comentario.")
    else:
        comentario.delete()
        messages.success(request, "Comentario borrado.")
    return redirect('foro')