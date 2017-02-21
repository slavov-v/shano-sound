from django.contrib import admin
from user_management.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']
