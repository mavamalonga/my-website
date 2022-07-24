from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from APIREST.models import Project, Badge, Task
from APIREST.serializers import ProjectSerializer, BadgeSerializer, TaskSerializer


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
       

class BadgeViewset(ModelViewSet):

    serializer_class = BadgeSerializer

    def get_queryset(self):
        return Badge.objects.all()


class TaskViewset(ModelViewSet):

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()



