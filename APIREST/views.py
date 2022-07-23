from rest_framework.viewsets import ModelViewSet
from APIREST.models import Project
from APIREST.serializers import ProjectSerializer


class ProjectViewset(ModelViewSet):

	serializer_class = ProjectSerializer

	def get_queryset(self):
		return Project.objects.all()

    