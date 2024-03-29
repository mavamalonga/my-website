# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from APIREST.models import User, Badge, Task, Project, CurriculumVitae, Analytic, Message


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('date_joined', 'groups')
    search_fields = ('username', )


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'id')


@admin.register(Badge)
class BadgeAdmin(ModelAdmin):
    list_display = ('name', 'id')
    filter_horizontal = ('projects', )


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ('description', 'id')
    filter_horizontal = ('projects', )
    search_fields = ('description', )


@admin.register(Analytic)
class AnalyticAdmin(ModelAdmin):
    list_display = ('page_title', 'visits')


@admin.register(CurriculumVitae)
class CurriculumVitaeAdmin(ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('name', 'mail', 'message', 'date')
