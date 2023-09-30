from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'nombre',
            'apellido',
            'especialidad',
            'correo',
            'edad',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'especialidad': 'Especialidad',
            'correo': 'Correo',
            'edad': 'Edad',
        }