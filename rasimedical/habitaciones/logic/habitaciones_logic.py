from ..models import Habitacion
from pacientes.models import Paciente
from medicos.models import Medico

def get_habitaciones():
    habitaciones = Habitacion.objects.all()
    return habitaciones


def get_habitacion(hab_pk):
    habitacion = Habitacion.objects.get(pk=hab_pk)
    return habitacion


def update_habitacion(hab_pk, new_hab):
    habitacion = get_habitacion(hab_pk)
    habitacion.ocupada = new_hab["ocupada"]
    habitacion.tipo = new_hab["tipo"]

    habitacion.save()
    return habitacion


def create_habitacion(form):
    habitacion = form.save()
    habitacion.save()
    return ()