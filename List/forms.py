from django import forms
from .models import List

class ListCreationForm(forms.ModelForm):
    
    class Meta:
        model = List
        fields = ("item_name", "item_description", "status")