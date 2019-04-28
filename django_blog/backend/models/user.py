from django.db import models
from django_blog.django_blog import settings
import hashlib


class Users():

    name = models.CharField(max_length=20)
    password_ = models.CharField(max_length=20)

    class Meta:
        db_table = "Users"

    @property
    def password(self):
        raise ValueError('PASSWORD IS NOT READ')

    @password.setter
    def password(self, value):
        self.password = hashlib.md5('{}{}'.format(settings.SECRET_KEY, value))

    def verify_password(self, password):
        return self.password_ == hashlib.md5('{}{}'.format(settings.SECRET_KEY, password))