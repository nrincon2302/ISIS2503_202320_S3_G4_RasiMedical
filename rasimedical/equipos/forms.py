from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'disponible',
            'tipo',
            'fecha_adquisiscion',
            'estado',
        
        ]
        labels = {
            'disponible': 'disponible',
            'tipo': 'tipo',
            'fecha_adquisiscion': 'fecha_adquisicion',
            'estado': 'estado',
      
        }