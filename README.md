# JobDetails---DjangoRestFrameWork

## Steps to Execute this Project ->

1 -> Install Python 3.9

2 -> Create a virtual Enviroment

> python3 -m venv venv

3 -> activate virtual env using the below command

> source venv/bin/activate

4 -> Open terminal and enter this command

> git clone https://github.com/rahulmis/JobDetails---DjangoRestFrameWork.git

5 -> go inside - JobDetails---DjangoRestFrameWork/JobsData

6 -> Install all required libraries using this command

> pip install -r requirements.txt

7 -> Execute migrate command

> python manage.py migrate

8 -> Execute our project

> python manage.py runserver

9 -> open brower and enter this url to get relevant jobs for a perticular user

> http://127.0.0.1:8080/jobs/1

Note :- exclude the user id from the url endpoint to get all the jobs

> http://127.0.0.1:8080/jobs/
