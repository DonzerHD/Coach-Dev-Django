# Generated by Django 4.1 on 2023-02-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0011_user_born'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, verbose_name='Prenom'),
        ),
    ]