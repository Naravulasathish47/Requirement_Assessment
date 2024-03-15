from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


@login_required(login_url="/login/")
def index(request):
    # Check if the user already has a profile
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # Check if the user already has a profile
            existing_profile = Profile.objects.filter(user=request.user).first()
            if existing_profile:
                # Update the existing profile instead of creating a new one
                existing_profile.email = profile.email
                existing_profile.UserName = profile.UserName
                existing_profile.Date_of_Birth = profile.Date_of_Birth
                existing_profile.Address = profile.Address
                existing_profile.Phone = profile.Phone
                existing_profile.FirstName = profile.FirstName
                existing_profile.LastName = profile.LastName
                existing_profile.save()
            else:
                # If the user doesn't have a profile, create a new one
                profile.user = request.user
                profile.save()
            return redirect('profile')  # Redirect to a page showing profile details
    else:
        form = ProfileForm()
    return render(request, 'index.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print("form is valid saving user")
            form.save()
            return redirect('login')
    else:
        print("this method itself is not working")
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url="/login/")
def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile': profile})
    except Profile.DoesNotExist:
        return render(request, 'no_profile.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login/")
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')  # Redirect to a page showing profile details
    else:
        form = ProfileForm()
    return render(request, 'index.html', {'form': form})


@login_required(login_url="/login/")
def no_profile(request):
    return render(request, 'no_profile.html')

@login_required(login_url="/login/")
def delete_profile(request):
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=request.user)
            profile.delete()
            messages.success(request, 'Profile deleted successfully.')
        except Profile.DoesNotExist:
            messages.error(request, 'No profile found for this user.')
    return render(request, 'no_profile.html')
