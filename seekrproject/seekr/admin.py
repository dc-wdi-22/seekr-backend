from django.contrib import admin
from .models import Company, Job, TodoItem,

# Register your models here.
admin.site.register([Company, Job, TodoItem])
