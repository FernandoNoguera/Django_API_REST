from django.db import models

# Create your models here.
class Personajes(models.Model):

    nombre = models.CharField(max_length=60)
    nombre_real = models.CharField(max_length=60)
    imagen = models.ImageField()
    descripcion = models.TextField()


class Chelas(models.Model):

    marca = models.CharField(max_length=50)
    alcohol = models.DecimalField(max_digits=4,decimal_places=2)
    mililitros = models.IntegerField()
    artesanal = models.BooleanField()
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    creado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.marca

        