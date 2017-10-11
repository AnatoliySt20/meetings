from django.db import models
from people.models import User


class Event(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    date = models.DateField()
    address = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name


class Member(models.Model):
    event = models.ForeignKey(Event, blank=True, null=True, default=None)
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    will_come = models.BooleanField(default=False)