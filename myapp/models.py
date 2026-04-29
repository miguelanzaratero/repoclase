from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario.username
