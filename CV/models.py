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

    def __str__(self):
        return '{}'.format(self.diuration)


class Info(models.Model):
    about = models.TextField(max_length=250)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    cv = models.FileField()

    def __str__(self):
        return '{}'.format(self.email)


class social_network(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return '{}'.format(self.name)


class Portfilio(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return '{}'.format(self.name)


class Refrences(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)


class ContactUS(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return '{}'.format(self.email)