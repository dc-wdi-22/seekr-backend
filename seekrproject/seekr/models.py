from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    glassdoor_link = models.TextField()
    
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=100)
    requirements = models.TextField()
    salary_range_start = models.PositiveIntegerField()
    salary_range_end = models.PositiveIntegerField()
    source = models.TextField()
    date_posted = models.DateField()
