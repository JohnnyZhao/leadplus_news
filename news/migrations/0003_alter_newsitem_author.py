# Generated by Django 4.1.7 on 2023-03-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsitem_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
