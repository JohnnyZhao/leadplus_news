# Generated by Django 4.1.7 on 2023-03-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newsitem_md5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='content',
            field=models.TextField(),
        ),
    ]
