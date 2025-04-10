from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer, AttendenceSerializer
from .models import Student, Attendence
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class AttendenceViewSet(viewsets.ModelViewSet):
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    