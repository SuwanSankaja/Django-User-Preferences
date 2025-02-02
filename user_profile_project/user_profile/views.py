from django.shortcuts import render

def home(request):
    return render(request, 'user_profile/profile.html')

def about(request):
    return render(request, 'user_profile/about.html')