from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey('car.Car',  on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order({self.id}): {self.user.username} - {self.car.title}"

    class Meta:
        ordering = ['-order_date']  # Newest orders first
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
