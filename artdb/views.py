from django.db.models import Q
from django.views import View
# from django.views.generic import ListView
from django.shortcuts import redirect, render

from artdb.models import Artist, Artwork


class ArtistListView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        artists = None
        context = dict()
        if query:
            artists = Artist.objects.filter(
                Q(name__icontains=query)
            )
            if len(artists) > 1:
                context['artists'] = artists
            else:
                artworks = Artwork.objects.filter(artist__name__icontains=query)
                context['artist'] = artists
                context['artworks'] = artworks
        return render(request, 'home.html', context)


def artist_detail_view(request, pk=None):
    artist = Artist.objects.filter(pk=pk)
    artworks = Artwork.objects.filter(artist=pk)
    context = {
        'artist': artist,
        'artworks': artworks
    }
    return render(request, 'home.html', context)
