from django.urls import path, include
from . import views

urlpatterns = [
    path("about/",views.about),
    path("pages/",views.pages),
    path("bloge/",views.bloge),
]