from django import forms
from django.db import models
from auditlog.registry import auditlog

from .tape import Tape, StorageLocation

class Movement(models.Model):
    movement_date = models.DateTimeField()
    tapes = models.ManyToManyField(Tape)
    location = models.ForeignKey(StorageLocation, on_delete=models.RESTRICT)
    comment = models.TextField(default='')

    def __str__(self):
        return f"{self.movement_date}"

    def get_absolute_url(self):
        return reverse('move-list')

auditlog.register(Movement)