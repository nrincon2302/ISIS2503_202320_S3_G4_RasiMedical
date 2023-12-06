from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('medicamentos/', views.medicamentos_list, name='medicamentoList'),
    path('medicamentos/medicamentocreate/', csrf_exempt(views.medicamento_create), name='medicamentoCreate'),
]