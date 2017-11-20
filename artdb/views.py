from django.db.models import Q
from django.views import View
from django.shortcuts import render

from artdb.models import Artist


def home(request):
    return render(request, 'home.html', {})


class ArtistListView(ListView):
    template_name = 'artist_list.html'
    queryset = Artist.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Artist.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
            )
        return qs
