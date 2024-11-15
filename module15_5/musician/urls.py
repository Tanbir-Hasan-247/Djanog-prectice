from django.urls import path,include
from . import views

urlpatterns = [
    path('add_musician', views.addMusician, name='add_musician'),
    path('edit/<int:id>', views.editMusician, name='edit_musician'),
    path('delete/<int:id>', views.deleteMusician, name='delete_musician')
]
