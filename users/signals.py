from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender = Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print("Profile Saved!")
    print("instance:", instance)
    print('CREATED:', created)
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('Deleting user ... ..', )

def createProfile(sender, instance, created, **kwargs):

    if created and not hasattr(instance, 'profile'):
        

        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name,
        )
        print("Profile signal triggered")


post_save.connect(createProfile, sender=User)


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



post_save.connect(updateUser, sender=Profile)