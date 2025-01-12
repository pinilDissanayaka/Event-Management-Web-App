from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")



    class Meta:
        model=User
        fields=["username", "password", "confirm_password"]