from django.urls import path
from . import views

urlpatterns = [
    path('get', views.get_jobs, name='get_jobs'),
    path('get/<int:pk>', views.get_job, name='get_job'),
    path('get-recruiter-job', views.get_recruiter_jobs, name='get_recruiter_jobs'),
    path('post', views.post_job, name='post_job'),
]
