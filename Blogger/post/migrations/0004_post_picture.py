# Generated by Django 5.1.2 on 2024-11-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='images/defaul.jpg', upload_to='images/'),
        ),
    ]
