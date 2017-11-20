from rest_framework import serializers

from artdb.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'bod',
                  'description',)
