from ..models import Cita

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
    cita.paciente = new_cita["paciente"]
    cita.medico = new_cita["medico"]
    cita.save()
    return cita


def create_cita(cit):
    cita = Cita(fecha=cit["fecha"], hora=cit["hora"], paciente=cit["paciente"], medico=cit["medico"])
    cita.save()
    return cita

