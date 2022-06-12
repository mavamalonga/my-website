from django.contrib import admin
from django.urls import path
from vitrine.views import index
from blog.views import blogs, blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog, name='blog')
]
