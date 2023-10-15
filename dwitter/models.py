from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse


   

class Profile(models.Model):

    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )

    follows = models.ManyToManyField(
        'self', 
        related_name='followed_by',
        symmetrical=False,
        blank=True
    )

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return self.user.username
    
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.id])
        user_profile.save()


#post_save.connect(create_profile, sender=User)