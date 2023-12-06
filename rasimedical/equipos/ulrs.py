from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('equipos/', views.equipos_list, name='equipoList'),
    path('equipos/equipocreate/', csrf_exempt(views.equipo_create), name='equipoCreate'),
]