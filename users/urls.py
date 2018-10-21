from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user-auth/confirmation/', views.UserLoginConfirmation.as_view(), name="login-confirmation"),
]