from django.shortcuts import render, redirect
from .models import Memory
from django.contrib.auth.decorators import login_required

@login_required
def memory_list(request):
    memories = Memory.objects.filter(user=request.user)
    return render(request, './memories/memory_list.html', {'memories': memories})

@login_required
def add_memory(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        Memory.objects.create(user=request.user, title=title, description=description, image=image)
        return redirect('memory_list')
    return render(request, './memories/add_memory.html')
