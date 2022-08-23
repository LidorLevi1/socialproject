# Generated by Django 4.0.3 on 2022-05-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ManyToManyField(blank=True, to='facebook.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imageUrl',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, to='facebook.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship',
            field=models.BooleanField(),
        ),
    ]