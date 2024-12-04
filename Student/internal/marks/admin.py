from django.contrib import admin
from .models import  Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_dispaly = ['user', 'name', 'standard', 'subject', 'marks', 'teacher']
    search_fields = ['name', 'subject', 'teacher']
    list_filters = ['standard', 'subject', 'teacher']
    