
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('users/', include('users.urls')),
    path('clientes/', include('clientes.urls')),
]
