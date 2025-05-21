from django.contrib import admin

from .models import MediaType, Tape, IPAddress, StorageLocation, Movement, FileRestoration

admin.site.register(MediaType)
admin.site.register(Movement)
admin.site.register(Tape)
admin.site.register(StorageLocation)
admin.site.register(FileRestoration)
admin.site.register(IPAddress)
