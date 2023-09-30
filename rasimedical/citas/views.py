from django.shortcuts import render
from .logic import logic_citas as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


def citas_view(request):
    if request.method == 'GET':
        citas = vl.get_citas()
        citas_dto = serializers.serialize('json', citas)
        return HttpResponse(citas_dto, 'application/json')


    if request.method == 'POST':
        cita_dto = vl.create_cita(json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')




def cita_view(request, pk):
    if request.method == 'GET':
        cita = vl.get_cita(pk)
        cita_dto = serializers.serialize('json', cita)
        return HttpResponse(cita_dto, 'application/json')

        

@csrf_exempt
def cita_view(request, pk):
    if request.method == 'GET':
        cita_dto = vl.get_cita(pk)
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')

    if request.method == 'PUT':
        cita_dto = vl.update_cita(pk, json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')



# Create your views here.
