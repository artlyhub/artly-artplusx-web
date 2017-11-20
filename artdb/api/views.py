from rest_framework import generics

from artdb.models import Artist
from artdb.api.serializers import ArtistSerializer


class ArtistAPIView(generics.ListCreateAPIView):
    queryset = Artist.objects.get_queryset()
    serializer_class = ArtistSerializer


class ArtistDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.get_queryset()
    serializer_class = ArtistSerializer
