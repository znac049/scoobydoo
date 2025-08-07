from django import forms
from django.db import models
from auditlog.registry import auditlog

class MediaType(models.Model):
    name = models.CharField(max_length=12)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class StorageLocation(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Tape(models.Model):
    label = models.CharField(max_length=30, unique=True, null=True, default=None)
    media_type = models.ForeignKey(MediaType, on_delete=models.RESTRICT)
    location = models.ForeignKey(StorageLocation, on_delete=models.RESTRICT, default=-1)
    date_moved = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.label} ({self.media_type})"

    def get_absolute_url(self):
        return reverse('tape-list')


auditlog.register(Tape)
auditlog.register(MediaType)
auditlog.register(StorageLocation)
