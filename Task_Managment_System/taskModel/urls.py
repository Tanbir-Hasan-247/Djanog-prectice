from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/', views.add_Task, name='add_Task'),
    
    path('edit/<int:id>', views.editTask, name='edit_task'),
    path('delete/<int:id>', views.deleteTask, name='delete_task')
]