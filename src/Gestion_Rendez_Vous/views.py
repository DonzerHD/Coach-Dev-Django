from datetime import timedelta
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Authentification.models import User
from Gestion_Rendez_Vous.models import Appointment
from .forms import AppointmentForm

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            appointment.coach = User.objects.get(username='Admin')
            appointment_datetime = datetime.datetime.combine(appointment.date, appointment.time_debut)
            appointment.time_fin = appointment_datetime +  timedelta(minutes=40)
            appointment.save()
        return redirect('accueil')
    else:
        form = AppointmentForm()
    return render(request, 'Gestion_Rendez_Vous/rdv.html', {'form': form})

@login_required
def appointment_list(request):
    coach = request.user
    appointments = Appointment.objects.filter(coach=coach).order_by('date')
    return render(request, 'Gestion_Rendez_Vous/listRdv.html', {'appointments': appointments})