from django.contrib import admin
from user_management.models import User, BaseUser


@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']
