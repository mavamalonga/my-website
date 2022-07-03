from multiprocessing import context
from django.shortcuts import render
from APIREST.models import Project, Skill, Badge

def home(request):
    projects = []
    for project in  Project.objects.filter(pk__in=[2, 3]):
        badges = Badge.objects.filter(projects__id=project.id)
        skills = Skill.objects.filter(projects__id=project.id)
        projects.append({'project':project, 'badges':badges, 'skills':skills})
    context = {'projects': projects}
    return render(request, 'my_profile/home.html', context)