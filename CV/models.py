from django.db import models
from django.utils import timezone


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=20)
    quality = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '{}'.format(self.name)


class WorkExperience(models.Model):
    diuration = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=250)

    def __str__(self):
        return '{}'.format(self.title)


class Education(models.Model):
    diuration = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    level = models.CharField(max_length=40)
    description = models.TextField(max_length=250)


class Info(models.Model):
    about = models.TextField(max_length=250)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
