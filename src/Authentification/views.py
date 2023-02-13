from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from Authentification.models import Note, User

from . import forms

@login_required
def logout_user(request):
    """Déconnexion de l'utilisateur"""
    logout(request)
    return redirect('login')

def login_page(request):
    """Page de connexion"""
    if request.user.is_authenticated:
        """Si l'utilisateur est déjà connecté, on le redirige vers l'accueil"""
        return redirect('accueil')
    form = forms.LoginForm()
    """Si l'utilisateur n'est pas connecté, on affiche le formulaire de connexion"""
    message = ''
    """Message d'erreur"""
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            """On vérifie que l'utilisateur existe bien"""
            if user is not None:
                """Si l'utilisateur existe, on le connecte"""
                login(request, user)
                return redirect('accueil')
            else:
                """Sinon, on affiche un message d'erreur"""
                message = "Vos identifiants sont incorrects"
    return render(request, 'Authentification/login.html', context={'form': form, 'message': message})

def create_user(request):
    """Création d'un utilisateur"""
    if request.user.is_authenticated:
        return redirect('accueil')
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            role = form.cleaned_data['role']
            born = form.cleaned_data['born']
            nom = form.cleaned_data['nom']
            user = User.objects.create_user(username = username , email=email, password=password)
            """On crée l'utilisateur"""
            user.role = role
            user.born = born
            user.nom = nom
            user.save()
            return redirect('login')
    return render(request, 'Authentification/create_user.html', context={'form': form})

@login_required
def liste_utilisateurs(request):
    """Liste des utilisateurs"""
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.user.role != 'CREATOR':
        return redirect('accueil')
    query = request.GET.get('q')
    if query:
        """Recherche d'un utilisateur"""
        users = User.objects.filter(username__contains=query)
    else:
        users = User.objects.all()
    return render(request, 'Authentification/liste_utilisateurs.html', context={'users': users})


@login_required
def delete_user(request, user_id):
    """Suppression d'un utilisateur"""
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.user.role != 'CREATOR':
        return redirect('accueil')
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('liste_utilisateurs')

@login_required
def details_utilisateur(request, user_id):
    """Détails d'un utilisateur"""
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.user.role != 'CREATOR':
        return redirect('accueil')
    user = User.objects.get(id=user_id)
    form = forms.NoteForm()
    if request.method == 'POST':
        """Ajout d'une note"""
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            """On vérifie que le formulaire est valide"""
            note = Note(user=user, text=form.cleaned_data['text'])
            note.save()
    notes = Note.objects.filter(user=user)
    return render(request, 'Authentification/details_utilisateur.html', context={'user': user, 'form': form, 'notes': notes})

 
@login_required   
def update_profile(request):
    """Modification d'un utilisateur"""
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.method == 'POST':
        form = forms.UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            """On vérifie que le formulaire est valide"""
            form.save()
        return redirect('accueil')
    else:
        form = forms.UpdateForm(instance=request.user)
    return render(request, 'Authentification/modification_utilisateur.html', {'form': form})



