from django.db import models
from user_management.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, through='MembershipInChat',
                                     related_name='chat_room')

    def __str__(self):
        return str(self.id)


class MembershipInChat(models.Model):
    chat_room = models.ForeignKey(Chat)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('chat_room', 'user')

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    content = models.TextField()
    membership = models.ForeignKey(MembershipInChat)

    def __str__(self):
        return self.content
