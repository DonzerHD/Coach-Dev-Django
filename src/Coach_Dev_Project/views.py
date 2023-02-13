from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def accueil(request):
    """Page d'accueil du site"""
    return render(request, 'accueil.html')
