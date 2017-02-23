from django.db import models
from user_management.custom_fields import PasswordModelField
from hashlib import sha256
# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    friends = models.ManyToManyField(to='User')

    @classmethod
    def exists(cls, mail):
        try:
            obj = cls.objects.get(email=mail)
            return True
        except Exception:
            return False

    @classmethod
    def validate_password(cls, mail, password):
        obj = User.objects.get(email=mail)
        password = sha256(password.encode('utf-8')).hexdigest()
        if password == obj.password:
            return True
        return False

    def __str__(self):
        return str(self.pk)
