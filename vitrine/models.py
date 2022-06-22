from django.db import models


class Profile(models.Model):
    firstname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    photo = models.ImageField(verbose_name='Photo de profil')
    about_me = models.CharField(max_length=5000)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    linkedin = models.CharField(max_length=254)
    github = models.CharField(max_length=254)
    instagram = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Projet(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(max_length=5000)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.title


class Formation(models.Model):
    name = models.CharField(max_length=64)
    location_date = models.CharField(max_length=64)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.name