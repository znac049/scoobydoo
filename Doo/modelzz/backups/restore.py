from django import forms
from django.db import models
from auditlog.registry import auditlog

# Backup restore log
class FileRestoration(models.Model):
    headline = models.CharField(max_length=100)
    requested = models.DateField()
    notes = models.TextField()
    completed = models.DateField()
    ticket = models.URLField()

    def __str__(self):
        return f"{self.headline}"


auditlog.register(FileRestoration)
