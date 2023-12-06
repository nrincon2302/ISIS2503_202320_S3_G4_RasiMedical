from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('hospitales/', views.hospitales_list, name='hospitalList'),
    path('hospitales/hospitalcreate/', csrf_exempt(views.hospital_create), name='hospitalCreate'),
]