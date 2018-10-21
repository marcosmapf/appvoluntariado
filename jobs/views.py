from rest_framework import generics
from .models import Job as JobModel
from .serializers import JobSerializer

class JobMixin:	
	serializer_class = JobSerializer
	permission_classes = ()

	def get_queryset(self):
		return JobModel.objects.all()


class JobRetrieveUpdate(JobMixin, generics.RetrieveUpdateAPIView):
    pass

class JobListCreate(JobMixin, generics.ListCreateAPIView):
	def perform_create(self, serializer):
		job = serializer.save()

#if professional.github.data_updated_at < limit_outdate:
	#professional.github.data_updated_at = timezone.now()
	#professional.github.save(update_fields=["data_updated_at"])		