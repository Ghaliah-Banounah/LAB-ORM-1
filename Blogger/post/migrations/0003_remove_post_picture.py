# Generated by Django 5.1.2 on 2024-11-03 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
    ]
