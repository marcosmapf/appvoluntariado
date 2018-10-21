from rest_framework import serializers
from volunteeringareas.models import VolunteeringArea

class VolunteeringAreaSerializer(serializers.ModelSerializer):
  
    class Meta:

        model = VolunteeringArea
        fields = ('id', 'title', 'description')
        read_only_fields = ('created_at', 'is_active')