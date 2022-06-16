
from JobOpen.models import JobOpen

from rest_framework import serializers


class JobOpenSerializer(serializers.ModelSerializer):
    # source="JobOpen Field.Company field(what field you want to get)"
    company = serializers.ReadOnlyField(source="company.company_name")
    class Meta:
        model = JobOpen
        fields = ['id','company','country','region','position','skills',]


class JobOpenDetailSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source="company.company_name")
    class Meta:
        model = JobOpen
        fields = '__all__'

    def create(self, validated_data):
        return JobOpen.objects.create(**validated_data)


