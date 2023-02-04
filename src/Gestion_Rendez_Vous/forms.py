from django import forms
import datetime

from Gestion_Rendez_Vous.models import Appointment

class AppointmentForm(forms.ModelForm):
    text = forms.CharField(label="formulaire l'objet de la séance", widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
    date = forms.ChoiceField(choices=[(date.strftime("%Y-%m-%d"), date.strftime("%Y-%m-%d")) for date in (datetime.date.today() + datetime.timedelta(n) for n in range(15))])
    time_debut = forms.ChoiceField(choices=[(datetime.datetime.combine(datetime.date.today(), datetime.time(hour=hour, minute=minute)).strftime("%H:%M"), datetime.datetime.combine(datetime.date.today(), datetime.time(hour=hour, minute=minute)).strftime("%H:%M")) for hour, minute in [(9, 0), (9, 50), (10, 40), (11, 30) , (13, 30), (14, 20), (15, 10), (16, 0)]])
    class Meta:
        model = Appointment
        fields = ['date', 'time_debut' , 'text']
        widgets = {
            'time_debut': forms.Select(attrs={'type': 'time'}),
        }