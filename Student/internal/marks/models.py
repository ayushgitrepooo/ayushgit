from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    standard = models.IntegerField()
    subject = models.CharField(max_length=30)
    marks = models.IntegerField()
    teacher = models.CharField(max_length=20)
    
    
    def __str__(self):
         return f"{self.name}" 