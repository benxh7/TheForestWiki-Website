from django.urls import path
from .views import home, error_404, login, animales

# Aqui debemos añadir las urls de la app core
urlpatterns = [
    path('', home, name='home'),
    path('error_404', error_404, name='error_404'),
    path('login', login, name='login'),
    path('animales', animales, name='animales'),
]