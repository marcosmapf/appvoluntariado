from rest_framework import serializers
from rest_framework.serializers import PrimaryKeyRelatedField
from volunteers.models import Volunteer
from volunteeringareas.serializers import VolunteeringAreaSerializer
from volunteeringareas.models import VolunteeringArea


class VolunteerSerializer(serializers.ModelSerializer):

	interest_areas = PrimaryKeyRelatedField(read_only=True, many=True)

	class Meta:
		model = Volunteer
		fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'state', 'gender', 'interest_areas', 'city', 'description', 'photo')
		read_only_fields = ('created_at', )

	def to_representation(self, instance):
		representation = super(VolunteerSerializer, self).to_representation(instance)
		representation['interest_areas'] = VolunteeringAreaSerializer(instance.interest_areas.all(), many=True).data
		return representation 		