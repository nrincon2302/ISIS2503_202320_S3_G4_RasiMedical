from ..models import Medico

def get_medicos():
    medicos = Medico.objects.all()
    return medicos

def get_medico(pac_pk):
    medico = Medico.objects.get(pk=pac_pk)
    return medico

def update_medico(pac_pk, new_pac):
    medico = get_medico(pac_pk)
    medico.nombre = new_pac["nombre"]
    medico.apellido = new_pac["apellido"]
    medico.especialidad = new_pac["especialidad"]
    medico.edad = new_pac["edad"]
    medico.correo = new_pac["correo"]
    medico.save()
    return medico

def create_medico(pac):
    medico = Medico(nombre=pac["nombre"].value(), apellido=pac["apellido"].value(), edad=pac["edad"].value(), 
                    especialidad=pac["especialidad"].value(),correo=pac["correo"].value())
    medico.save()
    return medico