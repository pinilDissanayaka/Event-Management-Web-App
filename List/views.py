from django.shortcuts import render
from django.http import HttpResponse 
from .forms import ListCreationForm
from .models import List
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def items(request):
    list_items = List.objects.all()
    return render(request, 'List/list.html', {"list_items": list_items})

def item(request, id):
    if request.method == "GET":
        list_item = List.objects.filter(id=id)
        return HttpResponse(list_item)
    elif request.method == "DELETE":
        list_item = List.objects.filter(id=id)
        list_item.delete()
        return HttpResponse("Deleted")
    elif request.method == "PUT":
        list_item = List.objects.filter(id=id)
        list_item.update(status=True)
        return HttpResponse("Updated")


@login_required
def create_list(request):
    if request.method == "POST":
        form = ListCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tist")
    else:
        form = ListCreationForm
        return render(request, 'List/createList.html', {"form": form})
