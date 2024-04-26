# employer/forms.py

from django import forms
from .models import JobListing


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'company', 'salary', 'job_type']  # Add 'job_type' field


class AcceptApplicationForm(forms.Form):
    message = forms.CharField(label='Message', widget=forms.Textarea)
    # You can add more fields as needed


class JobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'company', 'salary', 'job_type']  # Add or remove fields as needed
