from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from APIREST.models import User, Photo, Badge, Skill, Project
admin.autodiscover()


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
    list_display = ('title', 'id')
    filter_horizontal = ('projects', )


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('description', 'id')
    filter_horizontal = ('projects', )


admin.site.register(Photo)



