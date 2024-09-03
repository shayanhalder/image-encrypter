from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
            # all fields we want to serializers when we acccept and return a users
        extra_kwargs = {"password": {"write_only": True }}
            # we want to accept password when we're creating a new user 
            # but we don't want to return the password when we are 
            # # getting information about the user
            
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {'author': {'read_only': True}}
        
    
        
        
        




