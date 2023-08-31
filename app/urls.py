from django.urls import path

from app import views

urlpatterns = [
    path('', views.job_list),
    path('job/<int:id>', views.job_detail)
]

