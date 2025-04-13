from django import forms
from .models import Cuenta

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña',
            'id': 'confirm'
        })
    )
    class Meta:
        model = Cuenta
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre de usuario',
                'id': 'username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@gmail.com',
                'id': 'email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu contraseña',
                'id': 'password'
            }),
        }
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Email',
            'password': 'Contraseña',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data