from rest_framework import serializers
from companies.models import Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'trading_name', 'company_sector', 'company_location', 'website', 'phone', 'email', 'logo', 'description', 'created_at',]
