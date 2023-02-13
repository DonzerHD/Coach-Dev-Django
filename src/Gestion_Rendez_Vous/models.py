from django.db import models
from babel.dates import format_datetime

from Authentification.models import User

class Appointment(models.Model):
    """Modèle d'un rendez-vous"""
    date = models.DateTimeField(verbose_name="Date et heure du rendez-vous")
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Patient")
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Docteur', default=31)
    """On met le coach par défaut à 31, qui est le coach de test"""
    description = models.TextField(verbose_name="Description", blank=True)

    class Meta:
        """Meta"""
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"
    
    def formatted_date(self):
        """Retourne la date au format français"""
        return format_datetime(self.date, locale='fr_FR', format='dd MMMM YYYY à HH\'h\'mm')