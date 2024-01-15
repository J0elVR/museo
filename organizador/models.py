from django.db import models
from expedientes.models import Expediente  # Importa el modelo de expedientes

class Organizador(models.Model):
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)
    palabras_clave = models.TextField()

    def __str__(self):
        return f"Organizador para {self.expediente.nombre}"
