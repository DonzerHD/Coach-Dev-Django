# Generated by Django 4.1 on 2023-02-02 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authenfication', '0002_rename_utilisateurs_utilisateur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='mot_de_passe',
            new_name='password',
        ),
    ]