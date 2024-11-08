from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home1),
    path("app_2/",include("app_2.urls"))
]