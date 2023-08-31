from django.http import HttpResponse
from django.shortcuts import render

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
        html += f'<li><a href="job/{i}">{j}</a></li>'
    return HttpResponse(f'<html><ol>{html}</ol></html>')


def job_detail(request, id):
    return HttpResponse(f'<h1>{jobs[id]}</h1><h3>{details[id]}</h3>')
