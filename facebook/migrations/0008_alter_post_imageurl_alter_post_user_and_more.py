# Generated by Django 4.0.3 on 2022-05-25 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facebook', '0007_remove_post_group_delete_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageUrl',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(),
        ),
    ]
