# Generated by Django 5.1.4 on 2024-12-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
