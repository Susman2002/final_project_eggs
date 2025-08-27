from django.urls import path
from . import views

urlpatterns = urlpatterns = [
    path('crear/', views.crear_pedido, name='pedidos_crear'),
    path('listar/', views.listar_pedidos, name='pedidos_listar'),
    path('recibir/<int:pk>/', views.recibir_pedido, name='pedidos_recibir'),
]

