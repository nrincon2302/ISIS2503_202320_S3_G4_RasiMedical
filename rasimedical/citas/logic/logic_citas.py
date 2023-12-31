from ..models import Cita
from pacientes.models import Paciente
from medicos.models import Medico

def get_citas():
    citas = Cita.objects.all()
    return citas


def get_cita(cit_pk):
    cita = cita.objects.get(pk=cit_pk)
    return cita


def update_cita(cit_pk, new_cita):
    cita = get_cita(cit_pk)
    cita.fecha = new_cita["fecha"]
    cita.hora = new_cita["hora"]
    cita.consultorio = new_cita["consultorio"]
    cita.paciente = new_cita["paciente"]
    cita.medico = new_cita["medico"]
    cita.save()
    return cita


def create_cita(cit, pac_id, med_id):
    cita = Cita(fecha=cit["fecha"].value(), hora=cit["hora"].value(), 
                consultorio=cit["consultorio"].value(), paciente=pac_id, medico=med_id)
    cita.save()
    return cita

