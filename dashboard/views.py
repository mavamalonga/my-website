from multiprocessing import context
from django.shortcuts import render, redirect
from APIREST.models import Project, Skill, Badge, CVPDF

def index(request):
    projects = []
    cv = CVPDF.objects.get(id=1)
    for project in  Project.objects.filter(pk__in=[2, 4]):
        badges = Badge.objects.filter(projects__id=project.id)
        skills = Skill.objects.filter(projects__id=project.id)
        projects.append({'project':project, 'badges':badges, 'skills':skills})
    context = {'projects': projects,'cv': cv, 'page_name': 'dashboard'}
    return render(request, 'dashboard/index.html', context)

def mentions_legales(request):
    return render(request, 'dashboard/mentions.html', context)


