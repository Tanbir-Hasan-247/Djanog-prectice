from django.db import models
from brand.models import Brand

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='brand/media/images/')

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name =models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comments by {self.name}"