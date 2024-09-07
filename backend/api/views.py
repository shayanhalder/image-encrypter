from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from . import cdn
import json
from . import encrypt

VAlID_FILE_TYPES = {"image/jpeg", "image/png", "application/pdf"}

@api_view(['POST'])
def encrypt_image_message(request):
    print('got request...', request)
    
    file : InMemoryUploadedFile = request.FILES.get('file')
    data = request.data
    
    body = json.loads(data['body'])
    file_name = body['file_name']
    message = body['message']
    username = body['username']
    override = body['override']
    print('override: ', override)
    
    encrypted_file = encrypt.encrypt_image_message(file, message)
    if encrypted_file and encrypted_file.content_type in VAlID_FILE_TYPES:
        response = cdn.upload_file(encrypted_file, username=username, file_name=file_name, override=override)    
        return JsonResponse(response) 
             
    return HttpResponse("Invalid request. ", status=400)


@api_view(['POST'])
def decrypt_image_message(request):
    print('got request...', request)
    
    file : InMemoryUploadedFile = request.FILES.get('file')  
    
    message = encrypt.decrypt_image_message(file)
    print('message is: ', message)
    
    return JsonResponse({'message': message}) 


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # list of all diff objects to make sure we don't create a user that doesn't already exist
    serializer_class = UserSerializer # tells view what kind of data we need to accept to make a new user (username and password)
    permission_classes = [AllowAny] # allow anyone to create a new user even if they are not authenticated




