from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jobs/(?P<pk>\d+)$', views.JobRetrieveUpdate.as_view(), name="jobs-detail"),
    url(r'^jobs$', views.JobListCreate.as_view(), name="jobs-list"),
    url(r'^jobmatchs/(?P<pk>\d+)$', views.JobMatchRetrieveUpdate.as_view(), name="job-matchs-detail"),
    url(r'^jobmatchs$', views.JobMatchListCreate.as_view(), name="job-matchs-list"),
]