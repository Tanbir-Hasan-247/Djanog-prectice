from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.History, name="history")
]
