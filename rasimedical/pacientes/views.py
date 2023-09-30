from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PacienteForm
from .logic.pacientes_logic import get_pacientes, create_paciente, get_paciente, update_paciente

def paciente_list(request):
    pacientes = get_pacientes()
    context = {
        'paciente_list': pacientes
    }
    return render(request, 'Paciente/pacientes.html', context)

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            create_paciente(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created paciente')
            return HttpResponseRedirect(reverse('pacienteCreate'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    context = {
        'form': form,
    }
    return render(request, 'Paciente/pacienteCreate.html', context)