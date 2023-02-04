# Generated by Django 4.1 on 2023-02-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('coach', 'Coach'), ('utilisateur', 'Utilisateur')], max_length=30, verbose_name='Rôle'),
        ),
    ]
