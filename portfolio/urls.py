from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from dashboard.views import index, mentions_legales
from projects.views import projects
from portfolio.views import handler404, handler500
from django.views.static import serve
from django.views.decorators.cache import cache_page

handler404 = "portfolio.views.handler404"
handler500 = "portfolio.views.handler500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(60 * 15)(index), name='index'),
    path('project/', cache_page(60 * 15)(projects), name='projects'),
    path('mentions-legales/', mentions_legales, name='mentions-legales'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
    {'document_root': settings.MEDIA_ROOT, }), ]
