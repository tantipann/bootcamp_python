from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

@login_required()
@permission_required('vehiculo.add_vehiculo',raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página principal después de guardar
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

@login_required()
@permission_required('vehiculo.visualizar_catalogo',raise_exception=True)
def listar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()

    # Asignar condición de precio
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = "Bajo"
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = "Medio"
        elif vehiculo.precio > 30000:
            vehiculo.condicion_precio = "Alto"
        else:
            vehiculo.condicion_precio = "---"

    return render(request, 'vehiculo/listar_vehiculo.html', {'vehiculos': vehiculos})
