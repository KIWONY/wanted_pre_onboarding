from rest_framework import serializers

from JobOpen.models import JobOpen


class JobOpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpen
        fields = ['id','company','country','region','position','skills']


class JobOpenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpen
        fields = '__all__'