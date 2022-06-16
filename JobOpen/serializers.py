from rest_framework import serializers

from Company.serializers import CompanySerializer
from JobOpen.models import JobOpen


class JobOpenSerializer(serializers.ModelSerializer):


    # company = serializers.ReadOnlyField(source="company_name.company")
    class Meta:
        model = JobOpen
        fields = ['id','country','region','position','skills']

    # response[모델명] = ModelSerializer(instance.ForeingKeyField).data
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['Companys'] = CompanySerializer(instance.company).data
        return response



class JobOpenDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOpen
        fields = '__all__'

    def create(self, validated_data):
        return JobOpen.objects.create(**validated_data)


