from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from my_profile.views import home
from vitrine.views import index, mentions_legales
from blog.views import blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', index, name='index'),
    path('blogs/', blogs, name='blogs'),
    path('mentions-legales/', mentions_legales, name='mentions'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
