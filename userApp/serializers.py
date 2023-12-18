from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=CustomUser
        fields=['email','password']
        
    def create(self,validated_data):
        user=CustomUser.objects.create_user(**validated_data)    


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     class Meta:
#         fields = ('email','password','token')        