from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import CustomUser
from cart.models import UserCart


@receiver(post_save, sender=CustomUser)
def create_user_cart(sender, instance: CustomUser, created, **kwargs):
    if created:
        user_cart = UserCart(user=instance)
        user_cart.save()
