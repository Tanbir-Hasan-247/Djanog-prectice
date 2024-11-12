from django.shortcuts import render,redirect
from . import models, forms
# Create your views here.
def add_category(request):
    if request.method == 'POST': 
        post_form = forms.CategoryForm(request.POST) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('add_category') 
    else: 
        post_form = forms.CategoryForm()
        return render(request, 'task_category.html', {'form':post_form})
    
