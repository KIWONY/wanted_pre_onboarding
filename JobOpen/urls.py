from django.urls import path
from JobOpen.views import JobSearchList, JobDetailView, JobUpdateDeleteView, JobCreateView




urlpatterns = [
    path('', JobSearchList.as_view()),
    path('<int:id>/',JobDetailView.as_view()),
    path('post/',JobCreateView.as_view()),
    path('post/<int:id>/',JobUpdateDeleteView.as_view()),

]