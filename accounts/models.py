from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='Groups',
        blank=True,
        help_text='The groups this user belongs to',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='User permissions',
        blank=True,
        help_text='Specific permissions for this user',
        related_name='customuser_set',
        related_query_name='customuser',
    )
