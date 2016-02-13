from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# company model

class Company(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="Images")
    description = models.TextField()
    employees = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    comment = models.CharField(max_length=300)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return self.comment
