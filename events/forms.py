from django import forms
from .models import Venue

class VenueCreationForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"