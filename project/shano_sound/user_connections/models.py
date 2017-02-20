from django.db import models
from user_management.models import User


class Connection(models.Model):
    user_id_1 = models.ManyToManyField(User, related_name='current_user')
    user_id_2 = models.ManyToManyField(User, related_name='friend')

    def __str__(self):
        return "User " + str(self.user_id_1) + " is friends with " + str(self.user_id_2)
