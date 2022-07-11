# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.first_name


class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    image = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    github = models.CharField(max_length=128)
    website = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Badge(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True)
    projects = models.ManyToManyField(Project, related_name='projects')

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    projects = models.ManyToManyField(Project, related_name='Projects')

    def __str__(self):
        return self.description


class CVPDF(models.Model):
    name = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.name
