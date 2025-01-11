from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import EventUser, Venue, Event
from .forms import VenueCreationForm

# Create your views here.

def createVenue(request):
    if request.method == 'POST':
        form = VenueCreationForm(request.POST)
        if form.is_valid():
            print(form)
            return HttpResponse("Form")
    else:
        form = VenueCreationForm
        return render(request, 'events/createVenue.html', {'form': form})
