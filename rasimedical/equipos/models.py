from django.db import models

from medicos.models import Medico

# Create your models here.
class Equipo(models.Model):
    disponible = models.BooleanField()
    tipo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '{}{}. {} años.'.format(self.disponible, self.tipo, self.fecha_adquisicion, self.estado)