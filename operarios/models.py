from django.db import models

# Create your models here.

class Operario(models.Model):
    legajo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    puesto = models.JSONField()  # Para manejar múltiples puestos seleccionados
   

    def __str__(self):
        return self.nombre
