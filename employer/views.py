# employer/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobListingForm
from .models import JobListing
from django.contrib.auth import logout
from seeker.models import JobApplication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AcceptApplicationForm
from .forms import JobForm


@login_required
def employer_dashboard(request):
    if request.user.groups.filter(name='Employer').exists():
        # Render employer dashboard
        return render(request, 'employer_dashboard.html')
    else:
        messages.error(request, "You don't have permission to access this page.")
        return redirect('seeker_dashboard')


def post_job(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_job')  # Redirect to employer dashboard after posting job
    else:
        form = JobListingForm()
    return render(request, 'post_job.html', {'form': form})


def job_list(request):
    job_listings = JobListing.objects.all()
    return render(request, 'job_list.html', {'job_listings': job_listings})


def edit_job(request, job_id):
    # Fetch the job listing to be edited
    job = get_object_or_404(JobListing, id=job_id)

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = JobListingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to job listings page after editing job
    else:
        # If the request method is GET, render the form with the job listing data
        form = JobListingForm(instance=job)

    return render(request, 'edit_job.html', {'form': form})


def delete_job(request, job_id):
    # Fetch the job listing to be deleted
    job = get_object_or_404(JobListing, id=job_id)

    if request.method == 'POST':
        # If the request method is POST, delete the job listing and redirect to job listings page
        job.delete()
        return redirect('job_list')

    # Render a confirmation page (optional) if the request method is GET
    return render(request, 'employer/delete_job_confirm.html', {'job': job})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


def view_job_applications(request, job_id):
    job = JobListing.objects.get(pk=job_id)
    applications = JobApplication.objects.filter(job=job)
    return render(request, 'view_job_applications.html', {'job': job, 'applications': applications})



def accept_application(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    if request.method == 'POST':
        form = AcceptApplicationForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For demonstration, let's assume the form contains a message field
            message = form.cleaned_data['message']
            # Perform any additional actions here, such as sending notifications
            # or updating the application status
            # For now, let's just display a success message
            messages.success(request, f'Application from {application.user.username} accepted. Message: {message}')
            return redirect('acceptance_success')
    else:
        form = AcceptApplicationForm()
    return render(request, 'acceptance_success.html', {'application': application, 'form': form})


def acceptance_success(request):
    return render(request, 'acceptance_success.html')


def new_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new job listing
            form.save()
            messages.success(request, 'Job listing created successfully!')
            return redirect('new_job')  # Redirect to the same page or any other page
    else:
        form = JobForm()
    return render(request, 'new_job.html', {'form': form})
