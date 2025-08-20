from django.urls import path
from .views import ver_clientes, admin_dashboard, editar_cliente, cliente_delete, crear_cliente, client_dashboard
from . import views

urlpatterns = [
    path('ver_clientes/', ver_clientes, name='ver_clientes'),
    path('ver_clientes/crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('editar_cliente/<str:ci>/', editar_cliente, name='editar_cliente'),
    path("clientes/<int:pk>/delete/", cliente_delete, name="cliente_delete"),
    path('client_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard/', client_dashboard, name='client_dashboard'),
    #path('create-client/', views.create_client, name='create_client'),
]