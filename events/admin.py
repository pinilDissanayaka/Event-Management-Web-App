from django.contrib import admin
from .models import EventUser, Venue, Event

# Register your models here.

admin.site.register(EventUser)
admin.site.register(Venue)  
admin.site.register(Event)