from rest_framework import generics
#from users.models import CustomUser
from .models import Company
from .serializers import CompanySerializer

class CompanyMixin:	
	serializer_class = CompanySerializer

	def get_queryset(self):
		return Company.objects.all()


class CompanyRetrieveUpdate(CompanyMixin, generics.RetrieveUpdateAPIView):
    pass

class CompanyListCreate(CompanyMixin, generics.ListCreateAPIView):
	def perform_create(self, serializer):
		company = serializer.save()