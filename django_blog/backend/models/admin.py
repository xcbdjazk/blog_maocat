from django.db import models
from django_blog import settings
import hashlib
from .base import Model


class Admin(Model):

    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=50)

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