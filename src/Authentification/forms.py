from django import forms
from Authentification.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField(label="Prenom")
    nom = forms.CharField(label="Nom")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    role = forms.CharField(widget=forms.HiddenInput, initial='Utilisateur')
    born = forms.DateField(label="Date de naissance", widget=forms.DateInput(attrs={'type': 'date'}))
    
class NoteForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email' , "nom", "born" ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['born'].widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})