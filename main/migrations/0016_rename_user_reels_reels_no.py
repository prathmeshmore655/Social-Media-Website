# Generated by Django 4.2.13 on 2024-07-08 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_reels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reels',
            old_name='user',
            new_name='reels_no',
        ),
    ]