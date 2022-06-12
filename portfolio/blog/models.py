from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField()
    author = models.CharField(max_length=64)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie')
    
    def __str__(self):
        return self.name
