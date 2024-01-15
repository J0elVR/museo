from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    curp = models.CharField(max_length=18)
    numero_registro = models.IntegerField()  # Este campo se llenará automáticamente

    def __str__(self):
        return self.nombre