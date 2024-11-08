from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home2),
    path("app_3/",include("app_3.urls"))
]