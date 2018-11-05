from rest_framework import serializers
from jobs.models import Job, JobMatch
from companies.models import Company
from volunteers.models import Volunteer
from volunteeringareas.models import VolunteeringArea
from volunteers.serializers import VolunteerSerializer
from companies.serializers import CompanySerializer
from volunteeringareas.serializers import VolunteeringAreaSerializer
from rest_framework.serializers import PrimaryKeyRelatedField


class CompanyFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

	def get_queryset(self):
		request = self.context.get('request', None)
		queryset = super(CompanyFilteredPrimaryKeyRelatedField, self).get_queryset()
		identificator = request.data['company']
		if not request or not queryset:
			return None
		return queryset.filter(pk=identificator) 


class VolunteerFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

	def get_queryset(self):
		request = self.context.get('request', None)
		queryset = super(VolunteerFilteredPrimaryKeyRelatedField, self).get_queryset()
		identificator = request.data['volunteer']
		if not request or not queryset:
			return None
		return queryset.filter(pk=identificator) 


class JobAreaFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

	def get_queryset(self):
		request = self.context.get('request', None)
		queryset = super(JobAreaFilteredPrimaryKeyRelatedField, self).get_queryset()
		identificator = request.data['job_areas']
		if not request or not queryset:
			return None
		return queryset.filter(pk=identificator) 					  


class JobSerializer(serializers.ModelSerializer):
  
  	company = CompanyFilteredPrimaryKeyRelatedField(queryset=Company.objects)
  	job_areas = PrimaryKeyRelatedField(read_only=True, many=True)

  	class Meta:

  		model = Job
  		fields = ('id', 'company', 'title', 'description', 'photo', 'start_date', 'finish_date', 'recurrency', 'job_areas', 
  			'contact_email', 'state', 'city', 'neighborhood', 'street', 'street_number', 'extra_location', 'is_active')
  		read_only_fields = ('created_at', )

  	def to_representation(self, instance):
  		representation = super(JobSerializer, self).to_representation(instance)
  		#representation['company'] = CompanySerializer(instance.company.all()).data
  		representation['job_areas'] = VolunteeringAreaSerializer(instance.job_areas.all(), many=True).data
  		return representation


class JobMatchSerializer(serializers.ModelSerializer):

	company = CompanyFilteredPrimaryKeyRelatedField(queryset=Company.objects)
	volunteer = VolunteerFilteredPrimaryKeyRelatedField(queryset=Volunteer.objects)
	job_areas = JobAreaFilteredPrimaryKeyRelatedField(queryset=VolunteeringArea.objects)

	class Meta:

		model = JobMatch
		fields = ('id', 'company', 'volunteer', 'job_areas', 'attended_job', 'company_commentary', 'volunteer_commentary')
		read_only_fields = ('created_at', )

	def to_representation(self, instance):
		
		representation = super(JobMatchSerializer, self).to_representation(instance)
		representation['company'] = CompanySerializer(instance.company).data
		representation['volunteer'] = VolunteerSerializer(instance.volunteer).data
		representation['job_areas'] = VolunteeringAreaSerializer(instance.job_areas).data
		return representation