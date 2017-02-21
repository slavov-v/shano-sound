from django.db import models
from user_management.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, through='MembershipInChat',
                                     related_name='chat_room')


class MembershipInChat(models.Model):
    chat_room = models.ForeignKey(Chat)
    user = models.ForeignKey(User)


class Message(models.Model):
    content = models.TextField()
    membership = models.ForeignKey(MembershipInChat)
