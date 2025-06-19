# code
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tape, Movement

@receiver(post_save, sender=Movement) 
def update_related_tapes(sender, instance, created, **kwargs):
    print("ZARG!")
    if created:
        print("BLARG")
        movement = Movement.objects.get(id=instance.id)
        for tape in movement.tapes.all():
            print("TAPE")

 