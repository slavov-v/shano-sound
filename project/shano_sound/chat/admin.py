from django.contrib import admin
from chat.models import Chat, Message, MembershipInChat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'membership']


@admin.register(MembershipInChat)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_room', 'user']
