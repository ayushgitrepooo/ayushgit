from django.db import models

# Create your models here.

class Project(models.Model):
     title = models.CharField(max_length=200)
     description = models.TextField()
     technologies = models.CharField(max_length=50)
     project_url = models.URLField(blank=True, null=True)
     github_link = models.URLField(blank=True, null=True)
     image = models.ImageField(upload_to='project/', blank=True, null=True)
     
     def __str__(self):
        return self.title
     
     
class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency =  models.IntegerField()  # 1 - 100 scale
    
    
class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    complete_year = models.IntegerField()
    
class Contact(models.Model):
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    
            
    
    
    
    
       
     