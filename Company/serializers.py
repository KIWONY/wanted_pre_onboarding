from rest_framework import serializers

from Company.models import Companys


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companys
        fields = '__all__'
        depth = 1