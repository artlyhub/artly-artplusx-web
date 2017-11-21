from django.db.models import Q
from django.views import View
from django.views.generic import ListView
from django.shortcuts import redirect, render

from artdb.models import Artist


class ArtistListView(ListView):
    template_name = 'home.html'
    queryset = Artist.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super(ArtistListView, self).get_queryset()

        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
            )
            if qs.exists():
                return qs

def temp_page():
    pass
