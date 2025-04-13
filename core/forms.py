from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cuenta

class RegisterForm(UserCreationForm):
    """
    Formulario para registrar un usuario nuevo en la base de datos,
    basado en el modelo Cuenta (heredado de AbstractUser).
    """

    class Meta:
        model = Cuenta
        # 'password1' y 'password2' vienen de UserCreationForm
        # y se usan para manejar la validación de la contraseña.
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña'
        }

    # Opcionalmente puedes agregar widgets para estilizar.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre de usuario',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña',
        })