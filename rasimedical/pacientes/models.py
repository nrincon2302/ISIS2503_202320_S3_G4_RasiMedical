from django.db import models

from medicos.models import Medico

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=50)

    def __str__(self):
        return '{}{}. {} años.'.format(self.nombre, self.apellido, self.edad)