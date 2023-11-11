from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Paciente

from .forms import PagosForm
from .logic.logic_pagos import get_pagos, get_pago, update_pago, create_pago

import time

def pago_list(request):
    pagos = get_pagos()
    context = {
        'pago_list': pagos
    }
    return render(request, 'pago/pagos.html', context)

def pago_create(request):
    start = time.time()
    if request.method == 'POST':
        form = PagosForm(request.POST)
        if form.is_valid():

            paciente_pk = form["paciente"].value()
            paciente = Paciente.objects.get(pk=paciente_pk)

            create_pago(form, paciente)

        else:
            print(form.errors)
    else:
        form = PagosForm()

    context = {
        'form': form,
    }
    end = time.time()
    print("Tomó un tiempo de: ", end - start)
    return render(request, 'pago/pagoCreate.html', context)