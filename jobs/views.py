from rest_framework import generics, status
from .models import Job as JobModel
from .models import JobMatch as JobMatchModel
from .serializers import JobSerializer, JobMatchSerializer

from rest_framework.parsers import JSONParser
from rest_framework.response import Response

class JobMixin:	
	serializer_class = JobSerializer
	permission_classes = ()

	def get_queryset(self):
		queryset = JobModel.objects.all()
		job_area = self.request.query_params.get('job_areas', None)
		company = self.request.query_params.get('company', None)
		if job_area is not None:
			queryset = queryset.filter(job_areas=job_area)
		if company is not None:
			queryset = queryset.filter(company=company)
		return queryset

class JobRetrieveUpdate(JobMixin, generics.RetrieveUpdateAPIView):
    pass

class JobListCreate(JobMixin, generics.ListCreateAPIView):

	parser_classes = (JSONParser,)

	def create(self, request, *args, **kwargs):
		job_areas = request.data.pop('job_areas', [])
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer, job_areas)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


	def perform_create(self, serializer, job_areas):
		job = serializer.save()
		job.job_areas.add(*job_areas)


class JobMatchMixin:
	serializer_class = JobMatchSerializer
	permission_classes = ()

	def get_queryset(self):
		return JobMatchModel.objects.all()

class JobMatchRetrieveUpdate(JobMatchMixin, generics.RetrieveUpdateAPIView):
	pass

class JobMatchListCreate(JobMatchMixin, generics.ListCreateAPIView):
	pass
