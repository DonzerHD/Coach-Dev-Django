from django.shortcuts import render, redirect

from Authentification.models import User
from Gestion_Rendez_Vous.models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            appointment = Appointment(
                coach_id=31,
                client=request.user,
                date=cleaned_data['date'],
                description=cleaned_data['description']
            )
            appointment.save()
            return redirect('accueil')
    else:
        form = AppointmentForm()
    return render(request, 'Gestion_Rendez_Vous/rdv.html', {'form': form})