from rest_framework import serializers
from .models import Calculation, User


class UserSerializer(serializers. ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'date_joined', 'is_active', 'email']

class CalculationSerializer(serializers.ModelSerializer):
     user_detail = UserSerializer(source="user", read_only=True)
     class Meta:
         model = Calculation
         fields = '__all__'
         read_only_fields = ['result', 'created_at']
         
     def validate(self, data):
         if data ['operation'] == 'divide' and data['num2'] == 0:
             raise serializers.ValidationError("Division by zero is not allowed.")
         return data
     
     def create(self, validated_data):
         num1 = validated_data['num1']
         num2 = validated_data['num2']
         operation = validated_data['operation']
         
         
         if operation == 'add':
             validated_data['result'] = num1 + num2
         elif operation == 'subtract':
             validated_data['result'] = num1 - num2
         elif operation == 'multiply': 
             validated_data['result'] = num1 * num2
         elif operation == 'divide':
             validated_data['result'] = num1 / num2
         elif operation == 'module':
             validated_data['result'] = num1 ** num2
             
         return super(). create(validated_data)
     