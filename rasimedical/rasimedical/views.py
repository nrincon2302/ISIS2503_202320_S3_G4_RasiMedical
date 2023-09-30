from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hola mundo desde RASI MEDICAL")