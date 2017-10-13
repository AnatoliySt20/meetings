from django.db import models
from contacts.models import MyUser
# Create your models here.

class Event(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

class Member(models.Model):
    participant = models.ForeignKey(MyUser, blank=True, default=None)
    participation = models.ForeignKey(Event, blank=True, default=None)