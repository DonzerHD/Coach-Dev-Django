from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import date as date_filter
from django.db import models

class User(AbstractUser):
    
    username = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30 , verbose_name='Rôle')
    
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def formatted_date(self):
        return date_filter(self.date, "d F Y, H:i")