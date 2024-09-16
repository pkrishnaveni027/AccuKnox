from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction
import threading
from myapp.models import MyModel


@receiver(post_save, sender=MyModel)
def sync_signal_handler(sender, instance, **kwargs):
    print("Signal received")


@receiver(post_save, sender=MyModel)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")


@receiver(post_save, sender=MyModel)
def transaction_signal_handler(sender, instance, **kwargs):
    print(f"In transaction: {transaction.get_connection().in_atomic_block}")
