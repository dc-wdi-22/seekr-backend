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
        fields = ('pk', 'name', 'industry', 'address', 'url', 'glassdoor_link', 'jobs',)

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())
    class Meta:
        model = TodoItem
        fields = ('pk', 'status', 'name', 'job')

class JobSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    todos = serializers.PrimaryKeyRelatedField(
        many = True,
        read_only = True
    )
    # todo_list = TodoItemSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = ('pk', 'company', 'title', 'description', 'requirements', 'salary_range_start', 'salary_range_end', 'source', 'notes', 'date_posted', 'job_status', 'todos',)

