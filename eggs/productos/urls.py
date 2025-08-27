from django.urls import path
from . import views

urlpatterns = [
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('editar_productos/<int:pk>', views.editar_productos, name='editar_productos'),
]