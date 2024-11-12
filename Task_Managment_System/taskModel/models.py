from django.db import models
from taskCategory.models import Category
# Create your models here.
class Model(models.Model):
    task_title = models.CharField(max_length=200)
    task_description =models.TextField()
    is_completed = models.BooleanField()
    category = models.ManyToManyField(Category)
    task_assign_date =models.DateField()

    def __str__(self):
        return f'{self.task_title}'
  