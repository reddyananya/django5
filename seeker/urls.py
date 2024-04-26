# seeker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
    path('job_listings/', views.job_listings, name='job_listings'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('feedback/', views.feedback, name='feedback'),
    path('view_jobs/', views.view_jobs, name='view_jobs'),
    path('notifications/', views.view_notifications, name='view_notifications'),

]
