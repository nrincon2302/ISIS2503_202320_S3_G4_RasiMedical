from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MedicoForm
from .logic.medico_logic import get_medicos, create_medico

def medico_list(request):
    medicos = get_medicos()
    context = {
        'medico_list': medicos
    }
    return render(request, 'Medico/medicos.html', context)

def variable_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            create_medico(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created medico')
            return HttpResponseRedirect(reverse('medicoCreate'))
        else:
            print(form.errors)
    else:
        form = MedicoForm()

    context = {
        'form': form,
    }
    return render(request, 'Medico/medicoCreate.html', context)