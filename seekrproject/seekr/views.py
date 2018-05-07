from django.shortcuts import render
from rest_framework import generics
from .serializers import JobSerializer, CompanySerializer, ToDoItemSerializer
from .models import Job, Company, ToDoItem

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ToDoItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
