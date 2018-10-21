from rest_framework import serializers
from jobs.models import Job
from companies.serializers import CompanySerializer
from volunteeringareas.serializers import VolunteeringAreaSerializer

class JobSerializer(serializers.ModelSerializer):
  
    company = CompanySerializer()
    job_areas = VolunteeringAreaSerializer(many=True)

    class Meta:

        model = Job
        fields = ('id', 'company', 'title', 'description', 'photo', 'start_date', 'finish_date', 'recurrency', 'job_areas', 
    		'contact_email', 'state', 'city', 'neighborhood', 'street', 'street_number', 'extra_location', 'is_active')
        read_only_fields = ('created_at', )