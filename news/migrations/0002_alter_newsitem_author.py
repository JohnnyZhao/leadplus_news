# Generated by Django 4.1.7 on 2023-03-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]
