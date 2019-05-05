
from django.db import models
from django.conf import settings
import hashlib
from .base import Model


class Admin(Model):

    aid = models.AutoField(primary_key=True)
    password_hash = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    mobile = models.EmailField(max_length=11, null=True)
    desc = models.CharField(max_length=128, null=True)
    title = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "admin"

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = hashlib.md5('{}{}'.format(settings.SECRET_KEY, value).encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == hashlib.md5('{}{}'.format(settings.SECRET_KEY, password).encode()).hexdigest()