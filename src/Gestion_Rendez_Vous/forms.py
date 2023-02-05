from django import forms
from .models import Appointment
import datetime

class AppointmentForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())
    time = forms.TimeField(widget=forms.Select(choices=[(f'{x}:00', f'{x}:00') for x in range(9, 17)]))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        if date and time:
            datetime_str = f"{date.strftime('%Y-%m-%d')} {time.strftime('%H:%M:%S')}"
            datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            if Appointment.objects.filter(date=datetime_obj).exists():
                raise forms.ValidationError("Un rendez-vous est déjà pris pour cette heure et ce jour.")
            cleaned_data['datetime'] = datetime_obj
        return cleaned_data




