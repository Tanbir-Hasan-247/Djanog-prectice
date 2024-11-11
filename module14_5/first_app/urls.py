from django.urls import path,include
from . import views

urlpatterns = [
    path("django_form/",views.django_form, name='django_form')
]