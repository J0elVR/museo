from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from .models import Empleado

def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            # Asignar un número de registro (puedes usar algún mecanismo de generación automática)
            empleado.numero_registro = 1001  # Ejemplo
            empleado.save()
            # Obtén la lista de empleados
            empleados = Empleado.objects.all()
            # Renderiza la misma página con la lista actualizada de empleados
            return render(request, 'registrar_empleado.html', {'form': form, 'empleados': empleados})
    else:
        form = EmpleadoForm()

    return render(request, 'registrar_empleado.html', {'form': form})

def pagina_inicio(request):
    return render(request, 'inicio.html')

def lista_empleados(request):
    # Obtén la lista de empleados
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})

def admin_museo(request):
    # Obtén la lista de empleados
    empleados = Empleado.objects.all()
    return render(request, 'registrar_empleado.html', {'empleados': empleados})

