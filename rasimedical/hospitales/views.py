from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import HospitalForm
from .logic.hospitales_logic import get_hospital, create_hospital, get_hospitales, update_paciente

def hospitales_list(request):
    hospitales = get_hospitales()
    context = {
        'hospital_list': hospitales
    }
    return render(request, 'Hospital/hospitales.html', context)

def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            create_hospital(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created hospital')
            return HttpResponseRedirect(reverse('hospitalCreate'))
        else:
            print(form.errors)
    else:
        form = HospitalForm()

    context = {
        'form': form,
    }
    return render(request, 'Hospital/HospitalCreate.html', context)