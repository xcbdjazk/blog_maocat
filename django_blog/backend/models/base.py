
from django.db import models
import datetime
import django.utils.timezone as timezone

class Model(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.update_time = datetime.datetime.now()
        super(Model, self).save(*args, **kwargs)