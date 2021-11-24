from django.db import models
from newsletters.models import Newsletter


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    suscribir = models.ManyToManyField(Newsletter, related_name='newsletters')

    def __str__(self):
        return self.nombre