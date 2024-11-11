from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def addAlbum(request):
    if request.method == 'POST': 
        post_form = forms.AlbumForm(request.POST) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('add_album') 
    else: 
        post_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form' : post_form})

def editAlbum(request, id):
    album = models.Album.objects.get(pk=id)
    post_form = forms.AlbumForm(instance=album)
    if request.method == 'POST': 
        post_form = forms.AlbumForm(request.POST) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('add_album') 
    return render(request, 'add_album.html', {'form' : post_form})