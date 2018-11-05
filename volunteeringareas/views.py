from rest_framework import generics
from .models import VolunteeringArea
from .serializers import VolunteeringAreaSerializer

class VolunteeringAreaMixin:	
	serializer_class = VolunteeringAreaSerializer
	permission_classes = ()

	def get_queryset(self):
		return VolunteeringArea.objects.all()


class VolunteeringAreaRetrieve(VolunteeringAreaMixin, generics.RetrieveAPIView):
    pass

class VolunteeringAreaList(VolunteeringAreaMixin, generics.ListCreateAPIView):
	def perform_create(self, serializer):
		volunteeringArea = serializer.save()