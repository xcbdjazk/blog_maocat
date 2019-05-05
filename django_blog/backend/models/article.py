from django.db import models
from django.conf import settings
import hashlib
from .base import Model


class Article(Model):
    class Meta:
        db_table = "article"
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=4096)
    tag = models