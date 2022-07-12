from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from dashboard.views import index, mentions_legales
from projects.views import projects


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('project/', projects, name='projects'),
    path('mentions-legales/', mentions_legales, name='mentions-legales'),
    path('sentry-debug/', trigger_error),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
