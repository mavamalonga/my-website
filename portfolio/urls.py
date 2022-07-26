from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from knapsack.views import home, mentions, curriculum_vitae
from APIREST.views import ProjectViewset, BadgeViewset, TaskViewset
from portfolio.views import handler404, handler500
from django.views.static import serve
from rest_framework import routers

handler404 = "portfolio.views.handler404"
handler500 = "portfolio.views.handler500"

router = routers.SimpleRouter()
router.register('project', ProjectViewset, basename='project')
router.register('badge', BadgeViewset, basename='badge')
router.register('task', TaskViewset, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('mentions-legales/', mentions, name='mentions-legales'),
    path('curriculum_vitae/', curriculum_vitae, name='curriculum_vitae'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve,
    {'document_root': settings.MEDIA_ROOT, }), ]
