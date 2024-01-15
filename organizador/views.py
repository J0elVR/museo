from django.shortcuts import render, redirect
from .forms import OrganizadorForm
from .models import Organizador

def organizar_expediente(request, expediente_id):
    expediente = Expediente.objects.get(pk=expediente_id)

    if request.method == 'POST':
        form = OrganizadorForm(request.POST)
        if form.is_valid():
            organizador = form.save(commit=False)
            organizador.expediente = expediente
            organizador.save()
            return redirect('lista_expedientes')
    else:
        form = OrganizadorForm()

    return render(request, 'organizador/organizar_expediente.html', {'form': form, 'expediente': expediente})

def buscar_expedientes(request):
    if request.method == 'POST':
        palabra_clave = request.POST.get('palabra_clave')
        expedientes = Organizador.objects.filter(palabras_clave__icontains=palabra_clave).values_list('expediente', flat=True)
        expedientes = Expediente.objects.filter(id__in=expedientes)
    else:
        expedientes = Expediente.objects.all()

    return render(request, 'organizador/buscar_expedientes.html', {'expedientes': expedientes})
