from rest_framework import serializers
from .models import Company, Job, TodoItem

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(
        view_name = 'job_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = Company
        fields = ('name', 'industry', 'address', 'url', 'glassdoor_link', 'jobs',)

class JobSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.HyperlinkedRelatedField(
        view_name = 'company_detail',
        read_only = True
    )
    todoitems = serializers.HyperlinkedRelatedField(
        view_name = 'to_do_item_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = Job
        fields = ('company', 'title', 'description', 'requirements', 'salary_range_start', 'salary_range_end', 'source', 'notes', 'date_posted', 'todo_list', 'job_status',)

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    job = serializers.HyperlinkedRelatedField(
        view_name = 'job_detail',
        read_only = True
    )
    class Meta:
        model = TodoItem
        fields = ('status', 'name')
