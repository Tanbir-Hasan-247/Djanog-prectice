from django.shortcuts import render
from . forms import contactForm
# Create your views here.
def home(request):
    return render(request, './html/home.html')

def about(request):
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('email')
        return render(request,'./html/about.html',{'name':name,'email':email})
    else:
        return render(request,'./html/about.html')


def form(request):
    return render(request, './html/form.html')

def djangoforms(request):
    if request.method=='POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/'+file.name,'wb+') as ddestination:
                for chunk in file.chunks():
                    ddestination.write(chunk)
            print(form.cleaned_data)
        return render(request,'./html/django_form.html', {'form':form})
    else:
        form = contactForm()
        return render(request,'./html/django_form.html', {'form':form})
    