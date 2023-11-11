from django import forms
from .models import Pago
from pacientes.models import Paciente

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'fecha_pago',
            'monto_pago',
            'tipo_pago',
            'paciente',
        ]

        widgets = {
            'fecha_pago': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'fecha_pago': 'Fecha de pago',
            'monto_pago': 'Monto de pago',
            'tipo_pago': 'Tipo de pago',
            'paciente': 'Paciente',
        }