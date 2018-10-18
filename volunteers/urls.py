from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^volunteers/(?P<pk>\d+)$', views.VolunteerRetrieveUpdate.as_view(), name="volunteer-detail"),
    url(r'^volunteers$', views.VolunteerListCreate.as_view(), name="volunteer-list"),
]