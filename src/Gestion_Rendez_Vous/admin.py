from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Administration pour les rendez-vous"""
    list_display = ('client', 'coach', 'formatted_date', 'description')