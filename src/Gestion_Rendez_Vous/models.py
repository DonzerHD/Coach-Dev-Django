from django.db import models

from Authentification.models import User

class Appointment(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_appointments')
    date = models.DateField()
    time_debut = models.TimeField()
    time_fin = models.TimeField()
    text = models.CharField(max_length=200)
