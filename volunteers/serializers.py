from rest_framework import serializers
from volunteers.models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = ['id', 'first_name', 'last_name', 'state', 'city', 'gender', 'phone', 'email', 'description', 'photo']
