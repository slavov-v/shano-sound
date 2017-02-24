from django.db import models
from user_management.custom_fields import PasswordModelField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from hashlib import sha256
from user_management.managers import UserManager
# Create your models here.


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    friends = models.ManyToManyField(to='BaseUser')
    is_online = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_online = models.BooleanField(default=False)
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
        return self.email
