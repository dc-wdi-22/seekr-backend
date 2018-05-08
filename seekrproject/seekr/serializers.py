from rest_framework import serializers
from .models import Company, Job, TodoItem

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(
        view_name = 'job-detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = Company
        fields = ('name', 'industry', 'address', 'url', 'glassdoor_link', 'jobs',)

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    job = serializers.HyperlinkedRelatedField(
        view_name = 'job-detail',
        read_only = True
    )
    class Meta:
        model = TodoItem
        fields = ('status', 'name', 'job')

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    todo_list = TodoItemSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = ('company', 'title', 'description', 'requirements', 'salary_range_start', 'salary_range_end', 'source', 'notes', 'date_posted', 'todo_list', 'job_status',)

