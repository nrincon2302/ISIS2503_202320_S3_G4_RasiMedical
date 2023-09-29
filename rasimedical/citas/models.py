from django.db import models

from pacientes.models import Paciente
from medicos.models import Medico

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    consultorio = models.CharField(max_length=50)
    hora = models.TimeField()
    # Cita es el extremo multivalor de las relaciones ManyToOne (acá se mapea el relacional)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return '{}. {} \n Doctor: {} \nPaciente: {}'.format(self.fecha, self.hora, self.paciente, self.medico)
