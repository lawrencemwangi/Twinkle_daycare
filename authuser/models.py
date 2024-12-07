from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_LEVEL_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('student', 'Student'),
    ]
    
    user_level = models.CharField(max_length=10, choices=USER_LEVEL_CHOICES, default='student')
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

    # Avoid reverse accessor conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.user_level})"



