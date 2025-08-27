from django.db import models, transaction
from django.utils import timezone
from django.conf import settings
from django.db.models import F
from productos.models import Producto

class PedidoProveedor(models.Model):
    fecha_pedido = models.DateField(default=timezone.now)
    recibido = models.BooleanField(default=False)
    fecha_llegada = models.DateField(null=True, blank=True)
    procesado_stock = models.BooleanField(default=False)  # evita sumar stock 2 veces
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='pedidos_proveedor_creados'
    )

    def __str__(self):
        estado = "RECIBIDO" if self.recibido else "PENDIENTE"
        return f"Pedido #{self.id} - {estado} - {self.fecha_pedido}"

    @transaction.atomic
    def aplicar_stock_si_corresponde(self):
        """
        Si el pedido está marcado como recibido y aún no se aplicó al stock,
        suma las cantidades de cada ítem al stock del producto.
        """
        if self.recibido and not self.procesado_stock:
            for item in self.items.select_related('producto'):
                # Evita condiciones de carrera
                Producto.objects.filter(pk=item.producto_id).update(
                    stock=F('stock') + item.cantidad
                )
            self.procesado_stock = True
            if not self.fecha_llegada:
                self.fecha_llegada = timezone.now().date()
            super().save(update_fields=['procesado_stock', 'fecha_llegada'])

class PedidoProveedorItem(models.Model):
    pedido = models.ForeignKey(PedidoProveedor, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.producto.get_nombre_display()}"

