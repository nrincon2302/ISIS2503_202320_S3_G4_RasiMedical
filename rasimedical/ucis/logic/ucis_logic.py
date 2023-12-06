from ..models import    Uci
from pacientes.models import Paciente
from medicos.models import Medico

def get_ucis():
    ucis = Uci.objects.all()
    return ucis


def get_uci(uci_pk):
    uci = Uci.objects.get(pk=uci_pk)
    return uci


def update_hospital(uci_pk, new_uci):
    uci = get_uci(uci_pk)
    uci.disponible = new_uci["disponible"]
    uci.numMonitoresCardiacos = new_uci["numMonitoresCardiacos"]
    uci.numRespiradores = new_uci["numRespiradores"]
    uci.numSondas = new_uci["num_sondas"]

    uci.save()
    return uci


def create_uci(form):
    uci = form.save()
    uci.save()
    return ()