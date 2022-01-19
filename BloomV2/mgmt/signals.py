# code
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from accounts.models import CustomUser

from mgmt.middleware import RequestMiddleware
from mgmt.models import Amenity, AmenityProfileRelationship


@receiver(post_save, sender=Amenity)
def create_amenity(sender, instance, created, **kwargs):
    request = RequestMiddleware(get_response=None)
    request = request.thread_local.current_request
    user = request.user
    if user:
        if created:
            AmenityProfileRelationship.objects.create(
                amenity=instance, profile=user.profile, profile_type='0')

            print("\n\n\nYEOOO Relationship created\n\n\n")
