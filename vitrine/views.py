from multiprocessing import context
from django.shortcuts import render
from APIREST.models import CVPDF

def index(request):
    """
    articles = Article.objects.all()
    articles = sorted(articles, key=lambda k: k.date_published)
    context = {'articles': articles}
    """
    return render(request, 'vitrine/index.html')

def mentions_legales(request):
    cv = CVPDF.objects.get(id=1)
    context = {'cv': cv}
    return render(request, 'vitrine/mentions.html', context)

def plan(request):
    return render(request, 'vitrine/plan.html')

