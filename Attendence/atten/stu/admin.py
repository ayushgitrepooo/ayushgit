from django.contrib import admin
from .models import Student, Attendence
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'standard', 'created_at']
    
@admin.register(Attendence)   
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['attendence']
    
    
        
