from django.urls import path
from .views import home, error_404, login, registrarse, animales, enemigos, mapa, construcciones, plantas, armas, consumibles, historia, foro, micuenta

# Aqui debemos añadir las urls de la app core
urlpatterns = [
    path('', home, name='home'),
    path('error_404', error_404, name='error_404'),
    path('login', login, name='login'),
    path('registrarse', registrarse, name='registrarse'),
    path('animales', animales, name='animales'),
    path('enemigos', enemigos, name='enemigos'),
    path('mapa', mapa, name='mapa'),
    path('construcciones', construcciones, name='construcciones'),
    path('plantas', plantas, name='plantas'),
    path('armas', armas, name='armas'),
    path('consumibles', consumibles, name='consumibles'),
    path('historia', historia, name='historia'),
    path('foro', foro, name='foro'),
    path('micuenta', micuenta, name='micuenta'),
]