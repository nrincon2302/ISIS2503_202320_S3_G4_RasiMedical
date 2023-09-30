from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('pacientes/', views.paciente_list, name='pacienteList'),
    path('pacientes/pacientecreate/', csrf_exempt(views.paciente_create), name='pacienteCreate'),
]