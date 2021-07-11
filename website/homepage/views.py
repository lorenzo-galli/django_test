from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage/homepage.html')

def albums(request):
    return render(request, 'homepage/albums.html')