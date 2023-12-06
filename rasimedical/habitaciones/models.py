from django.db import models

from medicos.models import Medico

# Create your models here.
class Habitacion(models.Model):
    ocupada = models.BooleanField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return '{}{}. {} años.'.format(self.ocupada, self.tipo)