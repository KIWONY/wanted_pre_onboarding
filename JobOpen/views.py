from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListAPIView

from JobOpen.models import JobOpen
from JobOpen.serializers import JobOpenSerializer



class ListJobView(generics.ListCreateAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobOpenSerializer


