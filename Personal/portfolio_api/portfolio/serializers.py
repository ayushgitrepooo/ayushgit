from rest_framework import serializers
from .models import Project, Skill, Experience, Education, Contact

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project  # Make sure to use the actual model class, not a string
        fields = '__all__'
        
        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill  # This should be the actual model class, not a string
        fields = '__all__'        
       
        
    
'''

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = Experience
        model = '__all__'
        
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = Education
        model = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = Contact
        model = '__all__'  
        
        '''   
        
                                