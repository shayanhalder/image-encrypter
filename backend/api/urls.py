from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),    
    path("encrypt-image-message/", views.encrypt_image_message, name="encrypt-image-message"),
    path("decrypt-image-message/", views.decrypt_image_message, name="decrypt-image-message"),
]


