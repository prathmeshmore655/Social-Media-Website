# Generated by Django 4.2.13 on 2024-06-26 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_following_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followers',
            old_name='follower_no',
            new_name='follower_of',
        ),
    ]
