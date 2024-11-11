from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def django_form(request):
    if request.method == 'POST': # user post request koreche
        form = forms.ExampleForm(request.POST) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula amra valid kina check kortechi
            #post_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('add_post') # sob thik thakle take add author ei url e pathiye dibo
    
    else: # user normally website e gele blank form pabe
        form = forms.ExampleForm()
    return render(request,'django_form.html', {'form':form})