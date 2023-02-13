from django import forms
from Authentification.models import User

class LoginForm(forms.Form):
    """Formulaire de connexion"""
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    """Formulaire d'inscription"""
    username = forms.CharField(label="Prenom")
    nom = forms.CharField(label="Nom")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    role = forms.CharField(widget=forms.HiddenInput, initial='Utilisateur')
    """On met le rôle par défaut à "Utilisateur"""
    born = forms.DateField(label="Date de naissance", widget=forms.DateInput(attrs={'type': 'date'}))
    
class NoteForm(forms.Form):
    """Formulaire de note """
    text = forms.CharField(widget=forms.Textarea)
    
class UpdateForm(forms.ModelForm):
    """Formulaire de mise à jour"""
    class Meta:
        """Meta"""
        model = User
        """On utilise le modèle User"""
        fields = ['username', 'email' , "nom", "born" ]
        """On utilise les champs username, email, nom et born"""
        
    def __init__(self, *args, **kwargs):
        """Initialisation du formulaire"""
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['born'].widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})