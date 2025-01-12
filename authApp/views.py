from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )

            login(request, user)
             
            return redirect("items")
        else:
            return render(request, "authApp/register.html", {"form": form, "errors": form.errors})
    else:
        form = UserCreationForm()
        return render(request, "authApp/register.html", {"form": form})
    

def login_view(request):
    if request.user.is_authenticated:
        return redirect("items")

    if request.method == "POST":
        user=authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("items")
        else:
            return render(request, "authApp/login.html", {"error": "Invalid username or password"})
    else:
        return render(request, "authApp/login.html")


def logout_view(request):

    logout(request)

    return redirect("login")
