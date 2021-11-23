from django.db import models
from django.db.models.fields import DateField
from django.core.validators import MaxValueValidator, MinValueValidator
from tags.models import Tag 

class Newsletter(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=600)
    imagen = models.ImageField(upload_to='fotos')
    meta = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
    frecuencia = models.CharField(max_length = 100, default="")
    fecha = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='newsletters')

    def __str__(self):
        return self.nombre
