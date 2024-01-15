from django.db import models

class Expediente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    curriculum_vitae = models.FileField(upload_to='curriculums/')
    foto_identificacion = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.nombre
