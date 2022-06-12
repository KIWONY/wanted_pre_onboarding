from django.urls import path

from JobOpen.views import JobSearch, JobDetail

# from JobOpen.views import JobListView, JobSearch

urlpatterns = [
    # path('', JobListView.as_view()),
    path('', JobSearch.as_view()),
    path('<int:id>/',JobDetail.as_view())
]