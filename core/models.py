from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.db.models.signals import pre_save, post_delete

from django.dispatch import receiver


def generate_username():
    return f"user_{uuid.uuid4().hex[:8]}"


class Cuenta(AbstractUser):
    # Hacemos que el email sea unico para cada cuenta de usuario.
    email = models.EmailField(unique=True)
    imagen = models.ImageField(upload_to='foto_perfil', null=True, default='default/foto-usuario.png')

    def save(self, *args, **kwargs):
        # Si no tiene username manualmente ingresado, generarlo
        if not self.username:
            self.username = generate_username()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

# Borramos la imagen de perfil anterior al guardar una nueva
@receiver(pre_save, sender=Cuenta)
def borrar_imagen_antigua(sender, instance, **kwargs):
    if not instance.pk:
        return  # No hay imagen anterior
    try:
        viejo = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return
    # Si la imagen ha cambiado, borramos la anterior
    if viejo.imagen and viejo.imagen.name != instance.imagen.name:
        viejo.imagen.delete(save=False)

# Señal para borrar la imagen al eliminar la cuenta
@receiver(post_delete, sender=Cuenta)
def borrar_imagen_al_eliminar(sender, instance, **kwargs):
    if instance.imagen:
        instance.imagen.delete(save=False)
