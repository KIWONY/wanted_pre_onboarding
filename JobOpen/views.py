from django.shortcuts import render
#
# # Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets, mixins, status
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response

# from Company.permissions import IsCompanyOrReadOnly
from JobOpen.models import JobOpen

from JobOpen.serializers import JobOpenSerializer, JobOpenDetailSerializer, JobCreateSerializer

# # ---------------검색기능을 추가한 view ------------------
# User가 접근할 수 있는 list
class JobSearchList(generics.ListAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobOpenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company__company_name','country','region','position','skills']



# User가 상세목록 조회할 수 있는 view
class JobDetailView(RetrieveAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobOpenDetailSerializer
    lookup_field = "id"



# 회사가 채용공고 생성, 조회할 수 있는 view
class JobCreateView(ListCreateAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobCreateSerializer

    def list(self, request):
        queryset =self.get_queryset()
        serializer = JobCreateSerializer(queryset, many=True)
        return Response(serializer.data)


# 회사가 채용공고 업데이트,삭제할 수 있는 view
class JobUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobCreateSerializer
    lookup_field = "id"

