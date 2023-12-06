from django.db import models

from medicamentos.models import Medicamento
from ucis.models import Uci
from equipos.models import Equipo
from habitaciones.models import Habitacion

# Create your models here.
class Hospital(models.Model):
    nombre = models.CharField()
    direccion = models.CharField(max_length=50)
    
    # Cita es el extremo multivalor de las relaciones ManyToOne (acá se mapea el relacional)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    uci = models.ForeignKey(Uci, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return '{}. {} \n Doctor: {} \nPaciente: {}'.format(self.nombre, self.direccion, self.medicamento, self.uci, self.equipo, self.habitacion)
