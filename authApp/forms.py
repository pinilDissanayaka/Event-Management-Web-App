from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model=User
        fields=["username", "password", "confirm_password"]


    def clean(self):
        cleaned_data= super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")

        return cleaned_data
