from multiprocessing import context
from django.shortcuts import render
from blog.models import Article

def index(request):
    articles = Article.objects.all()
    articles = sorted(articles, key=lambda k: k.date_published)
    context = {'articles': articles}
    return render(request, 'vitrine/index.html')

def mentions_legales(request):
    return render(request, 'vitrine/mentions.html')

def plan(request):
    return render(request, 'vitrine/plan.html')

