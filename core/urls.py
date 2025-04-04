from django.urls import path
from .views import home, error_404

# Aqui debemos añadir las urls de la app core
urlpatterns = [
    path('', home, name='home'),
    path('error_404', error_404, name='error_404'),
]