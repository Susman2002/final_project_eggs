from django.db import models
from django.conf import settings

class Cliente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ci = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    telefono_principal = models.CharField(max_length=20)
    telefono_secundario = models.CharField(max_length=20, blank=True)
    direccion_principal = models.TextField()
    direccion_secundaria = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.ci})"

