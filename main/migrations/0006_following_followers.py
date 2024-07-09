# Generated by Django 4.2.13 on 2024-06-26 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_comments_reply_reply_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_name', models.CharField(max_length=50)),
                ('following_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_id', to='main.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_name', models.CharField(max_length=50)),
                ('follower_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_id', to='main.userprofile')),
            ],
        ),
    ]
