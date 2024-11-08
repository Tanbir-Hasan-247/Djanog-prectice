from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    d={"name":"tanbir","age":21,'lst' : ['python','is','best']}
    return render(request,"index.html",d)