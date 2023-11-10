from django.db import models

from pacientes.models import Paciente

# Create your models here.
class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_pago = models.DateField()
    monto_pago = models.IntegerField()
    tipo_pago = models.CharField(max_length=50)
    # Pago es el extremo multivalor de las relaciones ManyToOne (acá se mapea el relacional)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return 'Pago - id: {}, Realizado: {}, Por un valor de: ${} COP, Tipo: {}'.format(self.id, self.fecha_pago, self.monto_pago, self.tipo_pago)
