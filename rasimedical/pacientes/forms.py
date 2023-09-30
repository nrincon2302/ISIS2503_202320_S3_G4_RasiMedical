from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'edad',
            'correo',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'correo': 'Correo',
        }