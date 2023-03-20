# Generated by Django 4.1.7 on 2023-03-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('content', models.URLField()),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]
