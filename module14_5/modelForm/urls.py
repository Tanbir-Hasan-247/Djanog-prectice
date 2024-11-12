from django.urls import path,include
from . import views

urlpatterns = [
    path("model_form/",views.model_form, name='model_form')
]