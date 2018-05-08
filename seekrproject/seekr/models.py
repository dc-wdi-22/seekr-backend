from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    glassdoor_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    status = models.NullBooleanField()
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


    
class Job(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    salary_range_start = models.PositiveIntegerField(null=True)
    salary_range_end = models.PositiveIntegerField(null=True)
    source = models.CharField(max_length=100, null=True)
    notes = models.TextField(blank=True, null=True)
    date_posted = models.DateField(null=True)
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
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    def __str__(self):
        return self.title

