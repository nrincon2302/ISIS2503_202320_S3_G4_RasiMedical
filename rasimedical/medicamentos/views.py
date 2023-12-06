from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MedicamentoForm
from .logic.medicamentos_logic import get_medicamento, create_medicamento, get_medicamentos, update_paciente

def medicamentos_list(request):
    medicamentos = get_medicamentos()
    context = {
        'medicamento_list': medicamentos
    }
    return render(request, 'Medicamento/medicamentos.html', context)

def medicamento_create(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            create_medicamento(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created medicamento')
            return HttpResponseRedirect(reverse('medicamentoCreate'))
        else:
            print(form.errors)
    else:
        form = MedicamentoForm()

    context = {
        'form': form,
    }
    return render(request, 'Medicamento/MedicamentoCreate.html', context)