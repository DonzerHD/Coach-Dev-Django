from django.contrib import admin
from .models import User, Note

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin for User model"""
    list_display = ['username', 'email', 'role', 'nom', 'born']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin for Note model"""
    list_display = ['user', 'text', 'formatted_date']
