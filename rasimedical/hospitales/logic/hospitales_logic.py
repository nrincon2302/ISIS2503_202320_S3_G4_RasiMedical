from ..models import Hospital
from pacientes.models import Paciente
from medicos.models import Medico

def get_hospitales():
    hospitales = Hospital.objects.all()
    return hospitales


def get_hospital(hosp_pk):
    hospital = Hospital.objects.get(pk=hosp_pk)
    return hospital


def update_hospital(hosp_pk, new_hosp):
    hospital = get_hospital(hosp_pk)
    hospital.nombre = new_hosp["nombre"]
    hospital.direccion = new_hosp["direccion"]
    hospital.equipo = new_hosp["equipo"]
    hospital.medicamento = new_hosp["medicamento"]
    hospital.uci = new_hosp["uci"]
    hospital.habitacion = new_hosp["habitacion"]
    hospital.save()
    return hospital

def create_hospital(form):
    hospital = form.save()
    hospital.save()
    return ()


