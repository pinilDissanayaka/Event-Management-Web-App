from django.db import models

# Create your models here.

class EventUser(models.Model):
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    email = models.EmailField("Email Address")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=50)
    address=models.CharField("Venue Address", max_length=50)
    zip_code = models.IntegerField("Zip Code")
    phone = models.IntegerField("Phone Number") 
    web = models.URLField("Website", blank=True)
    email = models.EmailField("Email Address", blank=True)
    capacity = models.IntegerField("Capacity")

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    name = models.CharField("Event Name", max_length=50)
    event_date = models.DateField("Event Date")
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, blank=True, null=True)
    manager = models.CharField("Event Manager", max_length=50)
    description = models.TextField("Event Description")
    attendees = models.ManyToManyField(EventUser, blank=True)


    def __str__(self):
        return f"{self.name}"