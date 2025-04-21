from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, CustomerProfile, SupplierProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'customer':
            CustomerProfile.objects.create(user=instance)
        elif instance.user_type == 'supplier':
            SupplierProfile.objects.create(user=instance)
