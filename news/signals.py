import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import NewsItem

@receiver(pre_save, sender=NewsItem)
def calculate_md5(sender, instance, **kwargs):
    md5_hash = hashlib.md5(instance.url.encode('utf-8')).hexdigest()
    instance.md5 = md5_hash