from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('jobs.urls')),
    url(r'^v1/', include('users.urls')),
    url(r'^v1/', include('companies.urls')),
    url(r'^v1/', include('volunteers.urls')),
    url(r'^v1/user-auth/', include('rest_framework.urls')),
    url(r'^favicon\.ico$', favicon_view),
    #url(r'^v1/rest-auth/', include('rest_auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)