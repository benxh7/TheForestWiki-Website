from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

def generate_username():
    return f"user_{uuid.uuid4().hex[:8]}"

class Cuenta(AbstractUser):
    """
    Modelo personalizado de usuario que hereda de AbstractUser.
    AbstractUser ya incluye username, password, email, first_name y last_name.
    Puedes añadir campos adicionales si lo deseas.
    """

    # Vamos a forzar que el email sea único para cada cuenta.
    email = models.EmailField(unique=True)

    # OPCIONAL: Si deseas forzar que se genere un username automático,
    # podrías redefinir cómo se guarda el usuario.
    # Sin embargo, AbstractUser ya trae 'username',
    # así que aquí podríamos hacer algo adicional si se requiere:
    def save(self, *args, **kwargs):
        # Si no tiene username manualmente ingresado, generarlo
        if not self.username:
            self.username = generate_username()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username