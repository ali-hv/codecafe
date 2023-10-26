from django.contrib import admin
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "get_full_name", "date_joined", "last_login", "is_active", "is_superuser", "is_staff", ]
