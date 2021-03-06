from django.db.models.signals import post_save      # signal
from django.contrib.auth.models import User     # sender of the signal
from django.dispatch import receiver        # receiver of the signal
from .models import Profile     # model to save

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()