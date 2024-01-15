from django.shortcuts import render, redirect
from .forms import ReservarForm
from .models import Reservar

def reservar_evento(request):
    evento = request.GET.get('evento')
    if request.method == 'POST':
        form = ReservarForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)  # Obtener la instancia del formulario sin guardarla aún
            reserva.evento = evento  # Asignar el valor del evento a la instancia
            reserva.save()  # Guardar la instancia en la base de datos
            return redirect('ver_evento')  
    else:
        form = ReservarForm()

    return render(request, 'reservar_evento.html', {'form': form, 'evento': evento})


def pagina_inicio(request):
    return render(request, 'inicio.html')

def ver_evento(request):
    eventos = Reservar.objects.all()
    return render(request, 'ver_evento.html', {'eventos': eventos})

def eventos_museo(request):
    return render(request, 'eventos_museo.html')
