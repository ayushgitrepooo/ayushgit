from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework import viewsets
from .models import Student
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
   # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
   # filter_backends = [DjangoFilterBackend]
   # filterset_fields = ['marks']
    