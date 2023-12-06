from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import HabitacionForm
from .logic.habitaciones_logic import get_habitacion, create_habitacion, get_habitaciones, update_paciente

def habitaciones_list(request):
    habitaciones = get_habitaciones()
    context = {
        'habitacion_list': habitaciones
    }
    return render(request, 'Habitacion/habitaciones.html', context)

def habitacion_create(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            create_habitacion(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created habitacion')
            return HttpResponseRedirect(reverse('habitacionCreate'))
        else:
            print(form.errors)
    else:
        form = HabitacionForm()

    context = {
        'form': form,
    }
    return render(request, 'Habitacion/HabitacionCreate.html', context)