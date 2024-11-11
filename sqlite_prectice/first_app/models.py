from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    rool = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField()

    def __str__(self):
        return f"Roll : {self.rool} - {self.name}"