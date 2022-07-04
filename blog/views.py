from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from APIREST.models import Project, Skill, Badge


def blogs(request):
    projects = []
    for project in  Project.objects.all():
        badges = Badge.objects.filter(projects__id=project.id)
        skills = Skill.objects.filter(projects__id=project.id)
        projects.append({'project':project, 'badges':badges, 'skills':skills})
    context = {'projects': projects}
    return render(request, 'blog/blogs.html', context)

def blog(request, blog_id):
    #article = get_object_or_404(Article, pk=blog_id)
    #context = {'article': article}
    return render(request, 'blog/blog.html')
