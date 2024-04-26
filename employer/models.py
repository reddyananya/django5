# employer/models.py

from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=20,)  # Add job_type field without choices
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

