from django.shortcuts import render, redirect
from .froms import RegisterForm
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save(commit=True)
    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form':form})

#for longin logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                # check kortechi user database e ache kina
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  # profile page e redirect korbe
                
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user':request.user})
    else:
        return redirect('loginpage')

def Logout(request):
    logout(request)
    return redirect('loginpage')

#for changing passwoard
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash

def changePass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'changePass.html', {'form':form})
    else:
        return redirect('loginpage')
    
def changePass2(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'changePass2.html', {'form':form})
    else:
        return redirect('loginpage')

#for showing frofile impormation
from .froms import show_profile

def showProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = show_profile(request.POST, instance=request.user)
            
        else:
            form = show_profile(instance=request.user)
        return render(request, 'profileImpo.html', {'form': form})
    else:
        return redirect('signup')
    
# For Editing your profile
from .froms import EditProfile

def editProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfile(request.POST, instance=request.user)
            if form.is_valid():
                # messages.success(request, 'Account updated successfully')
                form.save()
                return redirect('showProfile')
        else:
            form = EditProfile(instance=request.user)
        return render(request, 'editprofile.html', {'form': form})
    else:
        return redirect('signup')