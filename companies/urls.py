from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^companies$', views.CompanyListCreate.as_view(), name="company-list"),
    url(r'^companies/(?P<pk>\d+)$', views.CompanyRetrieveUpdate.as_view(), name="company-detail"),
    url(r'^companies$', views.CompanyListCreate.as_view(), name="company-list"),
]