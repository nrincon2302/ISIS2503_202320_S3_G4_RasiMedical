from ..models import Pago
from pacientes.models import Paciente

def get_pagos():
    pagos = Pago.objects.all()
    return pagos


def get_pago(pago_pk):
    pago = pago.objects.get(pk=pago_pk)
    return pago


def update_pago(pago_pk, new_pago):
    pago = get_pago(pago_pk)
    pago.fecha_pago = new_pago["fecha_pago"]
    pago.monto_pago = new_pago["monto_pago"]
    pago.tipo_pago = new_pago["tipo_pago"]
    pago.paciente = new_pago["paciente"]
    pago.save()
    return pago


def create_pago(pago, pac_id):
    pago = pago(fecha_pago=pago["fecha_pago"], 
                monto_pago=pago["monto_pago"].value(), 
                tipo_pago=pago["tipo_pago"].value(), 
                paciente=pac_id)
    pago.save()
    return pago

