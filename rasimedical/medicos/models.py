from django.db import models

# Create your models here.
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return '{}{}. {} años. Especialidad en: {}'.format(self.nombre, self.apellido, self.edad, self.especialidad)