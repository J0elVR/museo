from django.shortcuts import render
from django.http import HttpResponse

def pagina_inicio(request):
    return render(request, 'inicio.html')

def info_museo(request):
    return render(request, 'info_museo.html')