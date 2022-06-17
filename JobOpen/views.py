from django.shortcuts import render
#
# # Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets, mixins
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response

# from Company.permissions import IsCompanyOrReadOnly
from JobOpen.models import JobOpen

from JobOpen.serializers import JobOpenSerializer, JobOpenDetailSerializer, JobCreateSerializer


# class JobPostViewSet(viewsets.ModelViewSet):
#     queryset = JobOpen.objects.all()
#     serializer_class = JobOpenSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
# # ---------------검색기능을 추가한 view ------------------
# User가 접근할 수 있는 list
# # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
class JobSearchList(generics.ListAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobOpenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company','country','region','position','skills']


#
# https://www.django-rest-framework.org/api-guide/generic-views/#examples
# 회사가 채용공고 생성, 조회
class JobCreateView(ListCreateAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobCreateSerializer

    def list(self, request):
        queryset =self.get_queryset()
        serializer = JobCreateSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(company_name=self.request.user)


class JobUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobCreateSerializer




# 사용자가 상세목록 조회
class JobDetailView(RetrieveAPIView):
    queryset = JobOpen.objects.all()
    serializer_class = JobOpenDetailSerializer
    lookup_field = "id"


# https://stackoverflow.com/questions/67700941/how-to-access-other-model-field-from-serializer-related-field