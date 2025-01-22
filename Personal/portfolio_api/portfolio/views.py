from django.shortcuts import render
from .serializers import ProjectSerializer, SkillSerializer
from .models import Project, Skill
from rest_framework import viewsets

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
        