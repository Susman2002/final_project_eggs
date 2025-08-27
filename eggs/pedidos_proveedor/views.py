from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import PedidoProveedor
from .forms import PedidoProveedorForm, PedidoItemFormSet
from django.core.paginator import Paginator

def is_admin(user):
    return user.is_authenticated and (getattr(user, 'role', '') == 'ADMIN' or user.is_superuser)

@login_required
@user_passes_test(is_admin)
@transaction.atomic
def crear_pedido(request):
    pedido = PedidoProveedor()
    if request.method == 'POST':
        form = PedidoProveedorForm(request.POST, instance=pedido)
        formset = PedidoItemFormSet(request.POST, instance=pedido)
        if form.is_valid() and formset.is_valid():
            pedido = form.save(commit=False)
            pedido.creado_por = request.user
            pedido.save()
            formset.instance = pedido
            formset.save()

            # Si ya viene marcado como recibido, aplica stock ahora
            pedido.aplicar_stock_si_corresponde()
            return redirect('pedidos_listar')
    else:
        form = PedidoProveedorForm()
        formset = PedidoItemFormSet(instance=pedido)

    return render(request, 'pedidos_proveedor/crear_pedido.html', {
        'form': form,
        'formset': formset
    })

def is_admin(user):
    return user.role == "ADMIN" or user.is_superuser

@login_required
@user_passes_test(is_admin)
def listar_pedidos(request):
    pedidos_pendientes = PedidoProveedor.objects.filter(recibido=False).prefetch_related('items__producto').order_by('-fecha_pedido')
    pedidos_completados = PedidoProveedor.objects.filter(recibido=True).prefetch_related('items__producto').order_by('-fecha_pedido')

    return render(request, 'pedidos_proveedor/listar_pedidos.html', {
        'pedidos_pendientes': pedidos_pendientes,
        'pedidos_completados': pedidos_completados,
    })


@login_required
@user_passes_test(is_admin)
@transaction.atomic
def recibir_pedido(request, pk):
    pedido = get_object_or_404(PedidoProveedor, pk=pk)
    if not pedido.recibido:
        pedido.recibido = True
        pedido.save(update_fields=['recibido'])
        pedido.aplicar_stock_si_corresponde()
    return redirect('pedidos_listar')