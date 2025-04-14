from django.urls import path, include
from .views import home, error_404, login_view, register_view, logout_view, mi_cuenta_view, mi_cuenta_editar_view, cambiar_contraseña_view, animales, enemigos, mapa, construcciones, plantas, armas, consumibles, historia, foro

# Aqui debemos añadir las urls de la app core
urlpatterns = [
    path('register/', register_view, name='registrarse'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('micuenta/', mi_cuenta_view, name='micuenta'),
    path('micuenta_editar/', mi_cuenta_editar_view, name='micuenta_editar'),
    path('cambiar_contraseña/', cambiar_contraseña_view, name='cambiar_contraseña'),
    path('', home, name='home'),
    path('error_404', error_404, name='error_404'),
    path('animales', animales, name='animales'),
    path('enemigos', enemigos, name='enemigos'),
    path('mapa', mapa, name='mapa'),
    path('construcciones', construcciones, name='construcciones'),
    path('plantas', plantas, name='plantas'),
    path('armas', armas, name='armas'),
    path('consumibles', consumibles, name='consumibles'),
    path('historia', historia, name='historia'),
    path('foro', foro, name='foro'),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación
]