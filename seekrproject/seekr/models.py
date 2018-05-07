from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    glassdoor_link = models.TextField()

    def __str__(self):
        return self.name
    
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    requirements = models.TextField()
    salary_range_start = models.PositiveIntegerField()
    salary_range_end = models.PositiveIntegerField()
    source = models.CharField()
    notes = models.TextField()
    date_posted = models.DateField()
    todo_list = models.ManyToManyField(Todo_Item)
    job_status = models.CharField(
        max_length = 100,
        choices = (
            ('Applied', 'Applied',),
            ('First Contact', 'First Contact',),
            ('Interview', 'Interview',),
            ('Offer', 'Offer',),
            ('Rejected', 'Rejected',),

        ),
        unique = True
    )
 def __str__(self):
        return self.title

class Todo_Item(models.Model):
    status = models.BooleanField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

