from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from dashboard.views import index, mentions_legales
from projects.views import projects
from portfolio.views import handler404, handler500
from django.views.static import serve

handler404 = "portfolio.views.handler404"
handler500 = "portfolio.views.handler500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('project/', projects, name='projects'),
    path('mentions-legales/', mentions_legales, name='mentions-legales'),
]

# The URL to use when referring to static files (where they will be served from)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
    {'document_root': settings.MEDIA_ROOT, }), ]
