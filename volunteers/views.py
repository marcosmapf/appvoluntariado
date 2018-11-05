from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Volunteer
from .serializers import VolunteerSerializer

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class VolunteerMixin:	

	serializer_class = VolunteerSerializer
	permission_classes = ()
	renderer_classes = (JSONRenderer, )

	def get_queryset(self):
		return Volunteer.objects.all()


class VolunteerRetrieveUpdate(VolunteerMixin, generics.RetrieveUpdateAPIView):
	
	def put(self, request, pk, format=None):
		queryset = self.get_queryset()
		volunteer = get_object_or_404(queryset, pk=pk)
		volunteer_data = VolunteerSerializer(volunteer).data

		if 'interest_areas' in request.data:
			interest_areas = request.data.pop("interest_areas")
		else:
			interest_areas = []
			for key in volunteer_data['interest_areas']:
				interest_areas.append(key.get('id'))

		for field in request.data:
			volunteer_data[field] = request.data.get(field)			

		modified_serializer = VolunteerSerializer(data=volunteer_data)

		if modified_serializer.is_valid():
			self.perform_update(modified_serializer, interest_areas)
			return Response(modified_serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def perform_update(self, serializer, interest_areas):
		volunteer = serializer.save()
		volunteer.interest_areas.add(*interest_areas)


class VolunteerListCreate(VolunteerMixin, generics.ListCreateAPIView):

	parser_classes = (JSONParser,)

	def create(self, request, *args, **kwargs):
		interest_areas = request.data.pop('interest_areas', [])
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer, interest_areas)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


	def perform_create(self, serializer, interest_areas):
		volunteer = serializer.save()
		volunteer.interest_areas.add(*interest_areas)