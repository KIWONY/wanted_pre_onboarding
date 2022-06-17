from Company.models import Companys
from JobOpen.models import JobOpen

from rest_framework import serializers

# 조회
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



# 회사 crud serializer
class JobCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOpen
        fields = ['company','country','region','position','compensation','description','skills']

    def create(self, validated_data):
        return JobOpen.objects.create(**validated_data)