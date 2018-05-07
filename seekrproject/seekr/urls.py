from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('companies', views.CompanyList.as_view(), name='company_list')
]

# will write other urls when model is updated and migrated correctly