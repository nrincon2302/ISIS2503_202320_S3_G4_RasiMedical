from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('habitaciones/', views.habitaciones_list, name='habitacionList'),
    path('habitaciones/habitacioncreate/', csrf_exempt(views.habitacion_create), name='habitacionCreate'),
]