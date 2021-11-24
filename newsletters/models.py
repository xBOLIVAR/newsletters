from django.db import models
from django.db.models.fields import DateField
from tags.models import Tag 
from usuarios.models import Usuario

class Newsletter(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=600)
    imagen = models.ImageField(upload_to='fotos')
    meta = models.ManyToManyField(Usuario, related_name='newsletters')
    frecuencia = models.CharField(max_length = 100, default="")
    fecha = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='newsletters')

    def __str__(self):
        return self.nombre
