from django.shortcuts import render,Http404
from django.conf import settings

# Create your views here.

def home(request,exeption):
    return render(request,'404.html')