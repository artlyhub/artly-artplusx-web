from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    bod = models.CharField(max_length=8,
                           blank=True,
                           null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
