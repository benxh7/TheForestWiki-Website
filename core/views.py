from django.shortcuts import render

# Vista para la página de inicio
def home(request):
    return render(request, 'core/home.html')

# Vista para manejar el error 404
def error_404(request):
    return render(request, 'core/error_404.html')

# Vista para la página de iniciar sesión
def login(request):
    return render(request, 'core/login.html')

# Vista para la página de animales
def animales(request):
    return render(request, 'core/animales.html')

# Vista para la página de enemigos
def enemigos(request):
    return render(request, 'core/enemigos.html')

# Vista para la página de mapa
def mapa(request):
    return render(request, 'core/mapa.html')

# Vista para la página de construccion
def construcciones(request):
    return render(request, 'core/construcciones.html')

# Vista para la página de plantas
def plantas(request):
    return render(request, 'core/plantas.html')