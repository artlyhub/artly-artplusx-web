from rest_framework import serializers

from artdb.models import (
    Artist,
    Artwork,
    PriceHistory,
)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'profile_img',
                  'bod',
                  'description',)


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('id',
                  'artist',
                  'title',
                  'image',
                  'size',
                  'style',
                  'created',)


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ('id',
                  'artwork',
                  'date',
                  'begin',
                  'estimate_low',
                  'estimate_high',
                  'hammer',
                  'sold',)
