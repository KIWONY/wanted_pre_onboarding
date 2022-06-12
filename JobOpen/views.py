from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from JobOpen.models import JobOpen
from JobOpen.serializers import JobOpenSerializer



class JobListView(generics.ListCreateAPIView):

    serializer_class = JobOpenSerializer

    def get_queryset(self):
        queryset = JobOpen.objects.all()
        company = self.request.query_params.get('company')
        if company is not None:
            queryset = queryset.filter(purchaser__company=company)
        return queryset


# ---------------검색기능------------------
class JobSearch(generics.ListAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobOpenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company','country','region','position','skills']

