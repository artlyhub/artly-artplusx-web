from django.db.models import Q
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


class SearchArtistAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_serializer_context(self, *args, **kwargs):
        context = super(SearchArtistAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        qs = self.queryset
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(Q(name__icontains=query))
        return qs
