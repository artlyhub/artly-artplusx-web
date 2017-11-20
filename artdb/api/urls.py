from django.conf.urls import url

from artdb.api.views import (
    ArtistAPIView,
    ArtistDetailAPIView,
    ArtworkAPIView,
    ArtworkDetailAPIView,
    PriceHistoryAPIView,
    PriceHistoryDetailAPIView,
)

urlpatterns = [
    url(r'^artist/$', ArtistAPIView.as_view(), name="artist"),
    url(r'^artist/(?P<pk>\d+)/$', ArtistDetailAPIView.as_view(), name="artist-detail"),

    url(r'^artwork/$', ArtworkAPIView.as_view(), name="artwork"),
    url(r'^artwork/(?P<pk>\d+)/$', ArtworkDetailAPIView.as_view(), name="artwork-detail"),

    url(r'^price/$', PriceHistoryAPIView.as_view(), name="price"),
    url(r'^price/(?P<pk>\d+)/$', PriceHistoryDetailAPIView.as_view(), name="price-detail"),
]
