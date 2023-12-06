from django import forms
from .models import Uci

class UciForm(forms.ModelForm):
    class Meta:
        model = Uci
        fields = [
            'disponible',
            'numMonitoresCardiacos',
            'numRespiradores',
            'numSondas',
 

        
        ]
        labels = {
            'disponible': 'disponible',
            'numMonitoresCardiacos' : 'numMonitoresCardiacos',
            'numRespiradores': 'numRespiradores',
            'numSondas': 'numSondas',
               
        }
