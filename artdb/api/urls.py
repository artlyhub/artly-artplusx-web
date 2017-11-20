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
    url(r'^artist/(?P<pk>[\w.@+-]+)/$', ArtistDetailAPIView.as_view(), name="artist-detail"),

    url(r'^artwork/$', ArtworkAPIView.as_view(), name="artwork"),
    url(r'^artwork/(?P<pk>[\w.@+-]+)/$', ArtworkDetailAPIView.as_view(), name="artwork-detail"),

    url(r'^price/$', PriceHistoryAPIView.as_view(), name="price"),
    url(r'^price/(?P<pk>[\w.@+-]+)/$', PriceHistoryDetailAPIView.as_view(), name="price-detail"),
]
