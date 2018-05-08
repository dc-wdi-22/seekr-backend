from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('companies', views.CompanyList.as_view(), name='company-list'),
    path('jobs', views.JobList.as_view(), name='job-list'),
    path('company/<int:id>', views.CompanyDetail.as_view(), name='company-detail'),
    path('job/<int:id>', views.JobDetail.as_view(), name='job-detail'),
    path('todos/<int:id>', views.TodoItemDetail.as_view(), name='todo-detail')
]

# will write other urls when model is updated and migrated correctly
