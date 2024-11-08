from django.contrib.auth.models import User
from django.db import models

class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='memories/upload')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
