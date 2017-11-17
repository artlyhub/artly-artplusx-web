from django.conf.urls import url

from artdb.api.views import ArtistAPIView

urlpatterns = [
    url(r'^artist/$', ArtistAPIView.as_view(), name="artist"),
]
