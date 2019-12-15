from django.shortcuts import render
from django.http import HttpResponse
from .forms import TopForm

def top(request):
    params = {
        "nameform": TopForm(),
    }
    return render(request, 'app/top.html', params)

def result(request):
    name = request.POST["name"]
    params = {
        "nameform": TopForm(),
        "name": name
    }
    return render(request, 'app/result.html', params)
# Create your views here.
