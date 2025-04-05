from django.urls import path
from .views import home, error_404, login, animales, enemigos, mapa, construcciones, plantas

# Aqui debemos añadir las urls de la app core
urlpatterns = [
    path('', home, name='home'),
    path('error_404', error_404, name='error_404'),
    path('login', login, name='login'),
    path('animales', animales, name='animales'),
    path('enemigos', enemigos, name='enemigos'),
    path('mapa', mapa, name='mapa'),
    path('construcciones', construcciones, name='construcciones'),
    path('plantas', plantas, name='plantas'),
]