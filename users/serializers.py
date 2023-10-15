from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import WTSUser, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class WTSUserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(required=False, read_only=True)

    class Meta:
        model = WTSUser
        fields = ['username', 'company']
