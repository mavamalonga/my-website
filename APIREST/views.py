# -*- coding: utf-8 -*-
from django.db import models


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
    image = models.ForeignKey(Photo, null=False, on_delete=models.SET_NULL, blank=True)
    badges = models.ManyToManyField(Badge, null=False, on_delete=models.SET_NULL, blank=True)
    skills = models.ManyToManyField(Skill, null=False, on_delete=models.SET_NULL, blank=True)
    github = models.CharField(max_length=128)
    website = models.CharField(max_length=128)

    def __str__(self):
        return self.title
