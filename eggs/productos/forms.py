from .models import Producto
from django import forms

class ProductEditionForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'precio_unitario', 
            'stock'
        ]