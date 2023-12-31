from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):

    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        related_name='profile'
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
        user_profile.follows.set([instance.profile.id])
        user_profile.save()



class Dweet(models.Model):
    user = models.ForeignKey(
        User, related_name="dweets", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:10]}..."
        )

post_save.connect(create_profile, sender=User)