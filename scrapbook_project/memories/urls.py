from django.urls import path
from . import views

urlpatterns = [
    path('', views.memory_list, name='memory_list'),
    path('add/', views.add_memory, name='add_memory'),
]
