from cgitb import text
from pickle import APPEND
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sp(request):
    return render(request,'sp.html')


def index(request):
    return render(request,'index.html',)
  

def counter(request):
        satya=request.POST['satya']
        words=len(satya.split())
        return render(request,'counter.html',{'amount':words},)

