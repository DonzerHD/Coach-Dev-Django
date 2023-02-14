from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import date as date_filter
from django.db import models

class User(AbstractUser):
    """Utilisateur personnalisé"""
    username = models.CharField(max_length=150, unique=False , verbose_name='Prenom')
    
    """Email est utilisé comme identifiant"""
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    """Role est utilisé pour la gestion des droits"""
    role = models.CharField(max_length=30 , verbose_name='Rôle')
    nom = models.CharField(max_length=150, unique=False, verbose_name='Nom' , default='Nom non donnée')
    born = models.DateField(verbose_name='Date de naissance' , default=None, null=True, blank=True)
    
class Note(models.Model):
    """Note d'un utilisateur écrit par le coach"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def formatted_date(self):
        return date_filter(self.date, "d F Y, H:i")