from django.shortcuts import get_object_or_404, render
#from blog.models import Article 


def blogs(request):
    """
    articles = Article.objects.all()
    articles = sorted(articles, key=lambda k:k.date_published, reverse=True)
    context = {'articles': articles}
    """
    return render(request, 'blog/blogs.html')

def blog(request, blog_id):
    #article = get_object_or_404(Article, pk=blog_id)
    #context = {'article': article}
    return render(request, 'blog/blog.html')
