from django.db import models


# Backup tape management
class MediaType(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.name}"

class StorageLocation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Tape(models.Model):
    label = models.CharField(max_length=30)
    media_type = models.ForeignKey(MediaType, on_delete=models.RESTRICT)
    location = models.ForeignKey(StorageLocation, on_delete=models.RESTRICT, default=-1)

    def __str__(self):
        return f"{self.label} ({self.media_type})"

class Movement(models.Model):
    movement_date = models.DateField()
    tapes = models.ManyToManyField(Tape)
    location = models.ForeignKey(StorageLocation, on_delete=models.RESTRICT)


# Backup restore log
class FileRestoration(models.Model):
    headline = models.CharField(max_length=100)
    requested = models.DateField()
    notes = models.TextField()
    completed = models.DateField()
    ticket = models.URLField()

    def __str__(self):
        return f"{self.headline}"


# IP address management
class IPAddress(models.Model):
    address = models.GenericIPAddressField(protocol='IPv4')
    server_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address}"



  