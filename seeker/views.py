# seeker/views.py

from django.shortcuts import render, redirect
from employer.models import JobListing
from .models import JobApplication
from .forms import FeedbackForm



def seeker_dashboard(request):
    return render(request, 'dashboard.html')


def job_listings(request):
    # Fetch all job listings
    job_listings = JobListing.objects.all()

    context = {
        'job_listings': job_listings
    }

    return render(request, 'job_listings.html', context)


def apply_for_job(request, job_id):
    if request.method == 'POST':
        # Retrieve the job listing
        job = JobListing.objects.get(pk=job_id)
        # Create a job application object
        application = JobApplication(
            user=request.user,
            job=job,
            cover_letter=request.POST['cover_letter']
            # Add more fields as needed
        )
        # Save the job application
        application.save()
        # Redirect to a success page or the job listings page
        return redirect('job_listings')  # Change this to the appropriate URL
    else:
        # Handle GET request (show application form)
        return render(request, 'apply_for_job.html', {'job_id': job_id})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send email, save to database)
            # In this example, we're just rendering a success page
            return render(request, 'feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def view_jobs(request):
    job_type = request.GET.get('job_type')
    job_listings = JobListing.objects.filter(job_type=job_type)
    context = {'job_listings': job_listings}
    return render(request, 'view_jobs.html', context)


def view_notifications(request):
    notifications = request.session.get('notifications', [])
    return render(request, 'notifications.html', {'notifications': notifications})
