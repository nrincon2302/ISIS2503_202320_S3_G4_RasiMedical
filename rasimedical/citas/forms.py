from django import forms
from .models import Cita
from pacientes.models import Paciente
from medicos.models import Medico

class CitasForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'fecha',
            'consultorio',
            'hora',
            'paciente',
            'medico',
        ]

        labels = {
            'fecha': 'Fecha',
            'consultorio': 'Consultorio',
            'hora': 'Hora',
            'paciente': 'Paciente',
            'medico': 'Medico',
        }