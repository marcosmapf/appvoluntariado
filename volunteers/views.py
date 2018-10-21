from rest_framework import generics
from .models import Volunteer
from .serializers import VolunteerSerializer

class VolunteerMixin:	
	serializer_class = VolunteerSerializer
	permission_classes = ()

	def get_queryset(self):
		return Volunteer.objects.all()


class VolunteerRetrieveUpdate(VolunteerMixin, generics.RetrieveUpdateAPIView):
    pass

class VolunteerListCreate(VolunteerMixin, generics.ListCreateAPIView):
	def perform_create(self, serializer):
		volunteer = serializer.save()