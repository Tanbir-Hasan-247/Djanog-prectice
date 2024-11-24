from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Car
from orders.models import Order
from .forms import CommentForm

# class DetailsView(View):
#     def get(self, request, id):
#         car = Car.objects.get(pk=id)
#         return render(request, 'details.html', {'car': car})

@method_decorator(login_required, name='dispatch')
class BuyCarView(View):
    def post(self, request, id):
        car = Car.objects.get(pk=id)
        if car.quantity > 0:
            Order.objects.create(user=request.user, car=car)
            car.quantity -= 1
            car.save()
            return redirect('history')
        return render(request, 'details.html', {'error': 'Out of stock', 'car': car})

from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Car, Comment
from .forms import CommentForm

class DetailsView(View):
    def get(self, request, id):
        car = get_object_or_404(Car, pk=id)
        comments = car.comments.all()
        form = CommentForm()
        
        return render(request, 'details.html', {'car': car,'comments': comments,'form': form, })

    def post(self, request, id):
        car = get_object_or_404(Car, pk=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
        
        comments = car.comments.all()
        
        return render(request, 'details.html', { 'car': car,'comments': comments,'form': form,})
