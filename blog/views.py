from multiprocessing import context
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from APIREST.models import Project, Skill, Badge
import math   


def blogs(request):
    # Set up Paginator
    p = Paginator(Project.objects.all(), 9)
    page = request.GET.get('page')
    p_projects = p.get_page(page)
    nums_pages = "a" * p_projects.paginator.num_pages

    projects = []
    for project in  p_projects:
        badges = Badge.objects.filter(projects__id=project.id)
        skills = Skill.objects.filter(projects__id=project.id)
        projects.append({'project':project, 'badges':badges, 'skills':skills})
    
    context = {'projects': projects, 'p_projects': p_projects, 'nums_pages': nums_pages}
    return render(request, 'blog/blogs.html', context)

def blog(request, blog_id):
    #article = get_object_or_404(Article, pk=blog_id)
    #context = {'article': article}
    return render(request, 'blog/blog.html')
