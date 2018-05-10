from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    glassdoor_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    salary_range_start = models.PositiveIntegerField(null=True, blank=True)
    salary_range_end = models.PositiveIntegerField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True)
    notes = models.TextField(blank=True, null=True)
    date_posted = models.DateField(null=True, blank=True)
    # todo_list = models.ManyToManyField(TodoItem, blank=True, null=True)
    job_status = models.CharField(
        max_length = 100,
        choices = (
            ('Applied', 'Applied',),
            ('First Contact', 'First Contact',),
            ('Interview', 'Interview',),
            ('Offer', 'Offer',),
            ('Rejected', 'Rejected',),
        ),
        blank=True,
        null=True
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs', blank=True, null=True)
    def __str__(self):
        return self.title

class TodoItem(models.Model):
    status = models.NullBooleanField()
    name = models.CharField(max_length=100, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='todos', blank=True, null=True)

    def __str__(self):
        return self.name