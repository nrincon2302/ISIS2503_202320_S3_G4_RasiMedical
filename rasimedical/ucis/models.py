from django.db import models

from django.db import models

from medicos.models import Medico

# Create your models here.
class Uci(models.Model):
    disponible = models.BooleanField()
    numMonitoresCardiacos = models.IntegerField()
    numRespiradores = models.IntegerField()
    numSondas = models.IntegerField()

    def __str__(self):
        return '{}{}. {} años.'.format(self.disponible, self.numRespiradores, self.numMonitoresCardiacos, self.numSondas)