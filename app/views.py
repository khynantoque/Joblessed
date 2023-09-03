from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import redirect, render
from django.template import loader

jobs = [
    'First Job',
    'Second Job',
    'Third Job'
]

details = [
    'First Description',
    'Second Description',
    'Third Description'
]


def hello(request):
    user = ['khyn', 'antoque']
    context = {'title': 'Django', 'name': user, 'age': 22}
    return render(request, 'app/hello.html', context)


# Create your views here.
def job_list(request):
    context = {'jobs': jobs}
    return render(request, 'app/job_list.html', context)

def job_detail(request, jobid):
    try:
        if jobid == 0:
            return redirect(reverse('jobs_list'))
        context = {'job': jobs[jobid], 'detail': details[jobid]}
        return render(request, 'app/job_detail.html', context)
    except:
        return HttpResponseNotFound('Not Found')
