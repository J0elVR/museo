from django.shortcuts import render, redirect
from .forms import ExpedienteForm
from .models import Expediente

def crear_expediente(request):
    if request.method == 'POST':
        form = ExpedienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_expedientes')  # redirigir a la lista de expedientes
    else:
        form = ExpedienteForm()

    return render(request, 'expedientes/crear_expediente.html', {'form': form})

def lista_expedientes(request):
    expedientes = Expediente.objects.all()
    return render(request, 'expedientes/lista_expedientes.html', {'expedientes': expedientes})
