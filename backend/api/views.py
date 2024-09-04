from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import FileResponse
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
@api_view(['POST'])
def encrypt_image_message(request):
    print('got image!')
    file = request.FILES.get('file')
    
    if file:
        if file.content_type == "image/jpeg":
            with open('test_file.jpg', 'wb') as save_file:
                for chunk in file.chunks():
                    save_file.write(chunk)
            
            with open('test_file.jpg', 'a+b') as save_file:
                save_file.write(b'hello world!')
                image_data = save_file.read()
            
            return HttpResponse(image_data, content_type='image/jpeg', status=200) # "File uploaded successfully", status=200)
        
        
            # with open('test_file.jpg', 'rb') as save_file:
            #     data = save_file.read()
            #     start = data.index(bytes.fromhex('FFD9'))
                
            #     save_file.seek(start + 2)
            #     save_file.write(b'Hello world!')
                
                
                
        
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




