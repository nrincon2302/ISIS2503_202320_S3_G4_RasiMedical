from ..models import Equipo
from pacientes.models import Paciente
from medicos.models import Medico

def get_equipos():
    equipos = Equipo.objects.all()
    return equipos


def get_equipo(eq_pk):
    equipo = Equipo.objects.get(pk=eq_pk)
    return equipo


def update_equipo(eq_pk, new_eq):
    equipo = get_equipo(eq_pk)
    equipo.disponible = new_eq["disponible"]
    equipo.tipo = new_eq["tipo"]
    equipo.fecha_adquisicion = new_eq["fechaAdquisicion"]
    equipo.estado = new_eq["estado"]
   
    equipo.save()
    return equipo

def create_Equipo(form):
    equipo = form.save()
    equipo.save()
    return ()