from django.urls import path,include
from . import views

urlpatterns = [
    path('add_album', views.addAlbum, name='add_album'),
    path('edit/<int:id>', views.editAlbum, name='edit_album')
]
