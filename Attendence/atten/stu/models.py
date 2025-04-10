from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    standard = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
       
    def __str__(self):
        return self.name
    
class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendence')
    attendence = models.CharField(max_length=5)
    
    
    
     
    
    
    