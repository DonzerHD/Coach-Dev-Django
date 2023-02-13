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
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput)
    role = forms.CharField(widget=forms.HiddenInput, initial='Utilisateur')
    """On met le rôle par défaut à "Utilisateur"""
    born = forms.DateField(label="Date de naissance", widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean_email(self):
        """Vérification de l'email"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("L'email est déjà utilisé.")
        return email
    
    def clean(self):
        """Vérification des mots de passe"""
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2 or password2 != password1:
            self.add_error("password2", "Les mots de passe ne correspondent pas.")
    
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