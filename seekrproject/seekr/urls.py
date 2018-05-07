from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('jobs', views.JobList.as_view(), name='job_list')
]