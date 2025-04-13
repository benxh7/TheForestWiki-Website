from django.db import models
import uuid

# Create your models here.

# Generamos un nombre de usuario automaticamente
def generate_username():
    return f"user_{uuid.uuid4().hex[:8]}"

class Cuenta(models.Model):
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    username = models.CharField(
        max_length=50,
        unique=True,
        default=generate_username,
        verbose_name="Nombre de usuario"
    )
    password = models.CharField(max_length=100, verbose_name="Contraseña")

    def __str__(self):
        return f"Registro: {self.email}"