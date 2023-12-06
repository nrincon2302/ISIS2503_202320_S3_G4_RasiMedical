from ..models import Medicamento
from pacientes.models import Paciente
from medicos.models import Medico

def get_medicamentos():
    medicamentos = Medicamento.objects.all()
    return medicamentos


def get_medicamento(medc_pk):
    medicamento = Medicamento.objects.get(pk=medc_pk)
    return medicamento


def update_medicamento(medc_pk, new_medc):
    medicamento = get_medicamento(medc_pk)
    medicamento.nombre = new_medc["nombre"]
    medicamento.laboratorio = new_medc["laboratorio"]
    medicamento.tipo = new_medc["tipo"]
    medicamento.dosis = new_medc["dosis"]
    medicamento.fechaCaducidad = new_medc["fechaCaducidad"]
    medicamento.fechaLote = new_medc["fechaLote"]
    medicamento.save()
    return medicamento

def create_medicamento(form):
    medicamento = form.save()
    medicamento.save()
    return ()