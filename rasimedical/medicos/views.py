from .logic import medico_logic as pl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def medicos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            medico_dto = pl.get_paciente(id)
            medico = serializers.serialize('json', [medico_dto,])
            return HttpResponse(medico, 'application/json')
        else:
            medico_dto = pl.get_medicos()
            medicos = serializers.serialize('json', medico_dto)
            return HttpResponse(medicos, 'application/json')

    if request.method == 'POST':
        medico_dto = pl.get_medicos(json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')

@csrf_exempt
def medico_view(request, pk):
    if request.method == 'GET':
        medico_dto = pl.get_medico(pk)
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')

    if request.method == 'PUT':
        medico_dto = pl.update_medico(pk, json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')