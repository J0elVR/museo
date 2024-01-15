from django.shortcuts import render
from django.http import HttpResponse

def pagina_inicio(request):
    return render(request, 'inicio.html')

def colecciones_museo(request):
    return render(request, 'colecciones_museo.html')

def coleccion_meso(request):
    return render(request, 'coleccion_meso.html')

def coleccion_colonia(request):
    return render(request, 'coleccion_colonia.html')

def coleccion_maestros(request):
    return render(request, 'coleccion_maestros.html')

def coleccion_romanticismo(request):
    return render(request, 'coleccion_romanticismo.html')