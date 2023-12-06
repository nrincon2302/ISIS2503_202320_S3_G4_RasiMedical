from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UciForm
from .logic.ucis_logic import get_ucis, create_uci, get_uci

def ucis_list(request):
    ucis = get_ucis()
    context = {
        'uci_list':ucis
    }
    return render(request, 'Uci/ucis.html', context)

def uci_create(request):
    if request.method == 'POST':
        form =  UciForm(request.POST)
        if form.is_valid():
            create_uci(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created uci')
            return HttpResponseRedirect(reverse('uciCreate'))
        else:
            print(form.errors)
    else:
        form = UciForm()

    context = {
        'form': form,
    }
    return render(request, 'Uci/UciCreate.html', context)