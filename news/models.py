from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=60)
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    date_added = models.DateField(auto_now=True, null=True, blank=True)
    date_of_event = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=20, null=True, blank=True)
