from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# django automatically converts to correct database code
# we define python version of our models in our class that we want to store in database tables
# django will automatically add them in our database correctly

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return self.title
    

