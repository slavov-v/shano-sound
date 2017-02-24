from django.db import models
from user_management.models import BaseUser
# Create your models here.


class Metadata(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    album = models.CharField(max_length=120, blank=True, null=True)
    artist = models.CharField(max_length=120, blank=True, null=True)
    # janre = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return """|Artist: {}|
                  |Name: {}|
                  |Album: {}|""".format(str(self.artist), str(self.name), str(self.album))

class Song(models.Model):
    user_id = models.ForeignKey(BaseUser, on_delete=None)
    metadata = models.ForeignKey(Metadata, on_delete=None, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    song_file = models.FileField()
