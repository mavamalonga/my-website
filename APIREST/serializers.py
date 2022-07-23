from rest_framework.serializers import ModelSerializer
from APIREST.models import Project


class ProjectSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = ('id', 'title', 'description', 'image', 'github', 'website')