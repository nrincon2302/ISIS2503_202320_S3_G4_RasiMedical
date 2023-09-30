from ..models import Medico

def get_medicos():
    queryset = Medico.objects.all()
    return (queryset)

def create_medico(form):
    medico = form.save()
    medico.save()
    return ()