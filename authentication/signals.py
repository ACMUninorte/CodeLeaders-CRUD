from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication.models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # for superusers
    if created and not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
