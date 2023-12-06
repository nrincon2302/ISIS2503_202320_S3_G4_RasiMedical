from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('ucis/', views.ucis_list, name='uciList'),
    path('ucis/ucicreate/', csrf_exempt(views.uci_create), name='uciCreate'),
]