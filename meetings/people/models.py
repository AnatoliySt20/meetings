from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=64, blank=True, null=True, default=None)
    school = models.CharField(max_length=64, blank=True, null=True, default=None)
    photography = models.ImageField(upload_to='personal_images/')

    def __str__(self):
        return "%s" % self.name
