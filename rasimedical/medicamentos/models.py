from django.db import models

from medicos.models import Medico

# Create your models here.
class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    laboratorio = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    dosis = models.IntegerField()
    fechaCaducidad = models.DateField()
    fechaLote = models.DateField()

    def __str__(self):
        return '{}{}. {} años.'.format(self.nombre, self.laboratorio, self.tipo, self.dosis, self.fechaCaducidad, self.fechaLote)