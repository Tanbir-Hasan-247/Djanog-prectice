from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def addMusician(request):
    if request.method == 'POST': 
        post_form = forms.MusicianForm(request.POST) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('add_album') 
    else: 
        post_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : post_form})

def editMusician(request, id):
    musician = models.Musician.objects.get(pk=id)
    post_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST': 
        post_form = forms.MusicianForm(request.POST) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('add_album') 
    return render(request, 'add_musician.html', {'form' : post_form})

def deleteMusician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('homepage')