from django.shortcuts import render

# Vista para la página de inicio
def home(request):
    return render(request, 'core/home.html')

# Vista para manejar el error 404
def error_404(request):
    return render(request, 'core/error_404.html')