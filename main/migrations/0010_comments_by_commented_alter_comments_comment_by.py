# Generated by Django 4.2.13 on 2024-07-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_commment_by_comments_comment_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='by_commented',
            field=models.CharField(default='NUll', max_length=50),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_By',
            field=models.CharField(default='Null', max_length=10),
        ),
    ]
