from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home2(request):
    return HttpResponse("This is home 3")
