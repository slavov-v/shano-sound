from django.contrib import admin
from chat.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']


# @admin.register(MembershipInChat)
# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ['id', 'chat_room', 'user']
