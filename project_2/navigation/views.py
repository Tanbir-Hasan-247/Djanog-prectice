from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'navigation/about.html')

def pages(request):
    return render(request,'navigation/pages.html')

def bloge(request):
    return render(request,'navigation/bloge.html')