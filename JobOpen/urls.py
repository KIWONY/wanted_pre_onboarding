from django.urls import path
from JobOpen.views import JobSearchList, JobDetail
#
# # from JobOpen.views import JobListView, JobSearch
#
#
#
urlpatterns = [
#     # path('', JobListView.as_view()),
    path('', JobSearchList.as_view()),
    path('<int:id>/',JobDetail.as_view())
#     # path('<int:id>/',JobDetail.as_view()),
]