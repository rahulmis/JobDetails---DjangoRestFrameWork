from django.urls import path
from findjob import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('jobs/', views.all_jobs),
    path('jobs/<int:id>', views.relevant_jobs)
]