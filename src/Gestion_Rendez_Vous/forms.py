from django import forms
from .models import Appointment
import datetime

class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(label="Date et heure du rendez-vous", widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment
        fields = ['date','description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})



