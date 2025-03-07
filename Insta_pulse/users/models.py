from django.db import models
from django.contrib.auth.models import AbstractUser

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions', 
        blank=True
    )

    def __str__(self):
        return self.username
