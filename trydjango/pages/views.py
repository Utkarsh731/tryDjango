from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(*args,**kwargs):
    return HttpResponse("<h1>He</h1>")
