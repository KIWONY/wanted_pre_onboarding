from django.urls import path, include
from rest_framework.routers import DefaultRouter

from JobPost.views import JobPostViewSet

router =DefaultRouter()
router.register('job_post',JobPostViewSet,basename='job_post')


urlpatterns = [
    path('',include(router.urls)),

]