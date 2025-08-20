from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Cliente
from .forms import ClienteForm, UserForm
from django.contrib.auth.hashers import make_password
from users.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.is_authenticated and user.role == 'ADMIN'


@user_passes_test(lambda u: u.is_superuser)
def ver_clientes(request):
    clientes = Cliente.objects.all() #accedemos a todos los datos de la BD
    return render(request, 'clientes/ver_clientes.html', {'clientes':clientes})


@login_required
@user_passes_test(lambda u: u.role == 'ADMIN')
def admin_dashboard(request):
    return render(request, 'clientes/base_admin.html')

@login_required
@user_passes_test(lambda u: u.role == 'CLIENT')
def client_dashboard(request):
    return render(request, 'clientes/client_dashboard.html')

#------------clinetes crud----------------
def editar_cliente(request, ci):
    cliente = get_object_or_404(Cliente, ci=ci)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/editar_clientes.html', {'form': form})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == "POST":
        cliente.delete()
        return redirect("ver_clientes")  # cambia por el nombre de tu lista de clientes
    
    return render(request, "clientes/cliente_confirm_delete.html", {"cliente": cliente})

#crear cliente-----------
@login_required
@user_passes_test(is_admin)
def crear_cliente(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            return redirect('ver_clientes')  # Ajusta al nombre de tu url
    else:
        user_form = UserForm()
        cliente_form = ClienteForm()

    return render(request, 'clientes/crear_cliente.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })


