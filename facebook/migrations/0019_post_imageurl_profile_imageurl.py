# Generated by Django 4.0.3 on 2022-05-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0018_remove_post_imageurl_remove_profile_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageUrl',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='imageUrl',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
