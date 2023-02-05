from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from Authentification.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    role = forms.CharField(widget=forms.HiddenInput, initial='Utilisateur')
    
class NoteForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    
class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']
