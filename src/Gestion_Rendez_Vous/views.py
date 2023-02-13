import time
from django.http import JsonResponse
from django.shortcuts import render, redirect

from Authentification.models import User
from Gestion_Rendez_Vous.models import Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

@login_required
def create_appointment(request):
    """Création d'un rendez-vous"""
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

@login_required
def liste_appointment(request):
    """Liste des rendez-vous"""
    appointments = Appointment.objects.all()
    return render(request, 'Gestion_Rendez_Vous/listRdv.html', {'appointments': appointments})

@login_required
def delete_appointment(request, appointment_id):
    """Suppression d'un rendez-vous"""
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    if request.user.role != 'CREATOR':
        return redirect('appointments_view')
    return redirect('appointment_list')

@login_required
def appointments_view(request):
    """Liste des rendez-vous d'un utilisateur"""
    appointments = Appointment.objects.filter(client=request.user)
    context = {
        'appointments': appointments
    }
    return render(request, 'Gestion_Rendez_Vous/rdv_utilisateur.html', context)