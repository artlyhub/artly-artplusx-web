from django.conf.urls import include, url
from django.contrib import admin

from artdb.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('artdb.api.urls', namespace='api')),
    url(r'^$', home, name='home'),
]
