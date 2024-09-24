# Nexus_Juridico/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('abogado', 'Abogado'),
        ('usuario', 'Usuario'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='usuario')

    # Personaliza los campos de relación
    groups = models.ManyToManyField(
        Group,
        related_name='Users_group',  
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='Users_permissions',  
        blank=True,
    )
