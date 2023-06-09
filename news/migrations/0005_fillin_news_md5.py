# Generated by Django 4.1.7 on 2023-03-21 03:13

import hashlib
from django.db import migrations


def set_md5(apps, schema_editor):
    """calculate md5 value for existing NewsItem records"""
    NewsItem = apps.get_model('news', 'NewsItem')
    for record in NewsItem.objects.all():
        record.md5 = hashlib.md5(record.url.encode('utf-8'))
        record.save()


class Migration(migrations.Migration):
    """set md5 value for existing NewsItem records"""

    dependencies = [
        ('news', '0004_newsitem_md5'),
    ]

    operations = [
        migrations.RunPython(set_md5),
    ]
