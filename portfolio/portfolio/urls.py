from django.contrib import admin
from django.urls import path
from app.views import index, blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blogs/', blogs, name='blogs'),
]
