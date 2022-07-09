# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from APIREST.models import Project, Skill, Badge, CVPDF


def index(request):
    # collect cv and top projects objects
    curriculum_vitae = get_object_or_404(CVPDF, pk=1)
    my_objects = Project.objects.filter(pk__in=[2, 4])

    # return an error if there are no projects
    if not my_objects:
        raise Http404("Projects does not exist")
    
    # collects badges and skills for each project
    projects = [{'project':project, 'badges':Badge.objects.filter(projects__id=project.id), 
    'skills':Skill.objects.filter(projects__id=project.id)} for project in my_objects]
        
    return render(request, 'dashboard/index.html', {'projects': projects,'cv': curriculum_vitae,
        'page_name': 'dashboard'})
    
def mentions_legales(request):
    return render(request, 'dashboard/mentions.html')
