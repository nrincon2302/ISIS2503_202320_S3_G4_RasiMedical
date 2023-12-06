from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EquipoForm
from .logic.equipos_logic import get_equipos, create_Equipo, get_hospitales, update_paciente

def equipos_list(request):
    equipos = get_equipos()
    context = {
        'equipo_list': equipos
    }
    return render(request, 'Equipo/equipos.html', context)

def equipo_create(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            create_Equipo(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created equipo')
            return HttpResponseRedirect(reverse('equipoCreate'))
        else:
            print(form.errors)
    else:
        form = EquipoForm()

    context = {
        'form': form,
    }
    return render(request, 'Equipo/EquipoCreate.html', context)