from django.shortcuts import render

# Créa tus vistas en este archivo
# Tambien agregamos un contexto para la plantilla
# y lo pasamos como segundo argumento a render
# La función render recibe el request, la plantilla y el contexto

def home(request):
    return render(request, 'core/home.html')