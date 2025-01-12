from django.shortcuts import render
from django.http import HttpResponse 
from .forms import ListCreationForm

# Create your views here.


def create_list(request):
    if request.method == "POST":
        form = ListCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tist")
    else:
        form = ListCreationForm
        return render(request, 'List/createList.html', {"form": form})
