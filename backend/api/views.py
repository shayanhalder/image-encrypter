from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import FileResponse
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
from django.http import JsonResponse
from django.core.files.uploadedfile import TemporaryUploadedFile
from . import cdn
import json

# Create your views here.
@api_view(['POST'])
def encrypt_image_message(request):
    print('got request...', request)
    
    file : TemporaryUploadedFile = request.FILES.get('file')
    # print('file: ', file)
    # print('file content type: ', file.content_type) 
    
    data = request.data
    
    body = json.loads(data['body'])
    file_name = body['file_name']
    # print('file name: ', file_name)
    
    if file:
        if file.content_type == "image/jpeg" or file.content_type == "image/png":
            response = cdn.upload_file(file, host_path=f'uploaded_images/{file_name}')
            
            return JsonResponse(response) 
             
    return HttpResponse("Invalid request. ", status=400)


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




