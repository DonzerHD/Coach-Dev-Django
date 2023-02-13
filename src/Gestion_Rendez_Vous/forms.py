from django import forms
from .models import Appointment

from django.utils import timezone
import datetime

class AppointmentForm(forms.ModelForm):
    """Formulaire de rendez-vous"""
    date = forms.ChoiceField(label="Date et heure du rendez-vous (Comptez environ 1 heure pour le rendez-vous)")

    class Meta:
        """Meta"""
        model = Appointment
        fields = ['date','description']

    def __init__(self, *args, **kwargs):
        """Initialisation du formulaire"""
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

        # Generate list of available appointment times
        available_times = []
        for i in range(70):
            """70 jours de disponibilité"""
            start = timezone.now() + datetime.timedelta(days=i + 2)
            if start.weekday() in [5, 6]:
                continue
            for i in range(24):
                """24 heures par jour"""
                current_hour = 9 + i
                if current_hour > 16:
                    """On ne prend pas en compte les heures après 16h"""
                    continue
                current_time = datetime.datetime.combine(start, datetime.time(current_hour))
                if current_time.hour < 12 or current_time.hour >= 13:
                    """On ne prend pas en compte les heures de midi"""
                    if not Appointment.objects.filter(date=current_time).exists():
                        """On ne prend pas en compte les heures déjà prises"""
                        available_times.append((current_time.strftime("%Y-%m-%dT%H:%M"), current_time.strftime("%d/%m/%Y %H:%M")))


        """On met à jour les choix de date"""
        self.fields['date'].choices = available_times

    def clean(self):
        """Validation du formulaire"""
        cleaned_data = super().clean()
        date_str = cleaned_data.get('date')
        if date_str:
            """On convertit la date en datetime"""
            date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
            cleaned_data['date'] = date

            """On vérifie que la date est dans le futur"""
            start = date
            end = start + datetime.timedelta(minutes=10)
            conflicting_appointments = Appointment.objects.filter(date__range=(start, end))
            if conflicting_appointments.exists():
                """On vérifie qu'il n'y a pas de conflit de date"""
                self.add_error('date', "Le coach ne peut être dans deux rendez-vous en même temps.")

    



