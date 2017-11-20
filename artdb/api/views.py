from rest_framework import generics

from artdb.models import (
    Artist,
    Artwork,
    PriceHistory,
)
from artdb.api.serializers import (
    ArtistSerializer,
    ArtworkSerializer,
    PriceHistorySerializer,
)


class ArtistAPIView(generics.ListCreateAPIView):
    queryset = Artist.objects.get_queryset()
    serializer_class = ArtistSerializer


class ArtistDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.get_queryset()
    serializer_class = ArtistSerializer


class ArtworkAPIView(generics.ListCreateAPIView):
    queryset = Artwork.objects.get_queryset()
    serializer_class = ArtworkSerializer


class ArtworkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.get_queryset()
    serializer_class = ArtworkSerializer


class PriceHistoryAPIView(generics.ListCreateAPIView):
    queryset = PriceHistory.objects.get_queryset()
    serializer_class = PriceHistorySerializer


class PriceHistoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceHistory.objects.get_queryset()
    serializer_class = PriceHistorySerializer
