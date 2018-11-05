from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^volunteeringareas/(?P<pk>\d+)$', views.VolunteeringAreaRetrieve.as_view(), name="volunteeringarea-detail"),
    url(r'^volunteeringareas$', views.VolunteeringAreaList.as_view(), name="volunteeringarea-list"),
]