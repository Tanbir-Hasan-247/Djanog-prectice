from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def model_form(request):
    if request.method == 'POST': 
        form = forms.ModelForm(request.POST) 
        if form.is_valid():
            #form.save() 
            return redirect('model_form') 
    else: 
        form = forms.ModelForm()
    return render(request, 'model_form.html', {'form':form})