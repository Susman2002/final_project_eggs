from .models import Producto
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test
from .forms import ProductEditionForm

@user_passes_test(lambda u: u.is_superuser)
def ver_productos(request):
    productos = Producto.objects.all() #accedemos a todos los datos de la BD
    return render(request, 'productos/ver_productos.html', {'productos':productos})

def editar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductEditionForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
    else:
        form = ProductEditionForm(instance=producto)

    return render(request, 'productos/editar_precio_productos.html', {'form': form, 'producto': producto})


