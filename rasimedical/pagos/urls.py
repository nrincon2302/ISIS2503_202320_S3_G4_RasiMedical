from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('pagos/', views.pago_list, name='pagoList'),
    path('pagos/pagocreate/', csrf_exempt(views.pago_create), name='pagoCreate'),
]