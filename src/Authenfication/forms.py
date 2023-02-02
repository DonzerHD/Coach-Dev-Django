from django import forms

from Authenfication.models import Utilisateur


class ConnexionForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'}))

    class Meta:
        model = Utilisateur
        fields = ('email', 'password')




    

    
    


