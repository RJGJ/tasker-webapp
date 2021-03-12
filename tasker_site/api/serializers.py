from rest_framework import serializers

from tasker_frontend.models import Company, Department, Task, Log


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
