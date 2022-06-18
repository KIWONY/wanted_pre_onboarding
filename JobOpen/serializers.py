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

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.country)
        instance.region = validated_data.get('region', instance.region)
        instance.position = validated_data.get('position', instance.position)
        instance.compensation = validated_data.get('compensation', instance.compensation)
        instance.description = validated_data.get('description', instance.description)
        instance.skills = validated_data.get('skills', instance.skills)
        return instance
