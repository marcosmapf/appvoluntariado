from rest_framework import generics, status
from .models import Volunteer
from .serializers import VolunteerSerializer

from rest_framework.parsers import JSONParser
from rest_framework.response import Response

class VolunteerMixin:	

	serializer_class = VolunteerSerializer
	permission_classes = ()

	def get_queryset(self):
		return Volunteer.objects.all()


class VolunteerRetrieveUpdate(VolunteerMixin, generics.RetrieveUpdateAPIView):
	pass
	#def put(self, request, pk, format=None):
		#queryset = Volunteer.objects.all()
		#get_object_or_404(queryset, pk=pk)
		#serializer = SnippetSerializer(snippet, data=request.data)
		#if serializer.is_valid():
			#serializer.save()
			#return Response(serializer.data)
		#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VolunteerListCreate(VolunteerMixin, generics.ListCreateAPIView):

	parser_classes = (JSONParser,)

	def create(self, request, *args, **kwargs):
		interest_areas = request.data.pop('interest_areas')
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer, interest_areas)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


	def perform_create(self, serializer, interest_areas):
		volunteer = serializer.save()
		volunteer.interest_areas.add(*interest_areas)