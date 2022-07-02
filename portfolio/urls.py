from django.contrib import admin
from django.urls import path
from my_profile.views import home
from vitrine.views import index, mentions_legales
from blog.views import blogs, blog
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', index, name='index'),
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog, name='blog'),
    path('mentions-legales/', mentions_legales, name='mentions'),
]
