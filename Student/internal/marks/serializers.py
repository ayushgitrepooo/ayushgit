from rest_framework import serializers
from .models import User, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'date_joined', 'is_active', 'email']
        
        
class StudentSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source="user", read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        