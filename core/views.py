from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def error_404(request):
    return render(request, 'core/error_404.html')

def login(request):
    return render(request, 'core/login.html')

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