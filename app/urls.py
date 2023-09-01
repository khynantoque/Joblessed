from django.urls import path

from app import views

urlpatterns = [
    path('', views.job_list, name='jobs_list'),
    path('job/<int:jobid>', views.job_detail, name='jobs_detail')
]

