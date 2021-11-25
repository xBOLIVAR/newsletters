from django.db import models
from tags.models import Tag 
from django.contrib.auth.models import User

class Newsletter(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=600)
    imagen = models.ImageField(upload_to='fotos', null=True)
    meta = models.IntegerField(default=0)
    frecuencia = models.CharField(max_length = 100, default="")
    fecha = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='newsletters')
    votos = models.ManyToManyField(User, related_name='newsletters')
    suscrito = models.ManyToManyField(User , related_name='news')
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
