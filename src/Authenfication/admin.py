from django.contrib import admin
from .models import Utilisateur

# Register your models here.

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom','date_naissance')
    
admin.site.register(Utilisateur, UtilisateurAdmin)