from django.urls import path
from .views import AddMusicianView, EditMusicianView, DeleteMusicianView

urlpatterns = [
    path('add-musician/', AddMusicianView.as_view(), name='add_musician'),
    path('edit-musician/<int:id>/', EditMusicianView.as_view(), name='edit_musician'),
    path('delete-musician/<int:id>/', DeleteMusicianView.as_view(), name='delete_musician'),
]
