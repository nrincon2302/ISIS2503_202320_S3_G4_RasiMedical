from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CitasForm
from .logic.logic_citas import get_citas, create_cita, get_cita, update_cita

def cita_list(request):
    citas = get_citas()
    context = {
        'cita_list': citas
    }
    return render(request, 'Cita/citas.html', context)

def cita_create(request):
    if request.method == 'POST':
        form = CitasForm(request.POST)
        if form.is_valid():
            create_cita(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created cita')
            return HttpResponseRedirect(reverse('citaCreate'))
        else:
            print(form.errors)
    else:
        form = CitasForm()

    context = {
        'form': form,
    }
    return render(request, 'Cita/citaCreate.html', context)