from django.shortcuts import render
from .forms import UserCreationForm
# Create your views here.


def register_view(request):
    form = UserCreationForm

    return render(request, 
                  "authApp/register.html",
                  {"form": form})
