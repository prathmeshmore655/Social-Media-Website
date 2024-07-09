from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, UserProfile

@receiver(post_save, sender=User)
def create_profile_and_post(sender, instance, created, **kwargs):
    if created:
        # Create a UserProfile
        UserProfile.objects.create(user=instance)
        # Create a default post for the new user
        Post.objects.create(post_no=instance, caption='Welcome post', post_file='posts/no_post.jpeg')
