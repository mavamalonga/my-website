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
    # debug filter method
    filter_horizontal = ('badges', 'skills')
    list_display = ('title', 'id')

admin.site.register(Photo)
admin.site.register(Badge)
admin.site.register(Skill)
#admin.site.register(Project)



