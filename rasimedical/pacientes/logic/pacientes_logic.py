from ..models import Paciente

def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(pac_pk):
    paciente = Paciente.objects.get(pk=pac_pk)
    return paciente

def update_paciente(pac_pk, new_pac):
    paciente = get_paciente(pac_pk)
    paciente.nombre = new_pac["nombre"]
    paciente.apellido = new_pac["apellido"]
    paciente.edad = new_pac["edad"]
    paciente.correo = new_pac["correo"]
    paciente.save()
    return paciente

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()
