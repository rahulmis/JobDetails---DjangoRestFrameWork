from findjob import constants
import requests, json
from rest_framework.exceptions import APIException

def fetch_job_type(request, user_id):
    """
    Fetch job type of a particular user through external API 
    """
    try:
        user = requests.get(f'https://63a18b81ba35b96522e0fdaf.mockapi.io/api/users/{user_id}', params=request.GET)
        job_type = json.loads(user.text)['job_type']
        return job_type
    except Exception as e:
        raise APIException("There was a problem!")

def fetch_jobs_data(request):
    """
    Fetch all jobs through an external API
    """
    try:
        all_jobs = requests.get('https://63a18b81ba35b96522e0fdaf.mockapi.io/api/jobs/', params=request.GET)
        jobs_data = json.loads(all_jobs.text)
        return jobs_data
    except Exception as e:
        raise APIException("There was a problem!")

def get_relevant_jobs(jobs_data, job_type):
    """
    Filter Jobs based on the job_type
    """
    result = []
    for data in jobs_data:
        if data['type'] == job_type:
            result.append(data)
    return result    

def fetch_user_jobs(request, user_id):
    jobs_data = fetch_jobs_data(request)
    job_type = fetch_job_type(request, user_id)
    result = get_relevant_jobs(jobs_data, job_type)
    return result
    
