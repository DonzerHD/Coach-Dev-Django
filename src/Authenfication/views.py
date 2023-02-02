from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from Authenfication.forms import ConnexionForm
from Authenfication.models import Utilisateur


def connexion(request):
    if request.method == "POST":
            form = ConnexionForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                utilisateur = Utilisateur.objects.filter(email=email)
                if utilisateur:
                    utilisateur = utilisateur[0]
                    if utilisateur.password == password:
                        request.session['utilisateur_id'] = utilisateur.id
                        return redirect('accueil')
                    else:
                        form.add_error(None, "Email ou mot de passe incorrect")
                else:
                    form.add_error(None, "Email ou mot de passe incorrect")
    else:
            form = ConnexionForm()
    return render(request, 'Authenfication/login.html', locals())