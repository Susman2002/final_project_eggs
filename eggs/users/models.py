from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('CLIENT', 'Cliente'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='CLIENT')

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'ADMIN'
        super().save(*args, **kwargs)

    def is_admin(self):
        return self.role == 'ADMIN'
    
    def is_client(self):
        return self.role == 'CLIENT'
