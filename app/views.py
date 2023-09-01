from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import redirect

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


# Create your views here.
def job_list(request):
    html = ''
    for i, j in enumerate(jobs):
        html += f'<li><a href="{reverse("jobs_detail", args=(i,))}">{j}</a></li>'
    return HttpResponse(f'<html><ol>{html}</ol></html>')


def job_detail(request, jobid):
    try:
        if jobid == 0:
            return redirect(reverse('jobs_list'))
        return HttpResponse(f'<h1>{jobs[jobid]}</h1><h3>{details[jobid]}</h3>')
    except:
        return HttpResponseNotFound('Not Found')
