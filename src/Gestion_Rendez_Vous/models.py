from django.db import models
from django.utils.dateformat import format
from babel.dates import format_date

from Authentification.models import User

class Appointment(models.Model):
    date = models.DateTimeField(verbose_name="Date et heure du rendez-vous")
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Patient")
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Docteur', default=31)
    description = models.TextField(verbose_name="Description", blank=True)

    class Meta:
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"
        
    def formatted_date(self):
        return format_date(self.date, locale='fr_FR')