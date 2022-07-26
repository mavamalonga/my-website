# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from APIREST.models import Project, Badge, Task


class BadgeSerializer(ModelSerializer):
    class Meta:
        read_only_fields = ('is_active',)
        model = Badge
        fields = ('id', 'name', 'color', 'projects')


class TaskSerializer(ModelSerializer):
    class Meta:
        read_only_fields = ('is_active',)
        model = Task
        fields = ('id', 'title', 'description', 'projects')


class ProjectSerializer(ModelSerializer):
    badges = SerializerMethodField()
    tasks = SerializerMethodField()

    class Meta:
        read_only_fields = ('is_active',)
        model = Project
        fields = ('id', 'title', 'description', 'image', 'framework', 'github',
        'website', 'badges', 'tasks')

    def get_badges(self, instance):
        queryset = Badge.objects.filter(projects__id=instance.id)
        serializer = BadgeSerializer(queryset, many=True)
        return serializer.data

    def get_tasks(self, instance):
        queryset = Task.objects.filter(projects__id=instance.id)
        serializer = TaskSerializer(queryset, many=True)
        return serializer.data
