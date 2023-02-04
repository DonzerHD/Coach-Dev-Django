from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render , redirect

from Authentification.models import Note, User

from . import forms

def logout_user(request):
    logout(request)
    return redirect('login')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
            else:
                message = "Vos identifiants sont incorrects"
    return render(request, 'Authentification/login.html', context={'form': form, 'message': message})

def create_user(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            user = User.objects.create_user(username = username , email=email, password=password)
            user.role = role
            user.save()
            return redirect('login')
    return render(request, 'Authentification/create_user.html', context={'form': form})

def liste_utilisateurs(request):
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.user.role != 'CREATOR':
        return redirect('accueil')
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__contains=query)
    else:
        users = User.objects.all()
    return render(request, 'Authentification/liste_utilisateurs.html', context={'users': users})


def delete_user(request, user_id):
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.user.role != 'CREATOR':
        return redirect('accueil')
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('liste_utilisateurs')

def details_utilisateur(request, user_id):
    if not request.user.is_authenticated:
        return redirect('accueil')
    if request.user.role != 'CREATOR':
        return redirect('accueil')
    user = User.objects.get(id=user_id)
    form = forms.NoteForm()
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            note = Note(user=user, text=form.cleaned_data['text'])
            note.save()
    notes = Note.objects.filter(user=user)
    return render(request, 'Authentification/details_utilisateur.html', context={'user': user, 'form': form, 'notes': notes})



