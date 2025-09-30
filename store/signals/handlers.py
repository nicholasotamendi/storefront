from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from store.models import Customer

#this signal creates a customer object whenever a new user is created
# this is a signal handler function that listens for the post_save signal from the User model

@receiver(signal = post_save, sender = settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user = kwargs['instance'])






