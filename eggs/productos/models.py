from django.db import models

class Producto(models.Model):
    TAMANIOS = [
        ('EXTRA', 'Extra'),
        ('ESPECIAL', 'Especial'),
        ('PRIMERA', 'Primera'),
        ('SEGUNDA', 'Segunda'),
        ('TERCERA', 'Tercera'),
        ('CUARTA', 'Cuarta'),
        ('ESPECIAL BLACO', 'Especial Blanco'),
        ('PRIMERA BLACO', 'Primera Blanco'),
        ('SEGUNDA BLACO', 'Segunda Blanco'),
        ('TERCERA BLACO', 'Tercera Blanco'),
        ('CUARTA BLACO', 'Cuarta Blanco'),
    ]

    nombre = models.CharField(max_length=50, choices=TAMANIOS, unique=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # cantidad en unidades o huevos

    def __str__(self):
        return f"{self.nombre}"


# Create your models here.
