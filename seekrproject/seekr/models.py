from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    glassdoor_link = models.TextField()

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    status = models.BooleanField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    
class Job(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    requirements = models.TextField(blank=True)
    salary_range_start = models.PositiveIntegerField()
    salary_range_end = models.PositiveIntegerField()
    source = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    date_posted = models.DateField()
    todo_list = models.ManyToManyField(TodoItem)
    job_status = models.CharField(
        max_length = 100,
        choices = (
            ('Applied', 'Applied',),
            ('First Contact', 'First Contact',),
            ('Interview', 'Interview',),
            ('Offer', 'Offer',),
            ('Rejected', 'Rejected',),

        ),
        unique = True,
        blank=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    def __str__(self):
        return self.title

