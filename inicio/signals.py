
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(user_logged_in)
def incrementar_contador_login(sender, request, user, **kwargs):
    profile, created = Profile.objects.get_or_create(user=user)
    profile.login_count += 1
    profile.save()


