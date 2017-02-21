from django.db import models
from user_management.models import User
# Create your models here.


class Song(models.Model):
    user_id = models.ForeignKey(User, on_delete=None)
    name = models.CharField(max_length=50, blank=True, null=True)
    song_file = models.FileField()
