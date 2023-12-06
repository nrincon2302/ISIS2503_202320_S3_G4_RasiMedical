from django import forms
from .models import Habitacion

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = [
            'ocupada',
            'tipo',

        
        ]
        labels = {
            'ocupada': 'ocupada',
            'tipo': 'tipo',
      
        }