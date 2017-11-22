from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from artdb.views import ArtistListView, artist_detail_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('artdb.api.urls', namespace='api')),
    url(r'^$', ArtistListView.as_view(), name='artist'),
    url(r'^(?P<pk>\d+)/$', artist_detail_view, name='artist-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
