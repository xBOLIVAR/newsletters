from django.db import models

class Tag(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250,null=False, unique=True) 
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre