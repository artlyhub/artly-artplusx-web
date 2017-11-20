from django.conf.urls import url

from artdb.api.views import (
    ArtistAPIView,
    ArtistDetailAPIView,
)

urlpatterns = [
    url(r'^artist/$', ArtistAPIView.as_view(), name="artist"),
    url(r'^artist/(?P<pk>[\w.@+-]+)/$', ArtistDetailAPIView.as_view(), name="artist-detail"),
]
