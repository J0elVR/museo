from django.db import models

class Reservar(models.Model):
    EVENTO_DEFAULT_TEXT = ""

    evento = models.CharField(max_length=100, default=EVENTO_DEFAULT_TEXT, editable=False)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
