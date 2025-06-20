# code
import itertools
import sys

from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import Tape, Movement

# Is this really how you do static variables in Python?
this = sys.modules[__name__]
this.movement_date = None
this.location = None

@receiver(post_save, sender=Movement) 
def tape_movement_saved(sender, instance, created, **kwargs):
    if created:
        # Save when and where so it can be used by the m2m_changed 
        # signal handler
        this.location = instance.location
        this.movement_date = instance.movement_date

@receiver(m2m_changed)
def movement_m2m_changed(sender, instance, action, model, pk_set, **kwargs):
    instance_name = instance.__class__.__name__

    if action == 'post_add' and instance_name == 'Movement':
        for tape_id in pk_set:
            tape = Tape.objects.get(id=tape_id)
            tape.date_moved = this.movement_date
            tape.location = this.location
            tape.save()
             