from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jobs/(?P<pk>\d+)$', views.JobRetrieveUpdate.as_view(), name="jobs-detail"),
    url(r'^jobs$', views.JobListCreate.as_view(), name="jobs-list"),
]