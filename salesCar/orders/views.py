from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import Order

@login_required
def History(request):
    # Filter orders to show only the ones for the logged-in user
    data = Order.objects.filter(user=request.user)
    return render(request, 'history.html', {'data': data})
