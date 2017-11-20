from django.db.models import Q
from django.views import View
from django.views.generic import ListView
from django.shortcuts import redirect, render

from artdb.models import Artist


class ArtistListView(ListView):
    template_name = 'home.html'
    queryset = Artist.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Artist.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
            )
            return render(self.request,
                          'artist_list.html',
                          {'artist': qs})
        else:
            return render(self.request,
                          'home.html',
                          {})


def temp_page():
    pass
