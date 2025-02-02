from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

users = [
    {
        'user_name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '555-555-5555',
        'password': 'password1'
        },
    {
        'user_name': 'Jane Doe',
        'email': 'janedoe@gmail.com',
        'phone': '555-555-5553',
        'password': 'password2'
    }
]
def home(request):
    return render(request, 'users/home.html', {'users': users, 'title': 'User Profile'})

def about(request):
    return render(request, 'users/about.html', {'title': 'About'})

@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html', {'users': users, 'title': 'User Profile'})