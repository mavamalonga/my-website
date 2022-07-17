# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from APIREST.models import Project, Task, Badge, CurriculumVitae


def index(request):
    # collect curriculum vitae and top projects objects
    curriculum_vitae = get_object_or_404(CurriculumVitae, pk=1)
    my_objects = Project.objects.filter(pk__in=[2, 4])

    # return an error if there are no projects
    if not my_objects:
        raise Http404("Projects does not exist")

    # collects badges and tasks for each project
    projects = [{'project': project, 'badges': Badge.objects.filter(projects__id=project.id),
    'tasks': Task.objects.filter(projects__id=project.id)} for project in my_objects]

    return render(request, 'dashboard/index.html', {'projects': projects,
        'curriculum_vitae': curriculum_vitae})


def mentions_legales(request):
    # collect cv and top projects objects
    curriculum_vitae = get_object_or_404(CurriculumVitae, pk=1)
    return render(request, 'dashboard/mentions.html', {'curriculum_vitae': curriculum_vitae})
