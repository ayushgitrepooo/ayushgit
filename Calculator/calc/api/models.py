from django.db import models
from django.contrib.auth.models import User

class Calculation(models.Model):
    OPERATION_CHOICES = [
        ('add', 'Addition'),
        ('subtract', 'Subtraction'),
        ('multiply', 'Multiplication'),
        ('divide', 'Division'),
        ('module', 'Modulus')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=10,  choices=OPERATION_CHOICES)
    result = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.num1} {self.operation} {self.num2} {self.result}"
    
    
    
     