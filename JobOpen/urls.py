from django.urls import path

from JobOpen.views import JobListView, JobSearch

urlpatterns = [
    path('', JobListView.as_view()),
    path('search/', JobSearch.as_view()),
]