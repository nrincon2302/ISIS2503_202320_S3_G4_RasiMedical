from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)