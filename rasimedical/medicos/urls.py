from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('medicos/', views.medico_list, name='medicoList'),
    path('medicos/medicocreate/', csrf_exempt(views.medico_create), name='medicoCreate'),
]