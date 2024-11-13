from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/',views.signup, name= "signup"),
    path('login/', views.Login, name= 'loginpage'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.Logout, name='logout'),
    path('changePassword/', views.changePass, name='changePass'),
    path('changePassword2/', views.changePass2, name='changePass2'),
    path('Personal_information/',views.showProfile, name='showProfile'),
    path('EditProfile/', views.editProfile, name='editProfile')
]