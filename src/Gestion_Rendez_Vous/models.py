from django.db import models

from Authentification.models import User

class Appointment(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments', default=8)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_appointments')
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=500, blank=True)