from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка пользователей"""
    list_display = (
        'phone_number',
    )
