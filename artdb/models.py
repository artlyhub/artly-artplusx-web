import uuid

from django.db import models

def scramble_uploaded_image(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class Artist(models.Model):
    name = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to=scramble_uploaded_image,
                                    blank=True,
                                    null=True)
    bod = models.CharField(max_length=50,
                           blank=True,
                           null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE,
                               related_name='artworks')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=scramble_uploaded_image)
    size = models.CharField(max_length=100,
                            blank=True,
                            null=True)
    style = models.CharField(max_length=100,
                             blank=True,
                             null=True)
    created = models.CharField(max_length=50,
                               blank=True,
                               null=True)

    def __str__(self):
        return self.title


class PriceHistory(models.Model):
    artwork = models.ForeignKey(Artwork,
                                on_delete=models.CASCADE,
                                related_name='price_history')
    date = models.CharField(max_length=50,
                            blank=True,
                            null=True)
    begin = models.IntegerField(blank=True, null=True)
    estimate_low = models.IntegerField(blank=True, null=True)
    estimate_high = models.IntegerField(blank=True, null=True)
    hammer = models.IntegerField(blank=True, null=True)
    sold = models.BooleanField()

    def __str__(self):
        return self.artwork.title
