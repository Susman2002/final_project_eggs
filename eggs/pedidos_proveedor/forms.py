from django import forms
from django.forms import inlineformset_factory
from .models import PedidoProveedor, PedidoProveedorItem

class PedidoProveedorForm(forms.ModelForm):
    class Meta:
        model = PedidoProveedor
        fields = ['fecha_pedido', 'recibido']  # puedes ocultar 'recibido' al crear si quieres
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'type': 'date'}),
        }

class PedidoProveedorItemForm(forms.ModelForm):
    class Meta:
        model = PedidoProveedorItem
        fields = ['producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1})
        }

PedidoItemFormSet = inlineformset_factory(
    parent_model=PedidoProveedor,
    model=PedidoProveedorItem,
    form=PedidoProveedorItemForm,
    extra=11,            # cuántas filas vacías mostrar por defecto
    can_delete=True,
    min_num=1,          # al menos 1 ítem
    validate_min=True,
)
