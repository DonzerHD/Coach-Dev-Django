# Generated by Django 4.1 on 2023-02-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0010_remove_user_profile_photo_user_nom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='born',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date de naissance'),
        ),
    ]
