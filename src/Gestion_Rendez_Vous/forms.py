from django import forms
from .models import Appointment

from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

class AppointmentForm(forms.ModelForm):
    date = forms.ChoiceField(label="Date et heure du rendez-vous (Comptez environ 1 heure pour le rendez-vous)")

    class Meta:
        model = Appointment
        fields = ['date','description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

        # Generate list of available appointment times
        available_times = []
        for i in range(70):
            start = timezone.now() + datetime.timedelta(days=i + 2)
            if start.weekday() in [5, 6]:
                continue
            for i in range(24):
                current_hour = 9 + i
                if current_hour > 16:
                    continue
                current_time = datetime.datetime.combine(start, datetime.time(current_hour))
                if current_time.hour < 12 or current_time.hour >= 13:
                    if not Appointment.objects.filter(date=current_time).exists():
                        available_times.append((current_time.strftime("%Y-%m-%dT%H:%M"), current_time.strftime("%d/%m/%Y %H:%M")))

        # Set choices for date field
        self.fields['date'].choices = available_times

    def clean(self):
        cleaned_data = super().clean()
        date_str = cleaned_data.get('date')
        if date_str:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
            cleaned_data['date'] = date

            # Check if coach is not in another appointment at the same time
            start = date
            end = start + datetime.timedelta(minutes=10)
            conflicting_appointments = Appointment.objects.filter(date__range=(start, end))
            if conflicting_appointments.exists():
                self.add_error('date', "Le coach ne peut être dans deux rendez-vous en même temps.")

    



