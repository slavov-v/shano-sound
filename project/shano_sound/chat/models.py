from django.db import models
from user_management.models import BaseUser


class Message(models.Model):
    sender = models.ForeignKey(BaseUser)
    content = models.TextField()

    def __str__(self):
        return self.content
