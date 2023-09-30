from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Medico
from .models import Paciente

from .forms import CitasForm
from .logic.logic_citas import get_citas, create_cita, get_cita, update_cita

import time

def cita_list(request):
    citas = get_citas()
    context = {
        'cita_list': citas
    }
    return render(request, 'Cita/citas.html', context)

def cita_create(request):
    start = time.time()
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():

            paciente_pk = form["paciente"].value()
            paciente = Paciente.objects.get(pk=paciente_pk)
            medico_pk = form["medico"].value()
            medico = Medico.objects.get(pk=medico_pk)

            create_cita(form, paciente, medico)

        else:
            print(form.errors)
    else:
        form = CitasForm()

    context = {
        'form': form,
    }
    end = time.time()
    print("Tomó un tiempo de: ", end - start)
    return render(request, 'Cita/citaCreate.html', context)