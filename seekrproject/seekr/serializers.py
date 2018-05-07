from rest_framework import serializers
from .models import Company, Job, ToDo_Item

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True
    )
    class Meta:
        model = Company
        fields = ()

class JobSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.HyperlinkedRelatedField(
        read_only = True
    )
    todoitems = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True
    )
    class Meta:
        model = Job
        fields = ()

class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    job = serializers.HyperlinkedRelatedField(
        read_only = True
    )
    class Meta:
        model = ToDoItem
        fields = ()