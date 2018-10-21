from rest_framework import serializers
from volunteers.models import Volunteer
from volunteeringareas.serializers import VolunteeringAreaSerializer


class VolunteerSerializer(serializers.ModelSerializer):

	interest_areas = VolunteeringAreaSerializer(many=True)

	class Meta:
		model = Volunteer
		fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'state', 'gender', 'interest_areas', 'city', 'description', 'photo')
		read_only_fields = ('created_at', )
