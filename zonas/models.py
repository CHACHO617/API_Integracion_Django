from django.db import models

# Create your models 
class ZonaAgricola(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    cultivo_principal = models.CharField(max_length=100)
    hectareas = models.FloatField()
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.nombre
