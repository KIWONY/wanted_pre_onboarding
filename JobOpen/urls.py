from django.urls import path

from JobOpen.views import ListJobView



urlpatterns = [
    path('', ListJobView.as_view())
]