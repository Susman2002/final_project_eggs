from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('users/', include('users.urls')),
    path('clientes/', include('clientes.urls')),
    path('productos/', include('productos.urls')),
    path('pedidos_proveedor/', include('pedidos_proveedor.urls')),
]
