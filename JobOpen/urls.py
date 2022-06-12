from django.urls import path

from JobOpen.views import JobSearch
# from JobOpen.views import JobListView, JobSearch

urlpatterns = [
    # path('', JobListView.as_view()),
    path('', JobSearch.as_view()),
]