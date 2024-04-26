# seeker/models.py

from django.db import models
from django.contrib.auth.models import User
from employer.models import JobListing


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    # Add more fields as needed
