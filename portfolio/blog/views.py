from django.shortcuts import render
from blog.models import Article 


def blogs(request):
    articles = Article.objects.all()
    articles = sorted(articles, key=lambda k:k.date_published, reverse=True)
    context = {'articles': articles}
    return render(request, 'app/blogs.html')

def blog(request, blog_id):
    article = Article.objects.get(id=blog_id)
    context = {'article': article}
    return render(request, 'app/blog.html')