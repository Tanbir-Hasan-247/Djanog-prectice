from django.urls import path
from .views import (
    SignupView, LoginView, changePass, changePass2, ProfileView, ShowProfileView, EditProfileView, Logout
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='loginpage'),
    path('logout/', Logout, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('changePassword/', changePass, name='changePass'),
    path('changePassword2/', changePass2, name='changePass2'),
    path('show-profile/', ShowProfileView.as_view(), name='showProfile'),
    path('edit-profile/', EditProfileView.as_view(), name='editProfile'),
]
