from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            'nombre',
            'laboratorio',
            'tipo',
            'dosis',
            'fechaCaducidad',
            'fechaLote',

        
        ]
        labels = {
            'nombre': 'nombre',
            'laboratorio' : 'laboratorio',
            'tipo': 'tipo',
            'dosis': 'dosis',
            'fechaCaducidad': 'fechaCaducidad',
            'fechaLote': 'fechaLote',      
        }


        