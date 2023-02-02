from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.prenom