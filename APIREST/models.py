# -*- coding: utf-8 -*-
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.first_name


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='project', null=True)
    framework = models.CharField(max_length=50, null=True)
    github = models.CharField(max_length=128)
    website = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Badge(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, null=True)
    projects = models.ManyToManyField(Project, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=128)
    projects = models.ManyToManyField(Project, related_name='Projects')

    def __str__(self):
        return self.description


class CurriculumVitae(models.Model):
    name = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.name


class Analytic(models.Model):
    page_title = models.CharField(max_length=50)
    visits = models.IntegerField()

    def __str__(self) -> str:
        return self.page_title


class Message(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    message = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.message
