from django.http import HttpResponse
import requests, json
from findjob import helpers

# function based apis

def all_jobs(request):
    """
    This view is usefull to fetch all jobs
    """
    result = helpers.fetch_jobs_data(request)
    return HttpResponse(f"All Jobs = {result}")

def relevant_jobs(request, id):
    """
    This view is usefull to fetch relevant jobs for a user based on there job_type
    """
    result = helpers.fetch_user_jobs(request, id)
    return HttpResponse(f"All Jobs for UserId -> {id} = {result}")
