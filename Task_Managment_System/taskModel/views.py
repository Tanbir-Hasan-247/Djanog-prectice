from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def add_Task(request):
    if request.method == 'POST': 
        post_form = forms.ModelsForm(request.POST) 
        if post_form.is_valid():
            post_form.save() 
            return redirect('homepage')  # Redirect to 'homepage' after saving
    else: 
        post_form = forms.ModelsForm()
    return render(request, 'task_model.html', {'form': post_form})

def editTask(request, id):
    task = models.Model.objects.get(pk=id)
    if request.method == 'POST': 
        post_form = forms.ModelsForm(request.POST, instance=task)  # Pass instance here
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage') 
    else: 
        post_form = forms.ModelsForm(instance=task)  # Pass instance here
    return render(request, 'task_model.html', {'form': post_form})

def deleteTask(request, id):
    task = models.Model.objects.get(pk=id)
    task.delete()
    return redirect('homepage')
