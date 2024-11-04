# Generated by Django 5.1.2 on 2024-11-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Travel', 'Travel'), ('Sport', 'Sport'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology'), ('Business', 'Business'), ('Culture', 'Culture')], max_length=256),
        ),
    ]