import datetime

from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=60)
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    date_added = models.DateField(auto_now=True, null=True, blank=True)
    date_of_event = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):  # make comment why I need this
        return self.title

    def published_recently(self):
        return self.date_added >= (timezone.now() - datetime.timedelta(days=7))
