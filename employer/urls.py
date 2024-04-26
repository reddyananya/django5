# employer/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Add URL patterns for employer views here
    path('dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('post_job/', views.post_job, name='post_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('logout/', views.logout_view, name='logout'),
    path('view_applications/<int:job_id>/', views.view_job_applications, name='view_job_applications'),
    path('accept-application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('acceptance_success/', views.acceptance_success, name='acceptance_success'),
    path('new/', views.new_job, name='new_job'),




]
