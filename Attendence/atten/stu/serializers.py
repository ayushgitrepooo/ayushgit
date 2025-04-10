from .models import Student, Attendence
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'standard', 'created_at']
        
        
class AttendenceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Attendence
        fields = [ 'student', 'attendence']