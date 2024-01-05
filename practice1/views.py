from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import singup_forms


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = singup_forms(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            login(request, form.get_user())
            messages.success(request, 'Account created and logged in successfully!')
            return redirect('home')
    else:
        form = singup_forms()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass)
            
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})



def log_out(request):
    logout(request)
    return redirect('home')

def profile(request):
    return render(request, 'profile.html')