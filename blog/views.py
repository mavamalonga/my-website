from multiprocessing import context
import django
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from APIREST.models import Project, Skill, Badge
import math   


def blogs(request):
    if request.GET.get('filter') == 'python':
        projects = []
        only_projects = []
        for project in  Project.objects.all():
            badges = Badge.objects.filter(projects__id=project.id)
            python_badges = Badge.objects.filter(name__in=['Python', 'Django', 'Flask'])

            if python_badges[0] in badges:
                skills = Skill.objects.filter(projects__id=project.id)
                projects.append({'project':project, 'badges':badges, 'skills':skills})
                only_projects.append(project)
                continue
            elif python_badges[1] in badges:
                skills = Skill.objects.filter(projects__id=project.id)
                projects.append({'project':project, 'badges':badges, 'skills':skills})
                only_projects.append(project)
                continue
            elif python_badges[2] in badges:
                skills = Skill.objects.filter(projects__id=project.id)
                projects.append({'project':project, 'badges':badges, 'skills':skills})
                only_projects.append(project)
                continue
        
        # Set up Paginator
        p = Paginator(only_projects, 9)
        page = request.GET.get('page')
        p_projects = p.get_page(page)
        nums_pages = "a" * p_projects.paginator.num_pages

        context = {'projects': projects, 'p_projects': p_projects, 'nums_pages': nums_pages}
        return render(request, 'blog/blogs.html', context)


    if request.GET.get('filter') == 'django':
        projects = []
        only_projects = []
        for project in  Project.objects.all():
            badges = Badge.objects.filter(projects__id=project.id)
            django_badge = Badge.objects.get(name='Django')

            if django_badge in badges:
                skills = Skill.objects.filter(projects__id=project.id)
                projects.append({'project':project, 'badges':badges, 'skills':skills})
                only_projects.append(project)
                continue
        
        # Set up Paginator
        p = Paginator(only_projects, 9)
        page = request.GET.get('page')
        p_projects = p.get_page(page)
        nums_pages = "a" * p_projects.paginator.num_pages

        context = {'projects': projects, 'p_projects': p_projects, 'nums_pages': nums_pages}
        return render(request, 'blog/blogs.html', context)




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
