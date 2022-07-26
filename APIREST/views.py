# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from APIREST.models import Project, Badge, Task
from APIREST.serializers import ProjectSerializer, BadgeSerializer, TaskSerializer
from APIREST.permissions import StaffPermission


class ProjectViewset(ModelViewSet):
    permission_classes = [StaffPermission]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all().order_by('id')


class BadgeViewset(ModelViewSet):
    permission_classes = [StaffPermission]
    serializer_class = BadgeSerializer

    def get_queryset(self):
        return Badge.objects.all()


class TaskViewset(ModelViewSet):
    permission_classes = [StaffPermission]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()
