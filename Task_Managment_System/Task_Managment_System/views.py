from django.shortcuts import render
from taskModel.models import Model
def home(request):
    data = Model.objects.all()
    return render(request, 'home.html', {'data' : data})