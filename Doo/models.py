import sys, traceback
from django import forms
from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog

from .modelzz.backups.restore import FileRestoration
from .modelzz.backups.tape import Tape, MediaType, StorageLocation
from .modelzz.backups.movement import Movement

class IPAddress(models.Model):
    address = models.GenericIPAddressField(protocol='IPv4')
    server_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address}"


  auditlog.register(IPAddress)