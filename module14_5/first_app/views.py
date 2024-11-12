from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def django_form(request):
    if request.method == 'POST': 
        form = forms.ExampleForm(request.POST) 
        if form.is_valid(): 
            return redirect('add_post') 
    
    else: 
        form = forms.ExampleForm()
    return render(request,'django_form.html', {'form':form})