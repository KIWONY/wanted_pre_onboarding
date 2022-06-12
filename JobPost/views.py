from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from JobPost.models import JobPost
from JobPost.serializers import JobPostSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    def perform_create(self, serializer):
        serializer.save()
