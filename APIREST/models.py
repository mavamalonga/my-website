from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

	def __str__(self):
		return self.first_name


class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 


class Badge(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class Skill(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    image = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    badges = models.ManyToManyField(Badge, related_name='badges')
    skills = models.ManyToManyField(Skill, related_name='skills')
    github = models.CharField(max_length=128)
    website = models.CharField(max_length=128)

    def __str__(self):
        return self.title