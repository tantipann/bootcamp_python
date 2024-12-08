from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from .forms import RegistroForm



def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Asignar permiso automáticamente
            permiso = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permiso)
            return redirect('login')
    else:
        form = RegistroForm()
        return render(request,'usuarios/registro.html', {'form':form})
            